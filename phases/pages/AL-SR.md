# Al–Sr phases

> Al–Sr system: 8 phases (tier A 4, tier C 3, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-SR.html · Markdown: https://data.orchid-project.org/phases/pages/AL-SR.md

8 phases (tier A 4, tier C 3, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-SR) · [full JSON](https://data.orchid-project.org/phases/systems/AL-SR.json) · [Al–Sr system page](https://data.orchid-project.org/systems/AL-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Sr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2SR](#phase-al-sr-al2sr); _phase:al-sr:al2sr_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1201.3 K, x(Sr) 0.33333–0.33333 | 26 | 4 |
| [AL3SR8](#phase-al-sr-al3sr8); _phase:al-sr:al3sr8_ | Ca8In3 · aP22 · P-1 (2) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 615.07–880.87 K, x(Sr) 0.72727–0.72727 | 0 | 3 |
| [AL4SR_D13](#phase-al-sr-al4sr-d13); _phase:al-sr:al4sr-d13_ | Al4Ba · D1_3 · tI10 · I4/mmm (139) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1333.21 K, x(Sr) 0.2–0.2 | 43 | 4 |
| [AL7SR8](#phase-al-sr-al7sr8); _phase:al-sr:al7sr8_ | Ba8Ga7 · cP60 · P2_13 (198) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–941.4 K, x(Sr) 0.53333–0.53333 | 21 | 4 |
| [BCC_A2](#phase-al-sr-bcc-a2); _phase:al-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300.01–2498.99 K, x(Sr) 0.99857–1 | 10 | 4 |
| [FCC_A1](#phase-al-sr-fcc-a1); _phase:al-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1044.99 K, x(Sr) 0–1 | 19 | 4 |
| [HCP_A3](#phase-al-sr-hcp-a3); _phase:al-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-al-sr-liquid); _phase:al-sr:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 851.91–2500 K, x(Sr) 0–1 | 61 | 4 |

## AL2SR (Al–Sr)

- Id: `phase:al-sr:al2sr`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.6667, Sr 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–1201.3 K, x(Sr) 0.33333–0.33333
- Literature: 26 values (26 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:al2sr)

Names (8): _corpus: _corpus:phase:al-sr:al2sr  
_paper: _paper:10.1016/j.actamat.2004.02.022:Al2Sr, paper:10.1016/j.jallcom.2014.05.018:SrAl2, paper:10.1016/s0925-8388(03)00046-x:SrAl2  
_tdb: _tdb:AlSr-03Wan-LB.tdb:AL2SR, tdb:AlSr-04Zho-RK.tdb:AL2SR, tdb:AlSr-04Zho-ass.tdb:AL2SR, tdb:AlSr-14Lia.tdb:AL2SR  


### TDB models of AL2SR (4): PHASE and CONSTITUENT statements as written

[AlSr-03Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-03Wan-LB.tdb): AL2SR, type code %, sha256 `2caf2ad6b04dbbc6…`

~~~~text
47: PHASE AL2SR % 2 2 1 !
48: CONST AL2SR : AL : SR : !
~~~~

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): AL2SR, type code %, sha256 `967e575d3bcd6d97…`

~~~~text
49: PHASE AL2SR % 2 2 1 !
50: CONST AL2SR : AL : SR : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): AL2SR, type code %, sha256 `1ee19ea419966799…`

~~~~text
57: PHASE AL2SR % 2 2 1 !
58: CONST AL2SR : AL : SR : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): AL2SR, type code %, sha256 `1fa45401a85a4430…`

~~~~text
48: PHASE AL2SR % 2 2 1 !
49: CONST AL2SR : AL : SR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(03)00046-X](https://doi.org/10.1016/S0925-8388%2803%2900046-X) C. Wang, Z. Jin, Y. Du, J. Alloys Compd., 358, 288-93(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02665326](https://doi.org/10.1007/bf02665326) B. Closset, H. Dugas, M. Pekguleryuz, J. E. Gruzleski, The aluminum-strontium phase diagram, Metall Trans A 17, 1250-1253 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_

## AL3SR8 (Al–Sr)

- Id: `phase:al-sr:al3sr8`; status `assigned`
- Structure: Ca8In3 · aP22 · P-1 (2); type `st:ca8in3-ap22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.2727, Sr 0.7273
- Stability: stable in 3 of 3 calculated diagram(s): 615.07–880.87 K, x(Sr) 0.72727–0.72727
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:al3sr8)

Names (4): _corpus: _corpus:phase:al-sr:al3sr8  
_tdb: _tdb:AlSr-04Zho-RK.tdb:AL3SR8, tdb:AlSr-04Zho-ass.tdb:AL3SR8, tdb:AlSr-14Lia.tdb:AL3SR8  


### TDB models of AL3SR8 (3): PHASE and CONSTITUENT statements as written

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): AL3SR8, type code %, sha256 `967e575d3bcd6d97…`

~~~~text
59: PHASE AL3SR8 % 2 3 8 !
60: CONST AL3SR8 : AL : SR : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): AL3SR8, type code %, sha256 `1ee19ea419966799…`

~~~~text
67: PHASE AL3SR8 % 2 3 8 !
68: CONST AL3SR8 : AL : SR : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): AL3SR8, type code %, sha256 `1fa45401a85a4430…`

~~~~text
58: PHASE AL3SR8 % 2 3 8 !
59: CONST AL3SR8 : AL : SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase_

## AL4SR_D13 (Al–Sr)

- Id: `phase:al-sr:al4sr-d13`; status `assigned`
- Structure: Al4Ba · D1_3 · tI10 · I4/mmm (139); type `st:d1-3-al4ba-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaect and oqmd-18718, space group 139
- Stoichiometry: Al 0.8000, Sr 0.2000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1333.21 K, x(Sr) 0.2–0.2
- Literature: 43 values (43 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:al4sr-d13)

Names (9): _corpus: _corpus:phase:al-sr:al4sr-d13  
_mp: _mp:mp-aaaaaect  
_oqmd: _oqmd:oqmd-18718  
_paper: _paper:10.1016/j.jallcom.2014.05.018:SrAl4, paper:10.1016/s0925-8388(03)00046-x:SrAl4  
_tdb: _tdb:AlSr-03Wan-LB.tdb:AL4SR_D13, tdb:AlSr-04Zho-RK.tdb:AL4SR_D13, tdb:AlSr-04Zho-ass.tdb:AL4SR_D13, tdb:AlSr-14Lia.tdb:AL4SR_D13  


### TDB models of AL4SR_D13 (4): PHASE and CONSTITUENT statements as written

[AlSr-03Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-03Wan-LB.tdb): AL4SR_D13, type code %, sha256 `2caf2ad6b04dbbc6…`

~~~~text
42: PHASE AL4SR_D13 % 2 4 1 !
43: CONST AL4SR_D13 : AL : SR : !
~~~~

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): AL4SR_D13, type code %, sha256 `967e575d3bcd6d97…`

~~~~text
44: PHASE AL4SR_D13 % 2 4 1 !
45: CONST AL4SR_D13 : AL : SR : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): AL4SR_D13, type code %, sha256 `1ee19ea419966799…`

~~~~text
52: PHASE AL4SR_D13 % 2 4 1 !
53: CONST AL4SR_D13 : AL : SR : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): AL4SR_D13, type code %, sha256 `1fa45401a85a4430…`

~~~~text
43: PHASE AL4SR_D13 % 2 4 1 !
44: CONST AL4SR_D13 : AL : SR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(03)00046-X](https://doi.org/10.1016/S0925-8388%2803%2900046-X) C. Wang, Z. Jin, Y. Du, J. Alloys Compd., 358, 288-93(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02665326](https://doi.org/10.1007/bf02665326) B. Closset, H. Dugas, M. Pekguleryuz, J. E. Gruzleski, The aluminum-strontium phase diagram, Metall Trans A 17, 1250-1253 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_

## AL7SR8 (Al–Sr)

- Id: `phase:al-sr:al7sr8`; status `assigned`
- Structure: Ba8Ga7 · cP60 · P2_13 (198); type `st:ba8ga7-cp60`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4667, Sr 0.5333
- Stability: stable in 4 of 4 calculated diagram(s): 300–941.4 K, x(Sr) 0.53333–0.53333
- Literature: 21 values (21 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:al7sr8)

Names (8): _corpus: _corpus:phase:al-sr:al7sr8  
_paper: _paper:10.1016/j.actamat.2004.02.022:Al7Sr8, paper:10.1016/j.jallcom.2014.05.018:Sr8Al7, paper:10.1016/s0925-8388(03)00046-x:Sr8Al7  
_tdb: _tdb:AlSr-03Wan-LB.tdb:AL7SR8, tdb:AlSr-04Zho-RK.tdb:AL7SR8, tdb:AlSr-04Zho-ass.tdb:AL7SR8, tdb:AlSr-14Lia.tdb:AL7SR8  


### TDB models of AL7SR8 (4): PHASE and CONSTITUENT statements as written

[AlSr-03Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-03Wan-LB.tdb): AL7SR8, type code %, sha256 `2caf2ad6b04dbbc6…`

~~~~text
52: PHASE AL7SR8 % 2 7 8 !
53: CONST AL7SR8 : AL : SR : !
~~~~

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): AL7SR8, type code %, sha256 `967e575d3bcd6d97…`

~~~~text
54: PHASE AL7SR8 % 2 7 8 !
55: CONST AL7SR8 : AL : SR : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): AL7SR8, type code %, sha256 `1ee19ea419966799…`

