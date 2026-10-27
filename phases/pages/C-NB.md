# C–Nb phases

> C–Nb system: 6 phases (tier A 4, liquid 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-NB.html · Markdown: https://data.orchid-project.org/phases/pages/C-NB.md

6 phases (tier A 4, liquid 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-NB) · [full JSON](https://data.orchid-project.org/phases/systems/C-NB.json) · [C–Nb system page](https://data.orchid-project.org/systems/C-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Nb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-nb-a4-diamond); _phase:c-nb:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [GRAPHITE_A9](#phase-c-nb-a9-graphite); _phase:c-nb:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 5 |
| [BCC_A2](#phase-c-nb-bcc-a2); _phase:c-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 0–0.05461 | 6 | 5 |
| [FCC_A1](#phase-c-nb-fcc-a1); _phase:c-nb:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 5 of 5 calculated diagram(s): 300–3923.28 K, x(C) 0.29181–0.5 | 18 | 5 |
| [HCP_A3](#phase-c-nb-hcp-a3); _phase:c-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–3282.3 K, x(C) 0.28816–0.33333 | 13 | 5 |
| [LIQUID](#phase-c-nb-liquid); _phase:c-nb:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 2597.4–4000 K, x(C) 0–0.71742 | 24 | 5 |

## DIAMOND_A4 (C–Nb)

- Id: `phase:c-nb:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-nb:a4-diamond)

Names (6): _corpus: _corpus:phase:c-nb:a4-diamond  
_tdb: _tdb:NbC-01Lee.tdb:DIAMOND_A4, tdb:NbC-13Khv.tdb:DIAMOND_A4, tdb:NbC-16Pen.tdb:DIAMOND_A4, tdb:NbC-90Hua.tdb:DIAMOND_A4, tdb:NbC-97Hua-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[NbC-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-01Lee.tdb): DIAMOND_A4, type code %, sha256 `9f0b0d890e5bd1f1…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

[NbC-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-13Khv.tdb): DIAMOND_A4, type code %, sha256 `4ae1654829e38036…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : C : !
~~~~

[NbC-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-16Pen.tdb): DIAMOND_A4, type code %, sha256 `22d77b32d5bd2a4f…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : C : !
~~~~

[NbC-90Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-90Hua.tdb): DIAMOND_A4, type code %, sha256 `3b357fde12f03aea…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

[NbC-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-97Hua-LB.tdb): DIAMOND_A4, type code %, sha256 `81f536c9df24e381…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013), based on B.-J. Lee, Metall. Mater. Trans. A, 32A, 2423-39(2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.1179/mst.1990.6.8.687](https://doi.org/10.1179/mst.1990.6.8.687) Weiming Huang, Thermodynamic evaluation of Nb–C system, Materials Science and Technology 6, 687-694 (1990).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Nb)

- Id: `phase:c-nb:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-nb:a9-graphite)

Names (7): _corpus: _corpus:phase:c-nb:a9-graphite, corpus:phase:c-nb:graphite-a9  
_tdb: _tdb:NbC-01Lee.tdb:GRAPHITE_A9, tdb:NbC-13Khv.tdb:GRAPHITE_A9, tdb:NbC-16Pen.tdb:GRAPHITE_A9, tdb:NbC-90Hua.tdb:GRAPHITE_A9, tdb:NbC-97Hua-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (5): PHASE and CONSTITUENT statements as written

[NbC-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-01Lee.tdb): GRAPHITE_A9, type code %, sha256 `9f0b0d890e5bd1f1…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

[NbC-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-13Khv.tdb): GRAPHITE_A9, type code %, sha256 `4ae1654829e38036…`

~~~~text
52: PHASE GRAPHITE_A9 % 1 1 !
53: CONST GRAPHITE_A9 : C : !
~~~~

[NbC-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-16Pen.tdb): GRAPHITE_A9, type code %, sha256 `22d77b32d5bd2a4f…`

~~~~text
44: PHASE GRAPHITE_A9 % 1 1 !
45: CONST GRAPHITE_A9 : C : !
~~~~

[NbC-90Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-90Hua.tdb): GRAPHITE_A9, type code %, sha256 `3b357fde12f03aea…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

[NbC-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-97Hua-LB.tdb): GRAPHITE_A9, type code %, sha256 `81f536c9df24e381…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013), based on B.-J. Lee, Metall. Mater. Trans. A, 32A, 2423-39(2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.1179/mst.1990.6.8.687](https://doi.org/10.1179/mst.1990.6.8.687) Weiming Huang, Thermodynamic evaluation of Nb–C system, Materials Science and Technology 6, 687-694 (1990).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## BCC_A2 (C–Nb)

- Id: `phase:c-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 0–0.05461
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-nb:bcc-a2)

Names (7): _corpus: _corpus:phase:c-nb:bcc-a2  
_paper: _paper:10.1179/mst.1990.6.8.687:bcc  
_tdb: _tdb:NbC-01Lee.tdb:BCC_A2, tdb:NbC-13Khv.tdb:BCC_A2, tdb:NbC-16Pen.tdb:BCC_A2, tdb:NbC-90Hua.tdb:BCC_A2, tdb:NbC-97Hua-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[NbC-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-01Lee.tdb): BCC_A2, type code %B, sha256 `9f0b0d890e5bd1f1…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NB% : C VA% : !
~~~~

[NbC-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-13Khv.tdb): BCC_A2, type code %B, sha256 `4ae1654829e38036…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : NB% : C VA% : !
~~~~

[NbC-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-16Pen.tdb): BCC_A2, type code %B, sha256 `22d77b32d5bd2a4f…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : NB% : C VA% : !
~~~~

[NbC-90Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-90Hua.tdb): BCC_A2, type code %B, sha256 `3b357fde12f03aea…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NB% : C VA% : !
~~~~

[NbC-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-97Hua-LB.tdb): BCC_A2, type code %B, sha256 `81f536c9df24e381…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NB% : C VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1179/mst.1990.6.8.687](https://doi.org/10.1179/mst.1990.6.8.687) Weiming Huang, Thermodynamic evaluation of Nb–C system, Materials Science and Technology 6, 687-694 (1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013), based on B.-J. Lee, Metall. Mater. Trans. A, 32A, 2423-39(2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## FCC_A1 (C–Nb)

- Id: `phase:c-nb:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–3923.28 K, x(C) 0.29181–0.5
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-nb:fcc-a1)

Names (7): _corpus: _corpus:phase:c-nb:fcc-a1  
_paper: _paper:10.1179/mst.1990.6.8.687:NbC  
_tdb: _tdb:NbC-01Lee.tdb:FCC_A1, tdb:NbC-13Khv.tdb:FCC_A1, tdb:NbC-16Pen.tdb:FCC_A1, tdb:NbC-90Hua.tdb:FCC_A1, tdb:NbC-97Hua-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[NbC-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-01Lee.tdb): FCC_A1, type code %A, sha256 `9f0b0d890e5bd1f1…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NB : C VA% : !
~~~~

[NbC-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-13Khv.tdb): FCC_A1, type code %A, sha256 `4ae1654829e38036…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : NB : C VA% : !
~~~~

[NbC-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-16Pen.tdb): FCC_A1, type code %A, sha256 `22d77b32d5bd2a4f…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : NB : C VA% : !
~~~~

[NbC-90Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-90Hua.tdb): FCC_A1, type code %A, sha256 `3b357fde12f03aea…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NB : C VA% : !
~~~~

[NbC-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-97Hua-LB.tdb): FCC_A1, type code %A, sha256 `81f536c9df24e381…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NB : C VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1179/mst.1990.6.8.687](https://doi.org/10.1179/mst.1990.6.8.687) Weiming Huang, Thermodynamic evaluation of Nb–C system, Materials Science and Technology 6, 687-694 (1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013), based on B.-J. Lee, Metall. Mater. Trans. A, 32A, 2423-39(2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## HCP_A3 (C–Nb)

- Id: `phase:c-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–3282.3 K, x(C) 0.28816–0.33333
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-nb:hcp-a3)

Names (7): _corpus: _corpus:phase:c-nb:hcp-a3  
_paper: _paper:10.1179/mst.1990.6.8.687:Nb2C  
_tdb: _tdb:NbC-01Lee.tdb:HCP_A3, tdb:NbC-13Khv.tdb:HCP_A3, tdb:NbC-16Pen.tdb:HCP_A3, tdb:NbC-90Hua.tdb:HCP_A3, tdb:NbC-97Hua-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[NbC-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-01Lee.tdb): HCP_A3, type code %A, sha256 `9f0b0d890e5bd1f1…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NB : C VA% : !
~~~~

[NbC-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-13Khv.tdb): HCP_A3, type code %A, sha256 `4ae1654829e38036…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : NB : C VA% : !
~~~~

[NbC-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-16Pen.tdb): HCP_A3, type code %A, sha256 `22d77b32d5bd2a4f…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : NB : C VA% : !
~~~~

[NbC-90Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-90Hua.tdb): HCP_A3, type code %A, sha256 `3b357fde12f03aea…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NB : C VA% : !
~~~~

[NbC-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-97Hua-LB.tdb): HCP_A3, type code %A, sha256 `81f536c9df24e381…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NB : C VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1179/mst.1990.6.8.687](https://doi.org/10.1179/mst.1990.6.8.687) Weiming Huang, Thermodynamic evaluation of Nb–C system, Materials Science and Technology 6, 687-694 (1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013), based on B.-J. Lee, Metall. Mater. Trans. A, 32A, 2423-39(2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## LIQUID (C–Nb)

- Id: `phase:c-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 2597.4–4000 K, x(C) 0–0.71742
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-nb:liquid)

Names (7): _corpus: _corpus:phase:c-nb:liquid  
_paper: _paper:10.1179/mst.1990.6.8.687:Liquid  
_tdb: _tdb:NbC-01Lee.tdb:LIQUID, tdb:NbC-13Khv.tdb:LIQUID, tdb:NbC-16Pen.tdb:LIQUID, tdb:NbC-90Hua.tdb:LIQUID, tdb:NbC-97Hua-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[NbC-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-01Lee.tdb): LIQUID, type code %, sha256 `9f0b0d890e5bd1f1…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C NB : !
~~~~

[NbC-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-13Khv.tdb): LIQUID, type code %, sha256 `4ae1654829e38036…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : C NB : !
~~~~

[NbC-16Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-16Pen.tdb): LIQUID, type code %, sha256 `22d77b32d5bd2a4f…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : C NB : !
~~~~

[NbC-90Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-90Hua.tdb): LIQUID, type code %, sha256 `3b357fde12f03aea…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C NB : !
~~~~

[NbC-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbC-97Hua-LB.tdb): LIQUID, type code %, sha256 `81f536c9df24e381…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C NB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1179/mst.1990.6.8.687](https://doi.org/10.1179/mst.1990.6.8.687) Weiming Huang, Thermodynamic evaluation of Nb–C system, Materials Science and Technology 6, 687-694 (1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013), based on B.-J. Lee, Metall. Mater. Trans. A, 32A, 2423-39(2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.004](https://doi.org/10.1016/j.calphad.2016.02.004) Y. Peng, P. Zhou, M. Bu, W. Zhang, Y. Du, Calphad, 53, 10-19(2016).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

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
