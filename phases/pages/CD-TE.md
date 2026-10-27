# Cd–Te phases

> Cd–Te system: 7 phases (tier A 5, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-TE.html · Markdown: https://data.orchid-project.org/phases/pages/CD-TE.md

7 phases (tier A 5, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-TE) · [full JSON](https://data.orchid-project.org/phases/systems/CD-TE.json) · [Cd–Te system page](https://data.orchid-project.org/systems/CD-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Te system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-cd-te-a8-hexagonal); _phase:cd-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 3 | 3 |
| [ZINCBLENDE_B3](#phase-cd-te-b3-zincblende); _phase:cd-te:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1371.96 K, x(Te) 0.5–0.5 | 14 | 3 |
| [BCC_A2](#phase-cd-te-bcc-a2); _phase:cd-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-cd-te-fcc-a1); _phase:cd-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-cd-te-gas); _phase:cd-te:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 1039.68–2500 K, x(Te) 0–1 | 0 | 3 |
| [HCP_A3](#phase-cd-te-hcp-a3); _phase:cd-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–594.22 K, x(Te) 0–0 | 2 | 3 |
| [LIQUID](#phase-cd-te-liquid); _phase:cd-te:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 594.13–1552.49 K, x(Te) 0–1 | 14 | 3 |

## HEXAGONAL_A8 (Cd–Te)

- Id: `phase:cd-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-te:a8-hexagonal)

Names (6): _corpus: _corpus:phase:cd-te:a8-hexagonal, corpus:phase:cd-te:hexagonal-a8  
_paper: _paper:10.1007/s11664-009-0875-3:hex  
_tdb: _tdb:CdTe-00Yam-LB.tdb:HEXAGONAL_A8, tdb:CdTe-09Liu.tdb:HEXAGONAL_A8, tdb:CdTe-95Yan.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (3): PHASE and CONSTITUENT statements as written

[CdTe-00Yam-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-00Yam-LB.tdb): HEXAGONAL_A8, type code %, sha256 `378f97637cad8435…`

~~~~text
57: PHASE HEXAGONAL_A8 % 1 1 !
58: CONST HEXAGONAL_A8 : TE : !
~~~~

[CdTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-09Liu.tdb): HEXAGONAL_A8, type code %, sha256 `0716dba9e0a29626…`

~~~~text
51: PHASE HEXAGONAL_A8 % 1 1 !
52: CONST HEXAGONAL_A8 : TE : !
~~~~

[CdTe-95Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-95Yan.tdb): HEXAGONAL_A8, type code %, sha256 `52f50c87a9d21165…`

~~~~text
52: PHASE HEXAGONAL_A8 % 1 1 !
53: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.2320/matertrans1989.41.790](https://doi.org/10.2320/matertrans1989.41.790) K. Yamaguchi, K. Hongo, K. Hack, I. Hurtado, D. Neuschuetz, Mater. Trans. JIM, 41, 790-98(2000).  
_assessment that models this phase_
- [doi:10.1002/zaac.19100690102](https://doi.org/10.1002/zaac.19100690102) Matsusuke Kobayashi, Über die Legierungen des Tellurs mit Cadmium und Zinn, Z. Anorg. Chem. 69, 1-9 (1911).  
_cited as the source of values for this phase_

## ZINCBLENDE_B3 (Cd–Te)

- Id: `phase:cd-te:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.5000, Te 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1371.96 K, x(Te) 0.5–0.5
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-te:b3-zincblende)

Names (6): _corpus: _corpus:phase:cd-te:b3-zincblende, corpus:phase:cd-te:zincblende-b3  
_paper: _paper:10.1007/s11664-009-0875-3:CdTe  
_tdb: _tdb:CdTe-00Yam-LB.tdb:ZINCBLENDE_B3, tdb:CdTe-09Liu.tdb:ZINCBLENDE_B3, tdb:CdTe-95Yan.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (3): PHASE and CONSTITUENT statements as written

[CdTe-00Yam-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-00Yam-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `378f97637cad8435…`

~~~~text
62: PHASE ZINCBLENDE_B3 % 2 1 1 !
63: CONST ZINCBLENDE_B3 : CD : TE : !
~~~~

[CdTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-09Liu.tdb): ZINCBLENDE_B3, type code %, sha256 `0716dba9e0a29626…`

~~~~text
56: PHASE ZINCBLENDE_B3 % 2 1 1 !
57: CONST ZINCBLENDE_B3 : CD : TE : !
~~~~

[CdTe-95Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-95Yan.tdb): ZINCBLENDE_B3, type code %, sha256 `52f50c87a9d21165…`

~~~~text
57: PHASE ZINCBLENDE_B3 % 2 1 1 !
58: CONST ZINCBLENDE_B3 : CD : TE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.2320/matertrans1989.41.790](https://doi.org/10.2320/matertrans1989.41.790) K. Yamaguchi, K. Hongo, K. Hack, I. Hurtado, D. Neuschuetz, Mater. Trans. JIM, 41, 790-98(2000).  
_assessment that models this phase_
- [doi:10.1002/zaac.19100690102](https://doi.org/10.1002/zaac.19100690102) Matsusuke Kobayashi, Über die Legierungen des Tellurs mit Cadmium und Zinn, Z. Anorg. Chem. 69, 1-9 (1911).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3697(59)90110-6](https://doi.org/10.1016/0022-3697%2859%2990110-6) W.D. Lawson, S. Nielsen, E.H. Putley, A.S. Young, Preparation and properties of HgTe and mixed crystals of HgTe-CdTe, Journal of Physics and Chemistry of Solids 9, 325-329 (1959).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3697(62)90151-8](https://doi.org/10.1016/0022-3697%2862%2990151-8) M.R. Lorenz, Phase equilibria in the system Cd—Te∗, Journal of Physics and Chemistry of Solids 23, 939-947 (1962).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2407297](https://doi.org/10.1149/1.2407297) J. Steininger, A.J. Strauss, and R.F. Brebrick, J. Appl. Phys. 117, 1305 (1970).  
_cited as the source of values for this phase_

## BCC_A2 (Cd–Te)

- Id: `phase:cd-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-te:bcc-a2)

Names (4): _corpus: _corpus:phase:cd-te:bcc-a2  
_tdb: _tdb:CdTe-00Yam-LB.tdb:BCC_A2, tdb:CdTe-09Liu.tdb:BCC_A2, tdb:CdTe-95Yan.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CdTe-00Yam-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-00Yam-LB.tdb): BCC_A2, type code %B, sha256 `378f97637cad8435…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : CD : VA : !
~~~~

[CdTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-09Liu.tdb): BCC_A2, type code %B, sha256 `0716dba9e0a29626…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CD : VA : !
~~~~

[CdTe-95Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-95Yan.tdb): BCC_A2, type code %B, sha256 `52f50c87a9d21165…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CD : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.2320/matertrans1989.41.790](https://doi.org/10.2320/matertrans1989.41.790) K. Yamaguchi, K. Hongo, K. Hack, I. Hurtado, D. Neuschuetz, Mater. Trans. JIM, 41, 790-98(2000).  
_assessment that models this phase_

## FCC_A1 (Cd–Te)

- Id: `phase:cd-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-te:fcc-a1)

Names (4): _corpus: _corpus:phase:cd-te:fcc-a1  
_tdb: _tdb:CdTe-00Yam-LB.tdb:FCC_A1, tdb:CdTe-09Liu.tdb:FCC_A1, tdb:CdTe-95Yan.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CdTe-00Yam-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-00Yam-LB.tdb): FCC_A1, type code %A, sha256 `378f97637cad8435…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : CD : VA : !
~~~~

[CdTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-09Liu.tdb): FCC_A1, type code %A, sha256 `0716dba9e0a29626…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CD : VA : !
~~~~

[CdTe-95Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-95Yan.tdb): FCC_A1, type code %A, sha256 `52f50c87a9d21165…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CD : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.2320/matertrans1989.41.790](https://doi.org/10.2320/matertrans1989.41.790) K. Yamaguchi, K. Hongo, K. Hack, I. Hurtado, D. Neuschuetz, Mater. Trans. JIM, 41, 790-98(2000).  
_assessment that models this phase_

## GAS (Cd–Te)

- Id: `phase:cd-te:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1039.68–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-te:gas)

Names (4): _corpus: _corpus:phase:cd-te:gas  
_tdb: _tdb:CdTe-00Yam-LB.tdb:GAS, tdb:CdTe-09Liu.tdb:GAS, tdb:CdTe-95Yan.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[CdTe-00Yam-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-00Yam-LB.tdb): GAS, type code %, sha256 `378f97637cad8435…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : CD TE TE2 TE3 TE4 TE5 TE6 TE7 : !
~~~~

[CdTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-09Liu.tdb): GAS, type code %, sha256 `0716dba9e0a29626…`

~~~~text
59: PHASE GAS:G % 1 1 !
60: CONST GAS:G : CD TE TE2 TE3 TE4 TE5 TE6 TE7 : !
~~~~

[CdTe-95Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-95Yan.tdb): GAS, type code %, sha256 `52f50c87a9d21165…`

~~~~text
60: PHASE GAS:G % 1 1 !
61: CONST GAS:G : CD TE TE2 TE3 TE4 TE5 TE6 TE7 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.2320/matertrans1989.41.790](https://doi.org/10.2320/matertrans1989.41.790) K. Yamaguchi, K. Hongo, K. Hack, I. Hurtado, D. Neuschuetz, Mater. Trans. JIM, 41, 790-98(2000).  
_assessment that models this phase_

## HCP_A3 (Cd–Te)

- Id: `phase:cd-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–594.22 K, x(Te) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-te:hcp-a3)

Names (5): _corpus: _corpus:phase:cd-te:hcp-a3  
_paper: _paper:10.1007/s11664-009-0875-3:Cd  
_tdb: _tdb:CdTe-00Yam-LB.tdb:HCP_A3, tdb:CdTe-09Liu.tdb:HCP_A3, tdb:CdTe-95Yan.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CdTe-00Yam-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-00Yam-LB.tdb): HCP_A3, type code %A, sha256 `378f97637cad8435…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : CD% : VA : !
~~~~

[CdTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-09Liu.tdb): HCP_A3, type code %A, sha256 `0716dba9e0a29626…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CD% : VA : !
~~~~

[CdTe-95Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-95Yan.tdb): HCP_A3, type code %A, sha256 `52f50c87a9d21165…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CD% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.2320/matertrans1989.41.790](https://doi.org/10.2320/matertrans1989.41.790) K. Yamaguchi, K. Hongo, K. Hack, I. Hurtado, D. Neuschuetz, Mater. Trans. JIM, 41, 790-98(2000).  
_assessment that models this phase_
- [doi:10.1002/zaac.19100690102](https://doi.org/10.1002/zaac.19100690102) Matsusuke Kobayashi, Über die Legierungen des Tellurs mit Cadmium und Zinn, Z. Anorg. Chem. 69, 1-9 (1911).  
_cited as the source of values for this phase_

## LIQUID (Cd–Te)

- Id: `phase:cd-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 594.13–1552.49 K, x(Te) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-te:liquid)

Names (5): _corpus: _corpus:phase:cd-te:liquid  
_paper: _paper:10.1007/s11664-009-0875-3:liq  
_tdb: _tdb:CdTe-00Yam-LB.tdb:LIQUID, tdb:CdTe-09Liu.tdb:LIQUID, tdb:CdTe-95Yan.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CdTe-00Yam-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-00Yam-LB.tdb): LIQUID, type code %, sha256 `378f97637cad8435…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : CD CDTE TE : !
~~~~

[CdTe-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-09Liu.tdb): LIQUID, type code %, sha256 `0716dba9e0a29626…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CD CDTE TE : !
~~~~

[CdTe-95Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CdTe-95Yan.tdb): LIQUID, type code %, sha256 `52f50c87a9d21165…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CD CDTE TE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.2320/matertrans1989.41.790](https://doi.org/10.2320/matertrans1989.41.790) K. Yamaguchi, K. Hongo, K. Hack, I. Hurtado, D. Neuschuetz, Mater. Trans. JIM, 41, 790-98(2000).  
_assessment that models this phase_
- [doi:10.1002/zaac.19100690102](https://doi.org/10.1002/zaac.19100690102) Matsusuke Kobayashi, Über die Legierungen des Tellurs mit Cadmium und Zinn, Z. Anorg. Chem. 69, 1-9 (1911).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3697(59)90110-6](https://doi.org/10.1016/0022-3697%2859%2990110-6) W.D. Lawson, S. Nielsen, E.H. Putley, A.S. Young, Preparation and properties of HgTe and mixed crystals of HgTe-CdTe, Journal of Physics and Chemistry of Solids 9, 325-329 (1959).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3697(62)90151-8](https://doi.org/10.1016/0022-3697%2862%2990151-8) M.R. Lorenz, Phase equilibria in the system Cd—Te∗, Journal of Physics and Chemistry of Solids 23, 939-947 (1962).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2407297](https://doi.org/10.1149/1.2407297) J. Steininger, A.J. Strauss, and R.F. Brebrick, J. Appl. Phys. 117, 1305 (1970).  
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