~~~~text
62: PHASE AL7SR8 % 2 7 8 !
63: CONST AL7SR8 : AL : SR : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): AL7SR8, type code %, sha256 `1fa45401a85a4430…`

~~~~text
53: PHASE AL7SR8 % 2 7 8 !
54: CONST AL7SR8 : AL : SR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S0925-8388(03)00046-X](https://doi.org/10.1016/S0925-8388%2803%2900046-X) C. Wang, Z. Jin, Y. Du, J. Alloys Compd., 358, 288-93(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02665326](https://doi.org/10.1007/bf02665326) B. Closset, H. Dugas, M. Pekguleryuz, J. E. Gruzleski, The aluminum-strontium phase diagram, Metall Trans A 17, 1250-1253 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_

## BCC_A2 (Al–Sr)

- Id: `phase:al-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300.01–2498.99 K, x(Sr) 0.99857–1
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:bcc-a2)

Names (7): _corpus: _corpus:phase:al-sr:bcc-a2  
_paper: _paper:10.1016/j.actamat.2004.02.022:Ni3Sn-type, paper:10.1016/s0925-8388(03)00046-x:(βSr)  
_tdb: _tdb:AlSr-03Wan-LB.tdb:BCC_A2, tdb:AlSr-04Zho-RK.tdb:BCC_A2, tdb:AlSr-04Zho-ass.tdb:BCC_A2, tdb:AlSr-14Lia.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[AlSr-03Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-03Wan-LB.tdb): BCC_A2, type code %B, sha256 `2caf2ad6b04dbbc6…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AL SR : VA : !
~~~~

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): BCC_A2, type code %B, sha256 `967e575d3bcd6d97…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL SR : VA : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): BCC_A2, type code %B, sha256 `1ee19ea419966799…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : AL SR : VA : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): BCC_A2, type code %B, sha256 `1fa45401a85a4430…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL SR : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S0925-8388(03)00046-X](https://doi.org/10.1016/S0925-8388%2803%2900046-X) C. Wang, Z. Jin, Y. Du, J. Alloys Compd., 358, 288-93(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase_
- [doi:10.1007/bf02665326](https://doi.org/10.1007/bf02665326) B. Closset, H. Dugas, M. Pekguleryuz, J. E. Gruzleski, The aluminum-strontium phase diagram, Metall Trans A 17, 1250-1253 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## FCC_A1 (Al–Sr)

- Id: `phase:al-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1044.99 K, x(Sr) 0–1
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:fcc-a1)

