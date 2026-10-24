# Al–Mo phases

> Al–Mo system: 15 phases (tier A 6, tier B 1, tier C 4, liquid 1, needs_review 3); 14 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-MO.html · Markdown: https://data.orchid-project.org/phases/pages/AL-MO.md

15 phases (tier A 6, tier B 1, tier C 4, liquid 1, needs_review 3); 14 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-MO) · [full JSON](https://data.orchid-project.org/phases/systems/AL-MO.json) · [Al–Mo system page](https://data.orchid-project.org/systems/AL-MO.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-MO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Mo system (15)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL12MO](#phase-al-mo-al12mo); _phase:al-mo:al12mo_ | Al12W · cI26 · Im-3 (204) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–985.17 K, x(Mo) 0.07692–0.07692 | 13 | 5 |
| [AL17MO4](#phase-al-mo-al17mo4); _phase:al-mo:al17mo4_ | Al17Mo4 · mC84 · C2 (5) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1270.43 K, x(Mo) 0.19048–0.19048 | 16 | 3 |
| [AL22MO5](#phase-al-mo-al22mo5); _phase:al-mo:al22mo5_ | Al22Mo5 · oF216 · Fdd2 (43) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1218.43 K, x(Mo) 0.18519–0.18519 | 8 | 3 |
| [AL3MO](#phase-al-mo-al3mo); _phase:al-mo:al3mo_ | Al3Mo · mC32 · Cm (8) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 1017.49–1495.16 K, x(Mo) 0.25–0.25 | 21 | 3 |
| [AL4MO](#phase-al-mo-al4mo); _phase:al-mo:al4mo_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–1425.24 K, x(Mo) 0.2–0.2 | 22 | 5 |
| [AL5MO](#phase-al-mo-al5mo); _phase:al-mo:al5mo_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–1119.15 K, x(Mo) 0.16667–0.16667 | 15 | 5 |
| [AL63MO37](#phase-al-mo-al63mo37); _phase:al-mo:al63mo37_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 1740–1930 K, x(Mo) 0.37–0.37 | 18 | 5 |
| [AL8MO3](#phase-al-mo-al8mo3); _phase:al-mo:al8mo3_ | Al8Mo3 · mC22 · C2/m (12) | tier B: DFT-supported (unique MP + OQMD match) | stable in 6 of 6 calculated diagram(s): 300–1855.47 K, x(Mo) 0.27273–0.27273 | 43 | 6 |
| [ALMO_A2](#phase-al-mo-almo-a2); _phase:al-mo:almo-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1462.8–2028.92 K, x(Mo) 0.5–0.5 | 0 | 1 |
| [ALMO3_A15](#phase-al-mo-almo3-a15); _phase:al-mo:almo3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2423.16 K, x(Mo) 0.70774–0.77614 | 20 | 6 |
| [BCC_A2](#phase-al-mo-bcc-a2); _phase:al-mo:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–3999.87 K, x(Mo) 0.44747–1 | 4 | 8 |
| [B2_BCC](#phase-al-mo-bcc-b2); _phase:al-mo:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.77 K, x(Mo) 0.46835–1 | 0 | 2 |
| [FCC_A1](#phase-al-mo-fcc-a1); _phase:al-mo:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–934 K, x(Mo) 0–0.00099 | 4 | 6 |
| [HCP_A3](#phase-al-mo-hcp-a3); _phase:al-mo:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-al-mo-liquid); _phase:al-mo:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 914.88–4000 K, x(Mo) 0–1 | 94 | 6 |

## AL12MO (Al–Mo)

- Id: `phase:al-mo:al12mo`; status `assigned`
- Structure: Al12W · cI26 · Im-3 (204); type `st:al12w-ci26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.9231, Mo 0.0769
- Stability: stable in 5 of 5 calculated diagram(s): 300–985.17 K, x(Mo) 0.07692–0.07692
- Literature: 13 values (13 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al12mo)

Names (9): _corpus: _corpus:phase:al-mo:al12mo  
_paper: _paper:10.1007/s11669-009-9564-4:Al12Mo, paper:10.1007/s11669-997-0063-1:Al12Mo, paper:10.1016/j.intermet.2010.03.010:Al12Mo  
_tdb: _tdb:AlMo-09Du.tdb:AL12MO, tdb:AlMo-10Cup.tdb:AL12MO, tdb:AlMo-16Pen.tdb:AL12MO, tdb:AlMo-97Sau.tdb:AL12MO, tdb:AlMo-98Sau-LB.tdb:AL12MO  


### TDB models of AL12MO (5): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL12MO, type code %, sha256 `2eb56c9f75298670…`

~~~~text
40: PHASE AL12MO % 2 12 1 !
41: CONST AL12MO : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL12MO, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
44: PHASE AL12MO % 2 12 1 !
45: CONST AL12MO : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL12MO, type code %, sha256 `b64c311d043cc74d…`

~~~~text
58: PHASE AL12MO % 2 12 1 !
59: CONST AL12MO : AL : MO : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): AL12MO, type code %, sha256 `709eda501ac1bee8…`

~~~~text
47: PHASE AL12MO % 2 12 1 !
48: CONST AL12MO : AL : MO : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): AL12MO, type code %, sha256 `bc4d36f89701a2a5…`

~~~~text
62: PHASE AL12MO % 2 12 1 !
63: CONST AL12MO : AL : MO : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
_cited as the source of values for this phase_

## AL17MO4 (Al–Mo)

- Id: `phase:al-mo:al17mo4`; status `assigned`
- Structure: Al17Mo4 · mC84 · C2 (5); type `st:al17mo4-mc84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.8095, Mo 0.1905
- Stability: stable in 3 of 3 calculated diagram(s): 300–1270.43 K, x(Mo) 0.19048–0.19048
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al17mo4)

Names (6): _corpus: _corpus:phase:al-mo:al17mo4  
_paper: _paper:10.1007/s11669-009-9564-4:Al17Mo4, paper:10.1016/j.intermet.2010.03.010:Al17Mo4  
_tdb: _tdb:AlMo-09Du.tdb:AL17MO4, tdb:AlMo-10Cup.tdb:AL17MO4, tdb:AlMo-16Pen.tdb:AL17MO4  


### TDB models of AL17MO4 (3): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL17MO4, type code %, sha256 `2eb56c9f75298670…`

~~~~text
56: PHASE AL17MO4 % 2 17 4 !
57: CONST AL17MO4 : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL17MO4, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
60: PHASE AL17MO4 % 2 17 4 !
61: CONST AL17MO4 : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL17MO4, type code %, sha256 `b64c311d043cc74d…`

~~~~text
74: PHASE AL17MO4 % 2 17 4 !
75: CONST AL17MO4 : AL : MO : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
_cited as the source of values for this phase_

## AL22MO5 (Al–Mo)

- Id: `phase:al-mo:al22mo5`; status `assigned`
- Structure: Al22Mo5 · oF216 · Fdd2 (43); type `st:al22mo5-of216`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.8148, Mo 0.1852
- Stability: stable in 3 of 3 calculated diagram(s): 300–1218.43 K, x(Mo) 0.18519–0.18519
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al22mo5)

Names (6): _corpus: _corpus:phase:al-mo:al22mo5  
_paper: _paper:10.1007/s11669-009-9564-4:Al22Mo5, paper:10.1016/j.intermet.2010.03.010:Al22Mo5  
_tdb: _tdb:AlMo-09Du.tdb:AL22MO5, tdb:AlMo-10Cup.tdb:AL22MO5, tdb:AlMo-16Pen.tdb:AL22MO5  


### TDB models of AL22MO5 (3): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL22MO5, type code %, sha256 `2eb56c9f75298670…`

~~~~text
51: PHASE AL22MO5 % 2 22 5 !
52: CONST AL22MO5 : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL22MO5, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
55: PHASE AL22MO5 % 2 22 5 !
56: CONST AL22MO5 : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL22MO5, type code %, sha256 `b64c311d043cc74d…`

~~~~text
69: PHASE AL22MO5 % 2 22 5 !
70: CONST AL22MO5 : AL : MO : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
_cited as the source of values for this phase_

## AL3MO (Al–Mo)

- Id: `phase:al-mo:al3mo`; status `assigned`
- Structure: Al3Mo · mC32 · Cm (8); type `st:al3mo-mc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.7500, Mo 0.2500
- Stability: stable in 3 of 3 calculated diagram(s): 1017.49–1495.16 K, x(Mo) 0.25–0.25
- Literature: 21 values (21 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al3mo)

Names (7): _corpus: _corpus:phase:al-mo:al3mo  
_paper: _paper:10.1007/s11669-009-9564-4:Al3Mo, paper:10.1007/s11669-997-0063-1:Al3Mo, paper:10.1016/j.intermet.2010.03.010:Al3Mo  
_tdb: _tdb:AlMo-09Du.tdb:AL3MO, tdb:AlMo-10Cup.tdb:AL3MO, tdb:AlMo-16Pen.tdb:AL3MO  


### TDB models of AL3MO (3): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL3MO, type code %, sha256 `2eb56c9f75298670…`

~~~~text
66: PHASE AL3MO % 2 3 1 !
67: CONST AL3MO : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL3MO, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
70: PHASE AL3MO % 2 3 1 !
71: CONST AL3MO : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL3MO, type code %, sha256 `b64c311d043cc74d…`

~~~~text
84: PHASE AL3MO % 2 3 1 !
85: CONST AL3MO : AL : MO : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_reports values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
_cited as the source of values for this phase_

## AL4MO (Al–Mo)

- Id: `phase:al-mo:al4mo`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Al17Mo4 · mC84 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Al17Mo4 · mC84 · C2 (5) — Hallstedt 2025 mmc2 row for AL4MO: Al4Mo
- Candidate (sgte_mmc2): Al4W · mC30 · Cm (8) — Hallstedt 2025 mmc2 row for AL4MO: Al4Mo
- Candidate (tdb_comment): Al4W · mC30 · Cm — AlMo-09Du.tdb: 'Prototype Al4W (mC30, Cm)'
- Candidate (tdb_comment): Al4W · mC30 · Cm — AlMo-10Cup.tdb: 'Prototype Al4W (mC30, Cm)'
- Candidate (tdb_comment): Al4W · mC30 · Cm — AlMo-16Pen.tdb: 'Prototype Al4W (mC30, Cm)'
- Candidate (tdb_comment): Al17Mo4 · mC84 · C2 — AlMo-97Sau.tdb: 'Prototype Al17Mo4 (mC84, C2) and Al4W (mC30, Cm)'
- Candidate (tdb_comment): Al17Mo4 · mC84 · C2 — AlMo-98Sau-LB.tdb: 'Prototype Al17Mo4 (mC84, C2) and Al4W (mC30, Cm)'
- Stoichiometry: Al 0.8000, Mo 0.2000
- Stability: stable in 5 of 5 calculated diagram(s): 300–1425.24 K, x(Mo) 0.2–0.2
- Literature: 22 values (22 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al4mo)

Names (9): _corpus: _corpus:phase:al-mo:al4mo  
_paper: _paper:10.1007/s11669-009-9564-4:Al4Mo, paper:10.1007/s11669-997-0063-1:Al4Mo, paper:10.1016/j.intermet.2010.03.010:Al4Mo  
_tdb: _tdb:AlMo-09Du.tdb:AL4MO, tdb:AlMo-10Cup.tdb:AL4MO, tdb:AlMo-16Pen.tdb:AL4MO, tdb:AlMo-97Sau.tdb:AL4MO, tdb:AlMo-98Sau-LB.tdb:AL4MO  


### TDB models of AL4MO (5): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL4MO, type code %, sha256 `2eb56c9f75298670…`

~~~~text
61: PHASE AL4MO % 2 4 1 !
62: CONST AL4MO : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL4MO, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
65: PHASE AL4MO % 2 4 1 !
66: CONST AL4MO : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL4MO, type code %, sha256 `b64c311d043cc74d…`

~~~~text
79: PHASE AL4MO % 2 4 1 !
80: CONST AL4MO : AL : MO : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): AL4MO, type code %, sha256 `709eda501ac1bee8…`

~~~~text
58: PHASE AL4MO % 2 4 1 !
59: CONST AL4MO : AL : MO : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): AL4MO, type code %, sha256 `bc4d36f89701a2a5…`

~~~~text
73: PHASE AL4MO % 2 4 1 !
74: CONST AL4MO : AL : MO : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
_cited as the source of values for this phase_

## AL5MO (Al–Mo)

- Id: `phase:al-mo:al5mo`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (dft_oqmd): P6322 (182) — on-hull OQMD Al5 Mo1 at x(MO)=0.1667
- Candidate (literature_printed): Al5Mo · hR12 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Al5Mo · hR12 · R-3c (167) — Hallstedt 2025 mmc2 row for AL5MO: Al5Mo (low T)
- Candidate (sgte_mmc2): Al5W · hP12 · P6_322 (182) — Hallstedt 2025 mmc2 row for AL5MO: Al5Mo (high T)
- Candidate (tdb_comment): Al5Mo · hR12 · R-3c — AlMo-09Du.tdb: 'Prototype Al5Mo (hR12, R-3c), low T'
- Candidate (tdb_comment): Al5W · hP12 · P6_322 — AlMo-09Du.tdb: 'Prototype Al5W (hP12, P6_322), high T'
- Candidate (tdb_comment): Al5Mo · hR12 · R-3c — AlMo-10Cup.tdb: 'Prototype Al5Mo (hR12, R-3c), low T'
- Candidate (tdb_comment): Al5W · hP12 · P6_322 — AlMo-10Cup.tdb: 'Prototype Al5W (hP12, P6_322), high T'
- Stoichiometry: Al 0.8333, Mo 0.1667
- Stability: stable in 5 of 5 calculated diagram(s): 300–1119.15 K, x(Mo) 0.16667–0.16667
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al5mo)

Names (9): _corpus: _corpus:phase:al-mo:al5mo  
_paper: _paper:10.1007/s11669-009-9564-4:Al5Mo, paper:10.1007/s11669-997-0063-1:Al5Mo, paper:10.1016/j.intermet.2010.03.010:Al5Mo  
_tdb: _tdb:AlMo-09Du.tdb:AL5MO, tdb:AlMo-10Cup.tdb:AL5MO, tdb:AlMo-16Pen.tdb:AL5MO, tdb:AlMo-97Sau.tdb:AL5MO, tdb:AlMo-98Sau-LB.tdb:AL5MO  


### TDB models of AL5MO (5): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL5MO, type code %, sha256 `2eb56c9f75298670…`

~~~~text
46: PHASE AL5MO % 2 5 1 !
47: CONST AL5MO : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL5MO, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
50: PHASE AL5MO % 2 5 1 !
51: CONST AL5MO : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL5MO, type code %, sha256 `b64c311d043cc74d…`

~~~~text
64: PHASE AL5MO % 2 5 1 !
65: CONST AL5MO : AL : MO : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): AL5MO, type code %, sha256 `709eda501ac1bee8…`

~~~~text
53: PHASE AL5MO % 2 5 1 !
54: CONST AL5MO : AL : MO : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): AL5MO, type code %, sha256 `bc4d36f89701a2a5…`

~~~~text
68: PHASE AL5MO % 2 5 1 !
69: CONST AL5MO : AL : MO : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
_cited as the source of values for this phase_

## AL63MO37 (Al–Mo)

- Id: `phase:al-mo:al63mo37`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Al63Mo37) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Al63Mo37) — Hallstedt 2025 mmc2 row for AL63MO37: Al63Mo37
- Stoichiometry: Al 0.6300, Mo 0.3700
- Stability: stable in 5 of 5 calculated diagram(s): 1740–1930 K, x(Mo) 0.37–0.37
- Literature: 18 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al63mo37)

Names (9): _corpus: _corpus:phase:al-mo:al63mo37  
_paper: _paper:10.1007/s11669-009-9564-4:Al63Mo37, paper:10.1007/s11669-997-0063-1:Al63Mo37, paper:10.1016/j.intermet.2010.03.010:Al63Mo37  
_tdb: _tdb:AlMo-09Du.tdb:AL63MO37, tdb:AlMo-10Cup.tdb:AL63MO37, tdb:AlMo-16Pen.tdb:AL63MO37, tdb:AlMo-97Sau.tdb:AL63MO37, tdb:AlMo-98Sau-LB.tdb:AL63MO37  


### TDB models of AL63MO37 (5): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL63MO37, type code %, sha256 `2eb56c9f75298670…`

~~~~text
76: PHASE AL63MO37 % 2 63 37 !
77: CONST AL63MO37 : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL63MO37, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
80: PHASE AL63MO37 % 2 63 37 !
81: CONST AL63MO37 : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL63MO37, type code %, sha256 `b64c311d043cc74d…`

~~~~text
94: PHASE AL63MO37 % 2 63 37 !
95: CONST AL63MO37 : AL : MO : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): AL63MO37, type code %, sha256 `709eda501ac1bee8…`

~~~~text
68: PHASE AL63MO37 % 2 63 37 !
69: CONST AL63MO37 : AL : MO : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): AL63MO37, type code %, sha256 `bc4d36f89701a2a5…`

~~~~text
83: PHASE AL63MO37 % 2 63 37 !
84: CONST AL63MO37 : AL : MO : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_

## AL8MO3 (Al–Mo)

- Id: `phase:al-mo:al8mo3`; status `assigned`
- Structure: Al8Mo3 · mC22 · C2/m (12); type `st:al8mo3-mc22`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.7273, Mo 0.2727
- Stability: stable in 6 of 6 calculated diagram(s): 300–1855.47 K, x(Mo) 0.27273–0.27273
- Literature: 43 values (43 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:al8mo3)

Names (12): _corpus: _corpus:phase:al-mo:al8mo3  
_mp: _mp:mp-aaaaaebd  
_oqmd: _oqmd:oqmd-10509  
_paper: _paper:10.1007/s11669-009-9564-4:Al8Mo3, paper:10.1007/s11669-997-0063-1:Al8Mo3, paper:10.1016/j.intermet.2010.03.010:Al8Mo3  
_tdb: _tdb:AlMo-09Du.tdb:AL8MO3, tdb:AlMo-10Cup.tdb:AL8MO3, tdb:AlMo-16Pen.tdb:AL8MO3, tdb:AlMo-97Cos.tdb:AL8MO3, tdb:AlMo-97Sau.tdb:AL8MO3, tdb:AlMo-98Sau-LB.tdb:AL8MO3  


### TDB models of AL8MO3 (6): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): AL8MO3, type code %, sha256 `2eb56c9f75298670…`

~~~~text
71: PHASE AL8MO3 % 2 8 3 !
72: CONST AL8MO3 : AL : MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): AL8MO3, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
75: PHASE AL8MO3 % 2 8 3 !
76: CONST AL8MO3 : AL : MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): AL8MO3, type code %, sha256 `b64c311d043cc74d…`

~~~~text
89: PHASE AL8MO3 % 2 8 3 !
90: CONST AL8MO3 : AL : MO : !
~~~~

[AlMo-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Cos.tdb): AL8MO3, type code %, sha256 `ddd7a660ca5292b2…`

~~~~text
43: PHASE AL8MO3 % 2 8 3 !
44: CONST AL8MO3 : AL : MO : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): AL8MO3, type code %, sha256 `709eda501ac1bee8…`

~~~~text
63: PHASE AL8MO3 % 2 8 3 !
64: CONST AL8MO3 : AL : MO : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): AL8MO3, type code %, sha256 `bc4d36f89701a2a5…`

~~~~text
78: PHASE AL8MO3 % 2 8 3 !
79: CONST AL8MO3 : AL : MO : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
_cited as the source of values for this phase_

## ALMO_A2 (Al–Mo)

- Id: `phase:al-mo:almo-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.5000, Mo 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 1462.8–2028.92 K, x(Mo) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:almo-a2)

Names (2): _corpus: _corpus:phase:al-mo:almo-a2  
_tdb: _tdb:AlMo-97Cos.tdb:ALMO_A2  


### TDB models of ALMO_A2 (1): PHASE and CONSTITUENT statements as written

[AlMo-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Cos.tdb): ALMO_A2, type code %, sha256 `ddd7a660ca5292b2…`

~~~~text
48: PHASE ALMO_A2 % 2 1 1 !
49: CONST ALMO_A2 : AL : MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_

## ALMO3_A15 (Al–Mo)

- Id: `phase:al-mo:almo3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlMo-09Du.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlMo-10Cup.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlMo-16Pen.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–2423.16 K, x(Mo) 0.70774–0.77614
- Literature: 20 values (20 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:almo3-a15)

Names (10): _corpus: _corpus:phase:al-mo:almo3-a15  
_paper: _paper:10.1007/s11669-009-9564-4:AlMo3, paper:10.1007/s11669-997-0063-1:AlMo3, paper:10.1016/j.intermet.2010.03.010:δ-AlMo3  
_tdb: _tdb:AlMo-09Du.tdb:ALMO3_A15, tdb:AlMo-10Cup.tdb:ALMO3_A15, tdb:AlMo-16Pen.tdb:ALMO3_A15, tdb:AlMo-97Cos.tdb:ALMO3_A15, tdb:AlMo-97Sau.tdb:ALMO3_A15, tdb:AlMo-98Sau-LB.tdb:ALMO3_A15  


### TDB models of ALMO3_A15 (6): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): ALMO3_A15, type code %, sha256 `2eb56c9f75298670…`

~~~~text
81: PHASE ALMO3_A15 % 2 1 3 !
82: CONST ALMO3_A15 : AL% MO : AL MO% : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): ALMO3_A15, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
85: PHASE ALMO3_A15 % 2 1 3 !
86: CONST ALMO3_A15 : AL% MO : AL MO% : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): ALMO3_A15, type code %, sha256 `b64c311d043cc74d…`

~~~~text
99: PHASE ALMO3_A15 % 2 1 3 !
100: CONST ALMO3_A15 : AL% MO : AL MO% : !
~~~~

[AlMo-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Cos.tdb): ALMO3_A15, type code %, sha256 `ddd7a660ca5292b2…`

~~~~text
53: PHASE ALMO3_A15 % 2 1 3 !
54: CONST ALMO3_A15 : AL : MO : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): ALMO3_A15, type code %, sha256 `709eda501ac1bee8…`

~~~~text
73: PHASE ALMO3_A15 % 2 1 3 !
74: CONST ALMO3_A15 : AL : MO : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): ALMO3_A15, type code %, sha256 `bc4d36f89701a2a5…`

~~~~text
88: PHASE ALMO3_A15 % 2 1 3 !
89: CONST ALMO3_A15 : AL : MO : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_

## BCC_A2 (Al–Mo)

- Id: `phase:al-mo:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–3999.87 K, x(Mo) 0.44747–1
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:bcc-a2)

Names (12): _corpus: _corpus:phase:al-mo:bcc-a2  
_paper: _paper:10.1007/s11669-009-9564-4:bcc(Mo), paper:10.1007/s11669-997-0063-1:(Mo), paper:10.1007/s11669-997-0063-1:Mo  
_tdb: _tdb:AlMo-09Du.tdb:BCC_A2, tdb:AlMo-10Cup.tdb:BCC_A2, tdb:AlMo-16Pen.tdb:A2_BCC, tdb:AlMo-16Pen.tdb:BCC_A2, tdb:AlMo-97Cos.tdb:BCC_A2, tdb:AlMo-97Sau.tdb:BCC_A2, tdb:AlMo-98Sau-LB.tdb:A2_BCC, tdb:AlMo-98Sau-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (8): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): BCC_A2, type code %B, sha256 `2eb56c9f75298670…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL MO% : VA : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): BCC_A2, type code %B, sha256 `87c3f97cf72fd336…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL MO% : VA : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): A2_BCC, type code %B, sha256 `b64c311d043cc74d…`

~~~~text
43: PHASE A2_BCC %B 2 1 3 !
44: CONST A2_BCC : AL MO% VA : VA : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): BCC_A2, type code %B, sha256 `b64c311d043cc74d…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL MO% : VA : !
~~~~

[AlMo-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Cos.tdb): BCC_A2, type code %B, sha256 `ddd7a660ca5292b2…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL MO% : VA : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): BCC_A2, type code %B, sha256 `709eda501ac1bee8…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL MO% : VA : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): A2_BCC, type code %B, sha256 `bc4d36f89701a2a5…`

~~~~text
47: PHASE A2_BCC %B 2 1 3 !
48: CONST A2_BCC : AL MO% : VA : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): BCC_A2, type code %B, sha256 `bc4d36f89701a2a5…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : AL MO% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_

## B2_BCC (Al–Mo)

- Id: `phase:al-mo:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: AlMo-16Pen.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: AlMo-98Sau-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in AlMo-16Pen.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlMo-98Sau-LB.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.77 K, x(Mo) 0.46835–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:bcc-b2)

Names (3): _corpus: _corpus:phase:al-mo:bcc-b2  
_tdb: _tdb:AlMo-16Pen.tdb:B2_BCC, tdb:AlMo-98Sau-LB.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): B2_BCC, type code %BO, sha256 `b64c311d043cc74d…`

~~~~text
48: PHASE B2_BCC %BO 3 0.5 0.5 3 !
49: CONST B2_BCC : AL% MO VA : AL MO% VA : VA : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): B2_BCC, type code %BO, sha256 `bc4d36f89701a2a5…`

~~~~text
52: PHASE B2_BCC %BO 3 0.5 0.5 3 !
53: CONST B2_BCC : AL% MO : AL MO% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_

## FCC_A1 (Al–Mo)

- Id: `phase:al-mo:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–934 K, x(Mo) 0–0.00099
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:fcc-a1)

Names (10): _corpus: _corpus:phase:al-mo:fcc-a1  
_paper: _paper:10.1007/s11669-009-9564-4:fcc, paper:10.1007/s11669-997-0063-1:(Al), paper:10.1007/s11669-997-0063-1:Al  
_tdb: _tdb:AlMo-09Du.tdb:FCC_A1, tdb:AlMo-10Cup.tdb:FCC_A1, tdb:AlMo-16Pen.tdb:FCC_A1, tdb:AlMo-97Cos.tdb:FCC_A1, tdb:AlMo-97Sau.tdb:FCC_A1, tdb:AlMo-98Sau-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): FCC_A1, type code %A, sha256 `2eb56c9f75298670…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL% MO : VA : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): FCC_A1, type code %A, sha256 `87c3f97cf72fd336…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL% MO : VA : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): FCC_A1, type code %A, sha256 `b64c311d043cc74d…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL% MO : VA : !
~~~~

[AlMo-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Cos.tdb): FCC_A1, type code %A, sha256 `ddd7a660ca5292b2…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL% MO : VA : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): FCC_A1, type code %A, sha256 `709eda501ac1bee8…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% MO : VA : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): FCC_A1, type code %A, sha256 `bc4d36f89701a2a5…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AL% MO : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_

## HCP_A3 (Al–Mo)

- Id: `phase:al-mo:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:hcp-a3)

Names (7): _corpus: _corpus:phase:al-mo:hcp-a3  
_tdb: _tdb:AlMo-09Du.tdb:HCP_A3, tdb:AlMo-10Cup.tdb:HCP_A3, tdb:AlMo-16Pen.tdb:HCP_A3, tdb:AlMo-97Cos.tdb:HCP_A3, tdb:AlMo-97Sau.tdb:HCP_A3, tdb:AlMo-98Sau-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): HCP_A3, type code %A, sha256 `2eb56c9f75298670…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL MO : VA : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): HCP_A3, type code %A, sha256 `87c3f97cf72fd336…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL MO : VA : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): HCP_A3, type code %A, sha256 `b64c311d043cc74d…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : AL MO : VA : !
~~~~

[AlMo-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Cos.tdb): HCP_A3, type code %A, sha256 `ddd7a660ca5292b2…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL MO : VA : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): HCP_A3, type code %A, sha256 `709eda501ac1bee8…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL MO : VA : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): HCP_A3, type code %A, sha256 `bc4d36f89701a2a5…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : AL MO : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_

## LIQUID (Al–Mo)

- Id: `phase:al-mo:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 914.88–4000 K, x(Mo) 0–1
- Literature: 94 values (94 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-mo:liquid)

