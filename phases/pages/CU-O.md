# Cu–O phases

> Cu–O system: 10 phases (tier A 3, tier C 3, liquid 2, gas 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-O.html · Markdown: https://data.orchid-project.org/phases/pages/CU-O.md

10 phases (tier A 3, tier C 3, liquid 2, gas 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-O) · [full JSON](https://data.orchid-project.org/phases/systems/CU-O.json) · [Cu–O system page](https://data.orchid-project.org/systems/CU-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–O system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-o-bcc-a2); _phase:cu-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 5 |
| [CUPRITE_C3](#phase-cu-o-c3-cuprite); _phase:cu-o:c3-cuprite_ | Cu2O · C3 · cP6 · Pn-3m (224) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1094.79 K, x(O) 0.33333–0.33333 | 84 | 5 |
| [CU4O3](#phase-cu-o-cu4o3); _phase:cu-o:cu4o3_ | Cu4O3 · tI28 · I4_1/amd (141) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 0 | 3 |
| [CUO](#phase-cu-o-cuo); _phase:cu-o:cuo_ | CuO · B26 · mC8 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–416 K, x(O) 0.5–0.5 | 76 | 5 |
| [FCC_A1](#phase-cu-o-fcc-a1); _phase:cu-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1357.77 K, x(O) 0–0.00019 | 0 | 5 |
| [GAS](#phase-cu-o-gas); _phase:cu-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 1382.32–2500 K, x(O) 0.92505–1 | 0 | 5 |
| [HCP_A3](#phase-cu-o-hcp-a3); _phase:cu-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 5 |
| [ION](#phase-cu-o-ion); _phase:cu-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1342.77–2500 K, x(O) 0–0.39143 | 0 | 3 |
| [LIQUID](#phase-cu-o-liquid); _phase:cu-o:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1342.77–2500 K, x(O) 0–0.33882 | 18 | 2 |
| [O2GAS](#phase-cu-o-o2gas); _phase:cu-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–416 K, x(O) 1–1 | 0 | 5 |

## BCC_A2 (Cu–O)

- Id: `phase:cu-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:bcc-a2)

Names (6): _corpus: _corpus:phase:cu-o:bcc-a2  
_tdb: _tdb:CuO-03Hal-LB.tdb:BCC_A2, tdb:CuO-05Sch.tdb:BCC_A2, tdb:CuO-14Mag.tdb:BCC_A2, tdb:CuO-92Bou.tdb:BCC_A2, tdb:CuO-94Hal.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): BCC_A2, type code %B, sha256 `5836249ea0179639…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : CU : VA : !
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): BCC_A2, type code %B, sha256 `a3dbcda00b2b888e…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : CU : VA : !
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): BCC_A2, type code %B, sha256 `c359243f81916348…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : CU : VA : !
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): BCC_A2, type code %B, sha256 `01c48e87b93fb30f…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : CU : VA : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): BCC_A2, type code %B, sha256 `59102ffec95449e3…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : CU : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_

## CUPRITE_C3 (Cu–O)

- Id: `phase:cu-o:c3-cuprite`; status `assigned`
- Structure: Cu2O · C3 · cP6 · Pn-3m (224); type `st:c3-cu2o-cp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:CUPRITE); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–1094.79 K, x(O) 0.33333–0.33333
- Literature: 84 values (84 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:c3-cuprite)

Names (8): _corpus: _corpus:phase:cu-o:c3-cuprite, corpus:phase:cu-o:cuprite-c3  
_paper: _paper:10.1007/bf02649399:Cu2O  
_tdb: _tdb:CuO-03Hal-LB.tdb:CUPRITE_C3, tdb:CuO-05Sch.tdb:CUPRITE_C3, tdb:CuO-14Mag.tdb:CUPRITE_C3, tdb:CuO-92Bou.tdb:CUPRITE_C3, tdb:CuO-94Hal.tdb:CUPRITE_C3  


### TDB models of CUPRITE_C3 (5): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): CUPRITE_C3, type code %, sha256 `5836249ea0179639…`

~~~~text
57: PHASE CUPRITE_C3:I % 2 2 1 !
58: CONST CUPRITE_C3:I : CU+1 : O-2 : !
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): CUPRITE_C3, type code %, sha256 `a3dbcda00b2b888e…`

~~~~text
58: PHASE CUPRITE_C3:I % 2 2 1 !
59: CONST CUPRITE_C3:I : CU+1 : O-2 : !
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): CUPRITE_C3, type code %, sha256 `c359243f81916348…`

~~~~text
57: PHASE CUPRITE_C3:I % 2 2 1 !
58: CONST CUPRITE_C3:I : CU+1 : O-2 : !
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): CUPRITE_C3, type code %, sha256 `01c48e87b93fb30f…`

~~~~text
59: PHASE CUPRITE_C3:I % 2 2 1 !
60: CONST CUPRITE_C3:I : CU+1 : O-2 : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): CUPRITE_C3, type code %, sha256 `59102ffec95449e3…`

~~~~text
55: PHASE CUPRITE_C3:I % 2 2 1 !
56: CONST CUPRITE_C3:I : CU+1 : O-2 : !
~~~~

Example references (10 of 16; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_
- [doi:10.1002/srin.197003613](https://doi.org/10.1002/srin.197003613) Wilhelm Anton Fischer, Gerd Pateisky, Die Eignung fester Metall-Metalloxid-Gemische als Bezugspotentiale in Sauerstoffmeßzellen, Archiv für das Eisenhüttenwesen 41, 661-673 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00639610](https://doi.org/10.1007/bf00639610) H. Peters, G. Mann, Elektrochemische Untersuchung der Reduktionsgleichgewichte von Metalloxyden, Naturwissenschaften 45, 209-209 (1958).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02654367](https://doi.org/10.1007/bf02654367) Rainer Schmid, A thermodynamic analysis of the Cu-O system with an associated solution model, Metall Trans B 14, 473-481 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0021-9614(79)90145-9](https://doi.org/10.1016/0021-9614%2879%2990145-9) N. Kemori, I. Katayama, Z. Kozuka, Measurements of standard molar Gibbs energies of formation of NiO, Cu2O, and CoO from solid and liquid metals and oxygen gas by an e.m.f. method at high temperatures, The Journal of Chemical Thermodynamics 11, 215-228 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(85)90079-7](https://doi.org/10.1016/0022-5088%2885%2990079-7) C Mallika, O.M Sreedharan, M.S Chandrasekharaiah, Determination of the standard Gibbs energy of formation of Rh2O3(s) and IrO2(s) from solid oxide electrolyte electromotive force measurements, Journal of the Less Common Metals 107, 203-212 (1985).  
_cited as the source of values for this phase_

## CU4O3 (Cu–O)

- Id: `phase:cu-o:cu4o3`; status `assigned`
- Structure: Cu4O3 · tI28 · I4_1/amd (141); type `st:cu4o3-ti28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:cu4o3)

Names (4): _corpus: _corpus:phase:cu-o:cu4o3  
_tdb: _tdb:CuO-03Hal-LB.tdb:CU4O3, tdb:CuO-14Mag.tdb:CU4O3, tdb:CuO-94Hal.tdb:CU4O3  


### TDB models of CU4O3 (3): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): CU4O3, type code %, sha256 `5836249ea0179639…`

~~~~text
67: PHASE CU4O3:I % 3 2 2 3 !
68: CONST CU4O3:I : CU+1 : CU+2 : O-2 : !
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): CU4O3, type code %, sha256 `c359243f81916348…`

~~~~text
67: PHASE CU4O3:I % 3 2 2 3 !
68: CONST CU4O3:I : CU+1 : CU+2 : O-2 : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): CU4O3, type code %, sha256 `59102ffec95449e3…`

~~~~text
65: PHASE CU4O3:I % 3 2 2 3 !
66: CONST CU4O3:I : CU+1 : CU+2 : O-2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_

## CUO (Cu–O)

- Id: `phase:cu-o:cuo`; status `assigned`
- Structure: CuO · B26 · mC8 · C2/c (15); type `st:b26-cuo-mc8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–416 K, x(O) 0.5–0.5
- Literature: 76 values (70 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:cuo)

Names (8): _corpus: _corpus:phase:cu-o:cuo  
_paper: _paper:10.1007/bf02649399:CuO, paper:10.1361/154770305x74421:CuO  
_tdb: _tdb:CuO-03Hal-LB.tdb:CUO, tdb:CuO-05Sch.tdb:CUO, tdb:CuO-14Mag.tdb:CUO, tdb:CuO-92Bou.tdb:CUO, tdb:CuO-94Hal.tdb:CUO  


### TDB models of CUO (5): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): CUO, type code %, sha256 `5836249ea0179639…`

~~~~text
62: PHASE CUO % 2 1 1 !
63: CONST CUO : CU+2 : O-2 : !
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): CUO, type code %, sha256 `a3dbcda00b2b888e…`

~~~~text
63: PHASE CUO % 2 1 1 !
64: CONST CUO : CU+2 : O-2 : !
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): CUO, type code %, sha256 `c359243f81916348…`

~~~~text
62: PHASE CUO % 2 1 1 !
63: CONST CUO : CU+2 : O-2 : !
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): CUO, type code %, sha256 `01c48e87b93fb30f…`

~~~~text
64: PHASE CUO:I % 2 1 1 !
65: CONST CUO:I : CU+2 : O-2 : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): CUO, type code %, sha256 `59102ffec95449e3…`

~~~~text
60: PHASE CUO % 2 1 1 !
61: CONST CUO : CU+2 : O-2 : !
~~~~

Example references (10 of 15; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_
- [doi:10.1021/ja01438a009](https://doi.org/10.1021/ja01438a009) H. S. Roberts, F. Hastings Smyth, THE SYSTEM COPPER: CUPRIC OXIDE: OXYGEN., J. Am. Chem. Soc. 43, 1061-1079 (1921).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02654367](https://doi.org/10.1007/bf02654367) Rainer Schmid, A thermodynamic analysis of the Cu-O system with an associated solution model, Metall Trans B 14, 473-481 (1983).  
_cited as the source of values for this phase_
- [doi:10.1021/ja01106a056](https://doi.org/10.1021/ja01106a056) Jih-Heng Hu, Herrick L. Johnston, Low Temperature Heat Capacities of Inorganic Solids. XVI. Heat Capacity of Cupric Oxide from 15 to 300 °K.\<sup>1\</sup>, J. Am. Chem. Soc. 75, 2471-2473 (1953).  
_cited as the source of values for this phase_
- [doi:10.1002/hlca.19440270195](https://doi.org/10.1002/hlca.19440270195) W. Feitknecht, Über die Löslichkeitsprodukte der Oxyde und des Hydroxyds von Kupfer und über die Löslichkeit von Kupferhydroxyd in Natronlauge, Helvetica Chimica Acta 27, 771-775 (1944).  
_cited as the source of values for this phase_
- [doi:10.1002/hlca.19650480528](https://doi.org/10.1002/hlca.19650480528) P. Schindler, H. Althaus, F. Hofer, W. Minder, Löslichkeitsprodukte von Metalloxiden und ‐hydroxiden. 10. Mitteilung. Löslichkeitsprodukte von Zinkoxid, Kupferhydroxid und Kupferoxid in Abhängigkeit von Teilchengrösse und molarer Oberfläche. Ein Beitrag zur Thermodynamik von Grenzflächen fest‐flüssig, Helvetica Chimica Acta 48, 1204-1215 (1965).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–O)

- Id: `phase:cu-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1357.77 K, x(O) 0–0.00019
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:fcc-a1)

Names (6): _corpus: _corpus:phase:cu-o:fcc-a1  
_tdb: _tdb:CuO-03Hal-LB.tdb:FCC_A1, tdb:CuO-05Sch.tdb:FCC_A1, tdb:CuO-14Mag.tdb:FCC_A1, tdb:CuO-92Bou.tdb:FCC_A1, tdb:CuO-94Hal.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): FCC_A1, type code %A, sha256 `5836249ea0179639…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : CU : VA% O : !
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): FCC_A1, type code %A, sha256 `a3dbcda00b2b888e…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : CU% O : VA : !
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): FCC_A1, type code %A, sha256 `c359243f81916348…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : CU : VA% O : !
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): FCC_A1, type code %A, sha256 `01c48e87b93fb30f…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : CU% O : VA : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): FCC_A1, type code %A, sha256 `59102ffec95449e3…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : CU% O : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_

## GAS (Cu–O)

- Id: `phase:cu-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1382.32–2500 K, x(O) 0.92505–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:gas)

Names (6): _corpus: _corpus:phase:cu-o:gas  
_tdb: _tdb:CuO-03Hal-LB.tdb:GAS, tdb:CuO-05Sch.tdb:GAS, tdb:CuO-14Mag.tdb:GAS, tdb:CuO-92Bou.tdb:GAS, tdb:CuO-94Hal.tdb:GAS  


### TDB models of GAS (5): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): GAS, type code %, sha256 `5836249ea0179639…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : CU CUO O O2 O3 : !
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): GAS, type code %, sha256 `a3dbcda00b2b888e…`

