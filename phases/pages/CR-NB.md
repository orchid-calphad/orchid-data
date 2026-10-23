# Cr–Nb phases

> Cr–Nb system: 7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-NB.html · Markdown: https://data.orchid-project.org/phases/pages/CR-NB.md

7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-NB) · [full JSON](https://data.orchid-project.org/phases/systems/CR-NB.json) · [Cr–Nb system page](https://data.orchid-project.org/systems/CR-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Nb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-nb-bcc-a2); _phase:cr-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–4000 K, x(Nb) 0–1 | 10 | 7 |
| [C14_LAVES](#phase-cr-nb-c14-laves); _phase:cr-nb:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 1580–2009.25 K, x(Nb) 0.2919–0.34945 | 0 | 3 |
| [C15_LAVES](#phase-cr-nb-c15-laves); _phase:cr-nb:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2027.32 K, x(Nb) 0.29058–0.37475 | 27 | 7 |
| [C36_LAVES](#phase-cr-nb-c36-laves); _phase:cr-nb:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-cr-nb-fcc-a1); _phase:cr-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [HCP_A3](#phase-cr-nb-hcp-a3); _phase:cr-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-cr-nb-liquid); _phase:cr-nb:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1887.51–4000 K, x(Nb) 0–1 | 75 | 7 |

## BCC_A2 (Cr–Nb)

- Id: `phase:cr-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–4000 K, x(Nb) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-nb:bcc-a2)

Names (10): _corpus: _corpus:phase:cr-nb:bcc-a2  
_paper: _paper:10.1007/s11669-014-0313-y:(Cr), paper:10.1007/s11669-014-0313-y:(Nb)  
_tdb: _tdb:CrNb-09Pav.tdb:BCC_A2, tdb:CrNb-14Sch.tdb:BCC_A2, tdb:CrNb-15Lu.tdb:BCC_A2, tdb:CrNb-16Pen.tdb:BCC_A2, tdb:CrNb-17Laf.tdb:BCC_A2, tdb:CrNb-18Jia.tdb:BCC_A2, tdb:CrNb-93Cos-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[CrNb-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-09Pav.tdb): BCC_A2, type code %B, sha256 `73a70da7700dd8e2…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% NB% : VA : !
~~~~

[CrNb-14Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-14Sch.tdb): BCC_A2, type code %B, sha256 `b90da552cf891541…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR% NB% : VA : !
~~~~

[CrNb-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-15Lu.tdb): BCC_A2, type code %B, sha256 `b80dfce45f08a88c…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR% NB% : VA : !
~~~~

[CrNb-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-16Pen.tdb): BCC_A2, type code %B, sha256 `e22b1db4c4e94cba…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CR% NB% : VA : !
~~~~

[CrNb-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-17Laf.tdb): BCC_A2, type code %B, sha256 `22b23d29a6033b09…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% NB% : VA : !
~~~~

[CrNb-18Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-18Jia.tdb): BCC_A2, type code %B, sha256 `b31829d9849c2093…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CR% NB% : VA : !
~~~~

[CrNb-93Cos-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-93Cos-LB.tdb): BCC_A2, type code %B, sha256 `224f9134223c5058…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% NB% : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-014-0313-y](https://doi.org/10.1007/s11669-014-0313-y) Clemens Schmetterer, Alexandra Khvan, Aurélie Jacob, Bengt Hallstedt, Torsten Markus, A New Theoretical Study of the Cr-Nb System, J. Phase Equilib. Diffus. 35, 434-444 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90001-R](https://doi.org/10.1016/0364-5916%2893%2990001-R) J.G. Costa Neto, S.G. Fries, H.L. Lukas, S. Garna, G. Effenberg, Calphad, 17, 219-28(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.06.002](https://doi.org/10.1016/j.calphad.2015.06.002) H.-J. Lu, W.-B. Wang, N. Zou, J.-Y. Shen, X.-G. Lu, Y.-L. He, Calphad, 50, 134-43(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.06.001](https://doi.org/10.1016/j.calphad.2018.06.001) Y. Jiang, S. Zomorodpoosh, I. Roslyakova, L. Zhang, Calphad, 62, 109-18(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(61)90042-x](https://doi.org/10.1016/0022-5088%2861%2990042-x) H.J. Goldschmidt, J.A. Brand, The constitution of the chromium-niobium-molybdenum system, Journal of the Less Common Metals 3, 44-61 (1961).  
_cited as the source of values for this phase_

## C14_LAVES (Cr–Nb)

- Id: `phase:cr-nb:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrNb-09Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-15Lu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-93Cos-LB.tdb also describes the disordered state
- Stability: stable in 2 of 3 calculated diagram(s): 1580–2009.25 K, x(Nb) 0.2919–0.34945
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-nb:c14-laves)

Names (4): _corpus: _corpus:phase:cr-nb:c14-laves  
_tdb: _tdb:CrNb-09Pav.tdb:C14_LAVES, tdb:CrNb-15Lu.tdb:C14_LAVES, tdb:CrNb-93Cos-LB.tdb:C14_LAVES  


### TDB models of C14_LAVES (3): PHASE and CONSTITUENT statements as written

[CrNb-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-09Pav.tdb): C14_LAVES, type code %, sha256 `73a70da7700dd8e2…`

~~~~text
44: PHASE C14_LAVES % 2 2 1 !
45: CONST C14_LAVES : CR% NB : CR NB% : !
~~~~

[CrNb-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-15Lu.tdb): C14_LAVES, type code %, sha256 `b80dfce45f08a88c…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : CR NB : CR NB : !
~~~~

[CrNb-93Cos-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-93Cos-LB.tdb): C14_LAVES, type code %, sha256 `224f9134223c5058…`

~~~~text
44: PHASE C14_LAVES % 2 2 1 !
45: CONST C14_LAVES : CR% NB : CR NB% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90001-R](https://doi.org/10.1016/0364-5916%2893%2990001-R) J.G. Costa Neto, S.G. Fries, H.L. Lukas, S. Garna, G. Effenberg, Calphad, 17, 219-28(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.06.002](https://doi.org/10.1016/j.calphad.2015.06.002) H.-J. Lu, W.-B. Wang, N. Zou, J.-Y. Shen, X.-G. Lu, Y.-L. He, Calphad, 50, 134-43(2015).  
_assessment that models this phase_

## C15_LAVES (Cr–Nb)

- Id: `phase:cr-nb:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrNb-09Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-14Sch.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-15Lu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-16Pen.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-17Laf.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-18Jia.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNb-93Cos-LB.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 300–2027.32 K, x(Nb) 0.29058–0.37475
- Literature: 27 values (27 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-nb:c15-laves)

Names (12): _corpus: _corpus:phase:cr-nb:c15-laves  
_paper: _paper:10.1007/s11669-014-0313-y:(Cr2Nb), paper:10.1007/s11669-014-0313-y:C15 Cr2Nb, paper:10.1007/s11669-014-0313-y:C15 Cr2Nb (Cr-rich side), paper:10.1007/s11669-014-0313-y:Cr2Nb LT  
_tdb: _tdb:CrNb-09Pav.tdb:C15_LAVES, tdb:CrNb-14Sch.tdb:C15_LAVES, tdb:CrNb-15Lu.tdb:C15_LAVES, tdb:CrNb-16Pen.tdb:C15_LAVES, tdb:CrNb-17Laf.tdb:C15_LAVES, tdb:CrNb-18Jia.tdb:C15_LAVES, tdb:CrNb-93Cos-LB.tdb:C15_LAVES  


### TDB models of C15_LAVES (7): PHASE and CONSTITUENT statements as written

[CrNb-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-09Pav.tdb): C15_LAVES, type code %, sha256 `73a70da7700dd8e2…`

~~~~text
49: PHASE C15_LAVES % 2 2 1 !
50: CONST C15_LAVES : CR% NB : CR NB% : !
~~~~

[CrNb-14Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-14Sch.tdb): C15_LAVES, type code %, sha256 `b90da552cf891541…`

~~~~text
41: PHASE C15_LAVES % 2 2 1 !
42: CONST C15_LAVES : CR% NB : CR NB% : !
~~~~

[CrNb-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-15Lu.tdb): C15_LAVES, type code %, sha256 `b80dfce45f08a88c…`

~~~~text
47: PHASE C15_LAVES % 2 2 1 !
48: CONST C15_LAVES : CR% NB : CR NB% : !
~~~~

[CrNb-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-16Pen.tdb): C15_LAVES, type code %, sha256 `e22b1db4c4e94cba…`

~~~~text
46: PHASE C15_LAVES % 2 2 1 !
47: CONST C15_LAVES : CR% NB : CR NB% : !
~~~~

[CrNb-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-17Laf.tdb): C15_LAVES, type code %, sha256 `22b23d29a6033b09…`

~~~~text
40: PHASE C15_LAVES % 2 2 1 !
41: CONST C15_LAVES : CR% NB : CR NB% : !
~~~~

[CrNb-18Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-18Jia.tdb): C15_LAVES, type code %, sha256 `b31829d9849c2093…`

~~~~text
34: PHASE C15_LAVES % 2 2 1 !
35: CONST C15_LAVES : CR% NB : CR NB% : !
~~~~

[CrNb-93Cos-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-93Cos-LB.tdb): C15_LAVES, type code %, sha256 `224f9134223c5058…`

~~~~text
49: PHASE C15_LAVES % 2 2 1 !
50: CONST C15_LAVES : CR% NB : CR NB% : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1007/s11669-014-0313-y](https://doi.org/10.1007/s11669-014-0313-y) Clemens Schmetterer, Alexandra Khvan, Aurélie Jacob, Bengt Hallstedt, Torsten Markus, A New Theoretical Study of the Cr-Nb System, J. Phase Equilib. Diffus. 35, 434-444 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(93)90001-R](https://doi.org/10.1016/0364-5916%2893%2990001-R) J.G. Costa Neto, S.G. Fries, H.L. Lukas, S. Garna, G. Effenberg, Calphad, 17, 219-28(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.06.002](https://doi.org/10.1016/j.calphad.2015.06.002) H.-J. Lu, W.-B. Wang, N. Zou, J.-Y. Shen, X.-G. Lu, Y.-L. He, Calphad, 50, 134-43(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.06.001](https://doi.org/10.1016/j.calphad.2018.06.001) Y. Jiang, S. Zomorodpoosh, I. Roslyakova, L. Zhang, Calphad, 62, 109-18(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(61)90042-x](https://doi.org/10.1016/0022-5088%2861%2990042-x) H.J. Goldschmidt, J.A. Brand, The constitution of the chromium-niobium-molybdenum system, Journal of the Less Common Metals 3, 44-61 (1961).  
_cited as the source of values for this phase_
- [doi:10.1016/0921-5093(92)90420-6](https://doi.org/10.1016/0921-5093%2892%2990420-6) D.J. Thoma and J.H. Perepezko, An experimental Evaluation of the Phase Relationships and Solubilities in the Nb-Cr System, Mater. Sci. Eng., 1992, 156A, p 97-108  
_cited as the source of values for this phase_
- [doi:10.1039/tf9706601065](https://doi.org/10.1039/tf9706601065) J. F. Martin, Franz Müller, O. Kubaschewski, Thermodynamic properties of TaCr \<sub>2\</sub> and NbCr \<sub>2\</sub>, Trans. Faraday Soc. 66, 1065-1072 (1970).  
_cited as the source of values for this phase_

## C36_LAVES (Cr–Nb)

- Id: `phase:cr-nb:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrNb-15Lu.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-nb:c36-laves)

Names (2): _corpus: _corpus:phase:cr-nb:c36-laves  
_tdb: _tdb:CrNb-15Lu.tdb:C36_LAVES  


### TDB models of C36_LAVES (1): PHASE and CONSTITUENT statements as written

[CrNb-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-15Lu.tdb): C36_LAVES, type code %, sha256 `b80dfce45f08a88c…`

~~~~text
52: PHASE C36_LAVES % 2 2 1 !
53: CONST C36_LAVES : CR NB : CR NB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.06.002](https://doi.org/10.1016/j.calphad.2015.06.002) H.-J. Lu, W.-B. Wang, N. Zou, J.-Y. Shen, X.-G. Lu, Y.-L. He, Calphad, 50, 134-43(2015).  
_assessment that models this phase_

## FCC_A1 (Cr–Nb)

- Id: `phase:cr-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-nb:fcc-a1)

Names (7): _corpus: _corpus:phase:cr-nb:fcc-a1  
_tdb: _tdb:CrNb-09Pav.tdb:FCC_A1, tdb:CrNb-14Sch.tdb:FCC_A1, tdb:CrNb-15Lu.tdb:FCC_A1, tdb:CrNb-16Pen.tdb:FCC_A1, tdb:CrNb-17Laf.tdb:FCC_A1, tdb:CrNb-93Cos-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[CrNb-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-09Pav.tdb): FCC_A1, type code %A, sha256 `73a70da7700dd8e2…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR NB : VA : !
~~~~

[CrNb-14Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-14Sch.tdb): FCC_A1, type code %A, sha256 `b90da552cf891541…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR NB : VA : !
~~~~

[CrNb-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-15Lu.tdb): FCC_A1, type code %A, sha256 `b80dfce45f08a88c…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR NB : VA : !
~~~~

[CrNb-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-16Pen.tdb): FCC_A1, type code %A, sha256 `e22b1db4c4e94cba…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CR NB : VA : !
~~~~

[CrNb-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-17Laf.tdb): FCC_A1, type code %A, sha256 `22b23d29a6033b09…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR NB : VA : !
~~~~

[CrNb-93Cos-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-93Cos-LB.tdb): FCC_A1, type code %A, sha256 `224f9134223c5058…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR NB : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-014-0313-y](https://doi.org/10.1007/s11669-014-0313-y) Clemens Schmetterer, Alexandra Khvan, Aurélie Jacob, Bengt Hallstedt, Torsten Markus, A New Theoretical Study of the Cr-Nb System, J. Phase Equilib. Diffus. 35, 434-444 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(93)90001-R](https://doi.org/10.1016/0364-5916%2893%2990001-R) J.G. Costa Neto, S.G. Fries, H.L. Lukas, S. Garna, G. Effenberg, Calphad, 17, 219-28(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.06.002](https://doi.org/10.1016/j.calphad.2015.06.002) H.-J. Lu, W.-B. Wang, N. Zou, J.-Y. Shen, X.-G. Lu, Y.-L. He, Calphad, 50, 134-43(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_

## HCP_A3 (Cr–Nb)

- Id: `phase:cr-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-nb:hcp-a3)

Names (7): _corpus: _corpus:phase:cr-nb:hcp-a3  
_tdb: _tdb:CrNb-09Pav.tdb:HCP_A3, tdb:CrNb-14Sch.tdb:HCP_A3, tdb:CrNb-15Lu.tdb:HCP_A3, tdb:CrNb-16Pen.tdb:HCP_A3, tdb:CrNb-17Laf.tdb:HCP_A3, tdb:CrNb-93Cos-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[CrNb-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-09Pav.tdb): HCP_A3, type code %A, sha256 `73a70da7700dd8e2…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CR NB : VA : !
~~~~

[CrNb-14Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-14Sch.tdb): HCP_A3, type code %A, sha256 `b90da552cf891541…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR NB : VA : !
~~~~

[CrNb-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-15Lu.tdb): HCP_A3, type code %A, sha256 `b80dfce45f08a88c…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CR NB : VA : !
~~~~

[CrNb-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-16Pen.tdb): HCP_A3, type code %A, sha256 `e22b1db4c4e94cba…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CR NB : VA : !
~~~~

[CrNb-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-17Laf.tdb): HCP_A3, type code %A, sha256 `22b23d29a6033b09…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR NB : VA : !
~~~~

[CrNb-93Cos-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-93Cos-LB.tdb): HCP_A3, type code %A, sha256 `224f9134223c5058…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CR NB : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-014-0313-y](https://doi.org/10.1007/s11669-014-0313-y) Clemens Schmetterer, Alexandra Khvan, Aurélie Jacob, Bengt Hallstedt, Torsten Markus, A New Theoretical Study of the Cr-Nb System, J. Phase Equilib. Diffus. 35, 434-444 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(93)90001-R](https://doi.org/10.1016/0364-5916%2893%2990001-R) J.G. Costa Neto, S.G. Fries, H.L. Lukas, S. Garna, G. Effenberg, Calphad, 17, 219-28(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.06.002](https://doi.org/10.1016/j.calphad.2015.06.002) H.-J. Lu, W.-B. Wang, N. Zou, J.-Y. Shen, X.-G. Lu, Y.-L. He, Calphad, 50, 134-43(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_

## LIQUID (Cr–Nb)

- Id: `phase:cr-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1887.51–4000 K, x(Nb) 0–1
- Literature: 75 values (75 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-nb:liquid)

Names (11): _corpus: _corpus:phase:cr-nb:liquid  
_paper: _paper:10.1007/s11669-014-0313-y:L, paper:10.1007/s11669-014-0313-y:liquid, paper:10.1016/0364-5916(93)90001-r:liquid  
_tdb: _tdb:CrNb-09Pav.tdb:LIQUID, tdb:CrNb-14Sch.tdb:LIQUID, tdb:CrNb-15Lu.tdb:LIQUID, tdb:CrNb-16Pen.tdb:LIQUID, tdb:CrNb-17Laf.tdb:LIQUID, tdb:CrNb-18Jia.tdb:LIQUID, tdb:CrNb-93Cos-LB.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[CrNb-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-09Pav.tdb): LIQUID, type code %, sha256 `73a70da7700dd8e2…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR NB : !
~~~~

[CrNb-14Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-14Sch.tdb): LIQUID, type code %, sha256 `b90da552cf891541…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR NB : !
~~~~

[CrNb-15Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-15Lu.tdb): LIQUID, type code %, sha256 `b80dfce45f08a88c…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CR NB : !
~~~~

[CrNb-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-16Pen.tdb): LIQUID, type code %, sha256 `e22b1db4c4e94cba…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CR NB : !
~~~~

[CrNb-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-17Laf.tdb): LIQUID, type code %, sha256 `22b23d29a6033b09…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR NB : !
~~~~

[CrNb-18Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-18Jia.tdb): LIQUID, type code %, sha256 `b31829d9849c2093…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR NB : !
~~~~

[CrNb-93Cos-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNb-93Cos-LB.tdb): LIQUID, type code %, sha256 `224f9134223c5058…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR NB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-014-0313-y](https://doi.org/10.1007/s11669-014-0313-y) Clemens Schmetterer, Alexandra Khvan, Aurélie Jacob, Bengt Hallstedt, Torsten Markus, A New Theoretical Study of the Cr-Nb System, J. Phase Equilib. Diffus. 35, 434-444 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90001-R](https://doi.org/10.1016/0364-5916%2893%2990001-R) J.G. Costa Neto, S.G. Fries, H.L. Lukas, S. Garna, G. Effenberg, Calphad, 17, 219-28(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.06.002](https://doi.org/10.1016/j.calphad.2015.06.002) H.-J. Lu, W.-B. Wang, N. Zou, J.-Y. Shen, X.-G. Lu, Y.-L. He, Calphad, 50, 134-43(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.06.001](https://doi.org/10.1016/j.calphad.2018.06.001) Y. Jiang, S. Zomorodpoosh, I. Roslyakova, L. Zhang, Calphad, 62, 109-18(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(61)90042-x](https://doi.org/10.1016/0022-5088%2861%2990042-x) H.J. Goldschmidt, J.A. Brand, The constitution of the chromium-niobium-molybdenum system, Journal of the Less Common Metals 3, 44-61 (1961).  
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