Names (11): _corpus: _corpus:phase:al-mo:liquid  
_paper: _paper:10.1007/s11669-009-9564-4:L, paper:10.1007/s11669-997-0063-1:L, paper:10.1007/s11669-997-0063-1:Liquid, paper:10.1016/j.intermet.2010.03.010:Liquid  
_tdb: _tdb:AlMo-09Du.tdb:LIQUID, tdb:AlMo-10Cup.tdb:LIQUID, tdb:AlMo-16Pen.tdb:LIQUID, tdb:AlMo-97Cos.tdb:LIQUID, tdb:AlMo-97Sau.tdb:LIQUID, tdb:AlMo-98Sau-LB.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[AlMo-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-09Du.tdb): LIQUID, type code %, sha256 `2eb56c9f75298670…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL MO : !
~~~~

[AlMo-10Cup.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-10Cup.tdb): LIQUID, type code %, sha256 `87c3f97cf72fd336…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL MO : !
~~~~

[AlMo-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-16Pen.tdb): LIQUID, type code %, sha256 `b64c311d043cc74d…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL MO : !
~~~~

[AlMo-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Cos.tdb): LIQUID, type code %, sha256 `ddd7a660ca5292b2…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL MO : !
~~~~

[AlMo-97Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-97Sau.tdb): LIQUID, type code %, sha256 `709eda501ac1bee8…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL MO : !
~~~~

[AlMo-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlMo-98Sau-LB.tdb): LIQUID, type code %, sha256 `bc4d36f89701a2a5…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : AL MO : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-997-0063-1](https://doi.org/10.1007/s11669-997-0063-1) Thermotech Ltd., N. Saunders, The Al-Mo system (aluminum-molybdenum), JPE 18, 370-378 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2010.03.010](https://doi.org/10.1016/j.intermet.2010.03.010) Damian M. Cupid, Olga Fabrichnaya, Fereshteh Ebrahimi, Hans J. Seifert, Thermodynamic assessment of the Al–Mo system and of the Ti–Al–Mo System from 0 to 20at.% Ti, Intermetallics 18, 1185-1196 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9564-4](https://doi.org/10.1007/s11669-009-9564-4) Zhenmin Du, Cuiping Guo, Changrong Li, Weijing Zhang, Thermodynamic Description of the Al-Mo and Al-Fe-Mo Systems, J. Phase Equilib. Diffus. 30, 487-501 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.03.044](https://doi.org/10.1016/j.jallcom.2016.03.044) Jian Peng, Peter Franke, Dario Manara, Tyson Watkins, Rudy J.M. Konings, Hans J. Seifert, Experimental investigation and thermodynamic re-assessment of the Al–Mo–Ni system, Journal of Alloys and Compounds 674, 305-314 (2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.3139/146.101412](https://doi.org/10.3139/146.101412) Markus Eumann, Gerhard Sauthoff, Martin Palm, Re-evaluation of phase equilibria in the Al–Mo system, International Journal of Materials Research 97, 1502-1511 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646496](https://doi.org/10.1007/bf02646496) Julius C. Schuster, Herbert Ipser, The AI-Ali8Mo3 section of the binary system aluminum-molybdenum, Metall Trans A 22, 1729-1736 (1991).  
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