~~~~text
69: PHASE GAS:G % 1 1 !
70: CONST GAS:G : CU CUO O O2 O3 : !
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): GAS, type code %, sha256 `c359243f81916348…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : CU CU2 CUO O O2 O3 : !
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): GAS, type code %, sha256 `01c48e87b93fb30f…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : CU CU2 CUO O O2 O3 : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): GAS, type code %, sha256 `59102ffec95449e3…`

~~~~text
71: PHASE GAS:G % 1 1 !
72: CONST GAS:G : CU CUO O O2 O3 : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_

## HCP_A3 (Cu–O)

- Id: `phase:cu-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:hcp-a3)

Names (6): _corpus: _corpus:phase:cu-o:hcp-a3  
_tdb: _tdb:CuO-03Hal-LB.tdb:HCP_A3, tdb:CuO-05Sch.tdb:HCP_A3, tdb:CuO-14Mag.tdb:HCP_A3, tdb:CuO-92Bou.tdb:HCP_A3, tdb:CuO-94Hal.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): HCP_A3, type code %A, sha256 `5836249ea0179639…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : CU : VA : !
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): HCP_A3, type code %A, sha256 `a3dbcda00b2b888e…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : CU : VA : !
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): HCP_A3, type code %A, sha256 `c359243f81916348…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : CU : VA : !
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): HCP_A3, type code %A, sha256 `01c48e87b93fb30f…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : CU : VA : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): HCP_A3, type code %A, sha256 `59102ffec95449e3…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : CU : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_

