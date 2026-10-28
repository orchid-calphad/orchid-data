# Cu–Mn phases

> Cu–Mn system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-MN.html · Markdown: https://data.orchid-project.org/phases/pages/CU-MN.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-MN) · [full JSON](https://data.orchid-project.org/phases/systems/CU-MN.json) · [Cu–Mn system page](https://data.orchid-project.org/systems/CU-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Mn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-mn-bcc-a2); _phase:cu-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1368.13–2484 K, x(Mn) 0.84894–1 | 6 | 3 |
| [CBCC_A12](#phase-cu-mn-cbcc-a12); _phase:cu-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–993.32 K, x(Mn) 0.98548–1 | 11 | 3 |
| [CUB_A13](#phase-cu-mn-cub-a13); _phase:cu-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 976.54–1404.99 K, x(Mn) 0.84–1 | 7 | 3 |
| [FCC_A1](#phase-cu-mn-fcc-a1); _phase:cu-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1411.01 K, x(Mn) 0–1 | 27 | 3 |
| [HCP_A3](#phase-cu-mn-hcp-a3); _phase:cu-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-cu-mn-liquid); _phase:cu-mn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1143.67–2500 K, x(Mn) 0–1 | 12 | 3 |

## BCC_A2 (Cu–Mn)

- Id: `phase:cu-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1368.13–2484 K, x(Mn) 0.84894–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-mn:bcc-a2)

Names (6): _corpus: _corpus:phase:cu-mn:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2007.03.041:BCC_A2, paper:10.1016/s0364-5916(03)00035-x:bcc  
_tdb: _tdb:CuMn-03Mie-LB.tdb:BCC_A2, tdb:CuMn-07Wan.tdb:BCC_A2, tdb:CuMn-08He.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CuMn-03Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-03Mie-LB.tdb): BCC_A2, type code %B, sha256 `9a63b9bd45d2e41a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CU MN% : VA : !
~~~~

[CuMn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-07Wan.tdb): BCC_A2, type code %B, sha256 `75738f0838950981…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CU MN% : VA : !
~~~~

[CuMn-08He.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-08He.tdb): BCC_A2, type code %B, sha256 `fff8bb27170f55ce…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CU MN% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.041](https://doi.org/10.1016/j.jallcom.2007.03.041) Cuiyun He, Yong Du, Hai-Lin Chen, Shuhong Liu, Honghui Xu, Yifang Ouyang et al., Thermodynamic modeling of the Cu–Mn system supported by key experiments, Journal of Alloys and Compounds 457, 233-238 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(03)00035-X](https://doi.org/10.1016/S0364-5916%2803%2900035-X) J. Miettinen, Calphad, 27, 103-14(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.08.018](https://doi.org/10.1016/j.jallcom.2006.08.018) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessments of the Cu–Mn–X (X: Fe, Co) systems, Journal of Alloys and Compounds 438, 129-141 (2007).  
_assessment that models this phase_
- [doi:10.1098/rsta.1957.0004](https://doi.org/10.1098/rsta.1957.0004) A. Hellawell, William Hume-Rothery, The constitution of alloys of iron and manganese with transition elements of the first long period, Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249, 417-459 (1957).  
_cited as the source of values for this phase_

## CBCC_A12 (Cu–Mn)

- Id: `phase:cu-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–993.32 K, x(Mn) 0.98548–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-mn:cbcc-a12)

Names (6): _corpus: _corpus:phase:cu-mn:cbcc-a12  
_paper: _paper:10.1016/j.jallcom.2007.03.041:CBCC_A12, paper:10.1016/s0364-5916(03)00035-x:cbcc  
_tdb: _tdb:CuMn-03Mie-LB.tdb:CBCC_A12, tdb:CuMn-07Wan.tdb:CBCC_A12, tdb:CuMn-08He.tdb:CBCC_A12  


### TDB models of CBCC_A12 (3): PHASE and CONSTITUENT statements as written

[CuMn-03Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-03Mie-LB.tdb): CBCC_A12, type code %A, sha256 `9a63b9bd45d2e41a…`

~~~~text
40: PHASE CBCC_A12 %A 2 1 1 !
41: CONST CBCC_A12 : CU MN% : VA : !
~~~~

[CuMn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-07Wan.tdb): CBCC_A12, type code %A, sha256 `75738f0838950981…`

~~~~text
44: PHASE CBCC_A12 %A 2 1 1 !
45: CONST CBCC_A12 : CU MN% : VA : !
~~~~

[CuMn-08He.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-08He.tdb): CBCC_A12, type code %A, sha256 `fff8bb27170f55ce…`

~~~~text
46: PHASE CBCC_A12 %A 2 1 1 !
47: CONST CBCC_A12 : CU MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.041](https://doi.org/10.1016/j.jallcom.2007.03.041) Cuiyun He, Yong Du, Hai-Lin Chen, Shuhong Liu, Honghui Xu, Yifang Ouyang et al., Thermodynamic modeling of the Cu–Mn system supported by key experiments, Journal of Alloys and Compounds 457, 233-238 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(03)00035-X](https://doi.org/10.1016/S0364-5916%2803%2900035-X) J. Miettinen, Calphad, 27, 103-14(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.08.018](https://doi.org/10.1016/j.jallcom.2006.08.018) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessments of the Cu–Mn–X (X: Fe, Co) systems, Journal of Alloys and Compounds 438, 129-141 (2007).  
_assessment that models this phase_

## CUB_A13 (Cu–Mn)

- Id: `phase:cu-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 976.54–1404.99 K, x(Mn) 0.84–1
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-mn:cub-a13)

Names (6): _corpus: _corpus:phase:cu-mn:cub-a13  
_paper: _paper:10.1016/j.jallcom.2007.03.041:CUB_A13, paper:10.1016/s0364-5916(03)00035-x:cub  
_tdb: _tdb:CuMn-03Mie-LB.tdb:CUB_A13, tdb:CuMn-07Wan.tdb:CUB_A13, tdb:CuMn-08He.tdb:CUB_A13  


### TDB models of CUB_A13 (3): PHASE and CONSTITUENT statements as written

[CuMn-03Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-03Mie-LB.tdb): CUB_A13, type code %, sha256 `9a63b9bd45d2e41a…`

~~~~text
45: PHASE CUB_A13 % 2 1 1 !
46: CONST CUB_A13 : CU MN% : VA : !
~~~~

[CuMn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-07Wan.tdb): CUB_A13, type code %, sha256 `75738f0838950981…`

~~~~text
49: PHASE CUB_A13 % 2 1 1 !
50: CONST CUB_A13 : CU MN% : VA : !
~~~~

[CuMn-08He.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-08He.tdb): CUB_A13, type code %, sha256 `fff8bb27170f55ce…`

~~~~text
51: PHASE CUB_A13 % 2 1 1 !
52: CONST CUB_A13 : CU MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.041](https://doi.org/10.1016/j.jallcom.2007.03.041) Cuiyun He, Yong Du, Hai-Lin Chen, Shuhong Liu, Honghui Xu, Yifang Ouyang et al., Thermodynamic modeling of the Cu–Mn system supported by key experiments, Journal of Alloys and Compounds 457, 233-238 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(03)00035-X](https://doi.org/10.1016/S0364-5916%2803%2900035-X) J. Miettinen, Calphad, 27, 103-14(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.08.018](https://doi.org/10.1016/j.jallcom.2006.08.018) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessments of the Cu–Mn–X (X: Fe, Co) systems, Journal of Alloys and Compounds 438, 129-141 (2007).  
_assessment that models this phase_

## FCC_A1 (Cu–Mn)

- Id: `phase:cu-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1411.01 K, x(Mn) 0–1
- Literature: 27 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-mn:fcc-a1)

Names (7): _corpus: _corpus:phase:cu-mn:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.03.041:FCC_A1, paper:10.1016/s0364-5916(03)00035-x:Fcc, paper:10.1016/s0364-5916(03)00035-x:fcc  
_tdb: _tdb:CuMn-03Mie-LB.tdb:FCC_A1, tdb:CuMn-07Wan.tdb:FCC_A1, tdb:CuMn-08He.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CuMn-03Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-03Mie-LB.tdb): FCC_A1, type code %A, sha256 `9a63b9bd45d2e41a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CU% MN% : VA : !
~~~~

[CuMn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-07Wan.tdb): FCC_A1, type code %A, sha256 `75738f0838950981…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CU% MN% : VA : !
~~~~

[CuMn-08He.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-08He.tdb): FCC_A1, type code %A, sha256 `fff8bb27170f55ce…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CU% MN% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.041](https://doi.org/10.1016/j.jallcom.2007.03.041) Cuiyun He, Yong Du, Hai-Lin Chen, Shuhong Liu, Honghui Xu, Yifang Ouyang et al., Thermodynamic modeling of the Cu–Mn system supported by key experiments, Journal of Alloys and Compounds 457, 233-238 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(03)00035-X](https://doi.org/10.1016/S0364-5916%2803%2900035-X) J. Miettinen, Calphad, 27, 103-14(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.08.018](https://doi.org/10.1016/j.jallcom.2006.08.018) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessments of the Cu–Mn–X (X: Fe, Co) systems, Journal of Alloys and Compounds 438, 129-141 (2007).  
_assessment that models this phase_
- [doi:10.1098/rsta.1957.0004](https://doi.org/10.1098/rsta.1957.0004) A. Hellawell, William Hume-Rothery, The constitution of alloys of iron and manganese with transition elements of the first long period, Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249, 417-459 (1957).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Mn)

- Id: `phase:cu-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-mn:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-mn:hcp-a3  
_tdb: _tdb:CuMn-03Mie-LB.tdb:HCP_A3, tdb:CuMn-07Wan.tdb:HCP_A3, tdb:CuMn-08He.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CuMn-03Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-03Mie-LB.tdb): HCP_A3, type code %A, sha256 `9a63b9bd45d2e41a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CU MN : VA : !
~~~~

[CuMn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-07Wan.tdb): HCP_A3, type code %A, sha256 `75738f0838950981…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CU MN : VA : !
~~~~

[CuMn-08He.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-08He.tdb): HCP_A3, type code %A, sha256 `fff8bb27170f55ce…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CU MN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2006.08.018](https://doi.org/10.1016/j.jallcom.2006.08.018) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessments of the Cu–Mn–X (X: Fe, Co) systems, Journal of Alloys and Compounds 438, 129-141 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.03.041](https://doi.org/10.1016/j.jallcom.2007.03.041) Cuiyun He, Yong Du, Hai-Lin Chen, Shuhong Liu, Honghui Xu, Yifang Ouyang et al., Thermodynamic modeling of the Cu–Mn system supported by key experiments, Journal of Alloys and Compounds 457, 233-238 (2008).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(03)00035-X](https://doi.org/10.1016/S0364-5916%2803%2900035-X) J. Miettinen, Calphad, 27, 103-14(2003).  
_assessment that models this phase_

## LIQUID (Cu–Mn)

- Id: `phase:cu-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1143.67–2500 K, x(Mn) 0–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-mn:liquid)

Names (6): _corpus: _corpus:phase:cu-mn:liquid  
_paper: _paper:10.1016/j.jallcom.2007.03.041:Liquid, paper:10.1016/s0364-5916(03)00035-x:Liq  
_tdb: _tdb:CuMn-03Mie-LB.tdb:LIQUID, tdb:CuMn-07Wan.tdb:LIQUID, tdb:CuMn-08He.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CuMn-03Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-03Mie-LB.tdb): LIQUID, type code %, sha256 `9a63b9bd45d2e41a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CU MN : !
~~~~

[CuMn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-07Wan.tdb): LIQUID, type code %, sha256 `75738f0838950981…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CU MN : !
~~~~

[CuMn-08He.tdb](https://orchid-project.org/data/databases/sgte-binary/CuMn-08He.tdb): LIQUID, type code %, sha256 `fff8bb27170f55ce…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CU MN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.041](https://doi.org/10.1016/j.jallcom.2007.03.041) Cuiyun He, Yong Du, Hai-Lin Chen, Shuhong Liu, Honghui Xu, Yifang Ouyang et al., Thermodynamic modeling of the Cu–Mn system supported by key experiments, Journal of Alloys and Compounds 457, 233-238 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(03)00035-X](https://doi.org/10.1016/S0364-5916%2803%2900035-X) J. Miettinen, Calphad, 27, 103-14(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2006.08.018](https://doi.org/10.1016/j.jallcom.2006.08.018) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessments of the Cu–Mn–X (X: Fe, Co) systems, Journal of Alloys and Compounds 438, 129-141 (2007).  
_assessment that models this phase_
- [doi:10.1098/rsta.1957.0004](https://doi.org/10.1098/rsta.1957.0004) A. Hellawell, William Hume-Rothery, The constitution of alloys of iron and manganese with transition elements of the first long period, Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249, 417-459 (1957).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