Names (8): _corpus: _corpus:phase:al-sr:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2014.05.018:(Al), paper:10.1016/s0925-8388(03)00046-x:(Al), paper:10.1016/s0925-8388(03)00046-x:(αSr)  
_tdb: _tdb:AlSr-03Wan-LB.tdb:FCC_A1, tdb:AlSr-04Zho-RK.tdb:FCC_A1, tdb:AlSr-04Zho-ass.tdb:FCC_A1, tdb:AlSr-14Lia.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[AlSr-03Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-03Wan-LB.tdb): FCC_A1, type code %A, sha256 `2caf2ad6b04dbbc6…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AL SR : VA : !
~~~~

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): FCC_A1, type code %A, sha256 `967e575d3bcd6d97…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL SR : VA : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): FCC_A1, type code %A, sha256 `1ee19ea419966799…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AL SR : VA : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): FCC_A1, type code %A, sha256 `1fa45401a85a4430…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL SR : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(03)00046-X](https://doi.org/10.1016/S0925-8388%2803%2900046-X) C. Wang, Z. Jin, Y. Du, J. Alloys Compd., 358, 288-93(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02665326](https://doi.org/10.1007/bf02665326) B. Closset, H. Dugas, M. Pekguleryuz, J. E. Gruzleski, The aluminum-strontium phase diagram, Metall Trans A 17, 1250-1253 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## HCP_A3 (Al–Sr)

- Id: `phase:al-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:hcp-a3)

Names (5): _corpus: _corpus:phase:al-sr:hcp-a3  
_tdb: _tdb:AlSr-03Wan-LB.tdb:HCP_A3, tdb:AlSr-04Zho-RK.tdb:HCP_A3, tdb:AlSr-04Zho-ass.tdb:HCP_A3, tdb:AlSr-14Lia.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[AlSr-03Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-03Wan-LB.tdb): HCP_A3, type code %A, sha256 `2caf2ad6b04dbbc6…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AL SR : VA : !
~~~~

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): HCP_A3, type code %A, sha256 `967e575d3bcd6d97…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL SR : VA : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): HCP_A3, type code %A, sha256 `1ee19ea419966799…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : AL SR : VA : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): HCP_A3, type code %A, sha256 `1fa45401a85a4430…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL SR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00046-X](https://doi.org/10.1016/S0925-8388%2803%2900046-X) C. Wang, Z. Jin, Y. Du, J. Alloys Compd., 358, 288-93(2003).  
_assessment that models this phase_

## LIQUID (Al–Sr)

- Id: `phase:al-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 851.91–2500 K, x(Sr) 0–1
- Literature: 61 values (61 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sr:liquid)