## ION (Cu–O)

- Id: `phase:cu-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1342.77–2500 K, x(O) 0–0.39143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:ion)

Names (4): _corpus: _corpus:phase:cu-o:ion  
_tdb: _tdb:CuO-03Hal-LB.tdb:ION, tdb:CuO-05Sch.tdb:ION, tdb:CuO-94Hal.tdb:ION  


### TDB models of ION (3): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): ION, type code %, sha256 `5836249ea0179639…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : CU+1 CU+2 : O-2 VA : !
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): ION, type code %, sha256 `a3dbcda00b2b888e…`

~~~~text
38: PHASE ION:Y % 2 1 1 !
39: CONST ION:Y : CU+1 CU+2 CU+3 : O-2 VA : !
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): ION, type code %, sha256 `59102ffec95449e3…`

~~~~text
35: PHASE ION:Y % 2 1 1 !
36: CONST ION:Y : CU+1 CU+2 : O-2 VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase_

## LIQUID (Cu–O)

- Id: `phase:cu-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1342.77–2500 K, x(O) 0–0.33882
- Literature: 18 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:liquid)

Names (6): _corpus: _corpus:phase:cu-o:liquid  
_paper: _paper:10.1007/bf02649399:L2, paper:10.1007/bf02649399:liquid, paper:10.1361/154770305x74421:liquid  
_tdb: _tdb:CuO-14Mag.tdb:LIQUID, tdb:CuO-92Bou.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): LIQUID, type code %, sha256 `c359243f81916348…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : CU CU2O O : !
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): LIQUID, type code %, sha256 `01c48e87b93fb30f…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : CU CU2O O : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_
- [doi:10.1007/bf02649399](https://doi.org/10.1007/bf02649399) B. Hallstedt, D. Risold, L. J. Gauckler, Thermodynamic assessment of the copper-oxygen system, JPE 15, 483-499 (1994).  
_reports values for this phase_
- [doi:10.1361/154770305x74421](https://doi.org/10.1361/154770305x74421) L. Schramm, G. Behr, W. Löser, K. Wetzig, Thermodynamic Reassessment of the Cu-O Phase Diagram, Journal of Phase Equilibria &amp; Diffusion 26, 605-612 (2005).  
_reports values for this phase_
- [doi:10.1007/bf02654367](https://doi.org/10.1007/bf02654367) Rainer Schmid, A thermodynamic analysis of the Cu-O system with an associated solution model, Metall Trans B 14, 473-481 (1983).  
_cited as the source of values for this phase_
- [doi:10.1021/ja01438a009](https://doi.org/10.1021/ja01438a009) H. S. Roberts, F. Hastings Smyth, THE SYSTEM COPPER: CUPRIC OXIDE: OXYGEN., J. Am. Chem. Soc. 43, 1061-1079 (1921).  
_cited as the source of values for this phase_
- [doi:10.1098/rspa.1912.0107](https://doi.org/10.1098/rspa.1912.0107) R. E. Slade, F. D. Farrow, An investigation of the dissociation pressures and melting points of the system Copper-cuprous oxide, Proceedings of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character 87, 524-534 (1912).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1968-590711](https://doi.org/10.1515/ijmr-1968-590711) J. Gerlach, J. Osterwald, and W. Stichel,"Coulometric Determination of the Miscibility Gap between Liquid Copper and Copper(I) Oxide,"Z. Metallkd., 59(7), 576-579 (1968) in German.  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.42.5_527](https://doi.org/10.2320/jinstmet1952.42.5_527) Y. Kayahara, K. Ono, T. Oishi, and J. Moriyama, "Thermodynamic Study of the Liquid Cu-O System," Trans. Jpn. Inst. Met., 22(7), 493-500 (1981); Y. Kayahara, K. Ono, T. Oishi, and J. Moriyama, "Thermodynamic Study of the Liquid Cu-O System," J. Jpn. Inst. Met.,42(5), 527-533 (1978) in Japanese. 8lOts: S. Otsuka and Z. Kozuka, "Activities of Oxygen in Liquid Copper and Silver from Electrochemical Me  
_cited as the source of values for this phase_
- [doi:10.2320/matertrans1960.21.275](https://doi.org/10.2320/matertrans1960.21.275) Nobumasa Kemori, Iwao Katayama, Zensaku Kozuka, Thermodynamic Study of Oxygen in Liquid Copper, Trans. JIM 21, 275-284 (1980).  
_cited as the source of values for this phase_

## O2GAS (Cu–O)

- Id: `phase:cu-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–416 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-o:o2gas)

Names (6): _corpus: _corpus:phase:cu-o:o2gas  
_tdb: _tdb:CuO-03Hal-LB.tdb:O2GAS, tdb:CuO-05Sch.tdb:O2GAS, tdb:CuO-14Mag.tdb:O2GAS, tdb:CuO-92Bou.tdb:O2GAS, tdb:CuO-94Hal.tdb:O2GAS  


### TDB models of O2GAS (5): PHASE and CONSTITUENT statements as written

[CuO-03Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-03Hal-LB.tdb): O2GAS, type code %, sha256 `5836249ea0179639…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 :!
~~~~

[CuO-05Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-05Sch.tdb): O2GAS, type code %, sha256 `a3dbcda00b2b888e…`

~~~~text
66: PHASE O2GAS % 1 1 !
67: CONST O2GAS : O2 :!
~~~~

[CuO-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-14Mag.tdb): O2GAS, type code %, sha256 `c359243f81916348…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 :!
~~~~

[CuO-92Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-92Bou.tdb): O2GAS, type code %, sha256 `01c48e87b93fb30f…`

~~~~text
67: PHASE O2GAS % 1 1 !
68: CONST O2GAS : O2 :!
~~~~

[CuO-94Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuO-94Hal.tdb): O2GAS, type code %, sha256 `59102ffec95449e3…`

~~~~text
68: PHASE O2GAS % 1 1 !
69: CONST O2GAS : O2 :!
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02649399](https://doi.org/10.1007/BF02649399) B. Hallstedt, D. Risold and L.J. Gauckler, J. Phase Equilib., 15, 483-99(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00050-6](https://doi.org/10.1016/S0364-5916%2803%2900050-6) B. Hallstedt, L.J. Gauckler, Calphad, 27, 177-91(2003).  
_assessment that models this phase_
- [doi:10.1361/154770305X74421](https://doi.org/10.1361/154770305X74421) J. Phase Equilib. Diffus., 26, 605-12(2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830905](https://doi.org/10.1515/ijmr-1992-830905) Z. Metallkd., 83, 663-68(1992).  
_assessment that models this phase_

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