Names (7): _corpus: _corpus:phase:al-sr:liquid  
_paper: _paper:10.1016/j.jallcom.2014.05.018:L, paper:10.1016/s0925-8388(03)00046-x:L  
_tdb: _tdb:AlSr-03Wan-LB.tdb:LIQUID, tdb:AlSr-04Zho-RK.tdb:LIQUID, tdb:AlSr-04Zho-ass.tdb:LIQUID, tdb:AlSr-14Lia.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[AlSr-03Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-03Wan-LB.tdb): LIQUID, type code %, sha256 `2caf2ad6b04dbbc6…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AL SR : !
~~~~

[AlSr-04Zho-RK.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-RK.tdb): LIQUID, type code %, sha256 `967e575d3bcd6d97…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL SR : !
~~~~

[AlSr-04Zho-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-04Zho-ass.tdb): LIQUID, type code %, sha256 `1ee19ea419966799…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : AL AL2SR AL4SR SR : !
~~~~

[AlSr-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSr-14Lia.tdb): LIQUID, type code %, sha256 `1fa45401a85a4430…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL SR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S0925-8388(03)00046-X](https://doi.org/10.1016/S0925-8388%2803%2900046-X) C. Wang, Z. Jin, Y. Du, J. Alloys Compd., 358, 288-93(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.05.018](https://doi.org/10.1016/j.jallcom.2014.05.018) Song-Mao Liang, Michael Engstler, Veronika Groten, Jenifer Barrirero, Frank Mücklich, Andreas Bührig-Polaczek et al., Key experiments and thermodynamic revision of the binary Al–Sr system, Journal of Alloys and Compounds 610, 443-450 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2004.02.022](https://doi.org/10.1016/j.actamat.2004.02.022) Yu Zhong, C. Wolverton, Y. Austin Chang, Zi-Kui Liu, A combined CALPHAD/first-principles remodeling of the thermodynamics of Al–Sr: unsuspected ground state energies by “rounding up the (un)usual suspects”, Acta Materialia 52, 2739-2754 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02665326](https://doi.org/10.1007/bf02665326) B. Closset, H. Dugas, M. Pekguleryuz, J. E. Gruzleski, The aluminum-strontium phase diagram, Metall Trans A 17, 1250-1253 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
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
