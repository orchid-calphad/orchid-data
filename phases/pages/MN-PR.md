# Mn–Pr phases

> Mn–Pr system: 9 phases (tier A 8, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-PR.html · Markdown: https://data.orchid-project.org/phases/pages/MN-PR.md

9 phases (tier A 8, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-PR) · [full JSON](https://data.orchid-project.org/phases/systems/MN-PR.json) · [Mn–Pr system page](https://data.orchid-project.org/systems/MN-PR.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-PR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Pr system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-pr-bcc-a2); _phase:mn-pr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 937.89–1619 K, x(Pr) 0–1 | 4 | 2 |
| [CBCC_A12](#phase-mn-pr-cbcc-a12); _phase:mn-pr:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–980 K, x(Pr) 0–0 | 4 | 2 |
| [CUB_A13](#phase-mn-pr-cub-a13); _phase:mn-pr:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 980–1473.6 K, x(Pr) 0–0 | 2 | 2 |
| [DHCP](#phase-mn-pr-dhcp); _phase:mn-pr:dhcp_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 0 |
| [DHCP](#phase-mn-pr-dhcp-a3); _phase:mn-pr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1203.01 K, x(Pr) 0.98969–1 | 6 | 2 |
| [FCC_A1](#phase-mn-pr-fcc-a1); _phase:mn-pr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1359.85–1473.6 K, x(Pr) 0–2e-05 | 4 | 2 |
| [HCP_A3](#phase-mn-pr-hcp-a3); _phase:mn-pr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-mn-pr-liquid); _phase:mn-pr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 933.71–2500 K, x(Pr) 0–1 | 6 | 2 |
| [MN23PR6_D8A](#phase-mn-pr-mn23pr6-d8a); _phase:mn-pr:mn23pr6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 922.39–1065.06 K, x(Pr) 0.2069–0.2069 | 6 | 2 |

## BCC_A2 (Mn–Pr)

- Id: `phase:mn-pr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 937.89–1619 K, x(Pr) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:bcc-a2)

Names (5): _corpus: _corpus:phase:mn-pr:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.01.092:βPr, paper:10.1016/j.jallcom.2008.01.092:δMn  
_tdb: _tdb:MnPr-09Wan.tdb:BCC_A2, tdb:MnPr-24Ye.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): BCC_A2, type code %B, sha256 `afe8988cd246247a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MN% PR% : VA : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): BCC_A2, type code %B, sha256 `d5a488fd0fc8b6bc…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : MN% PR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## CBCC_A12 (Mn–Pr)

- Id: `phase:mn-pr:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–980 K, x(Pr) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:cbcc-a12)

Names (4): _corpus: _corpus:phase:mn-pr:cbcc-a12  
_paper: _paper:10.1016/j.jallcom.2008.01.092:αMn  
_tdb: _tdb:MnPr-09Wan.tdb:CBCC_A12, tdb:MnPr-24Ye.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): CBCC_A12, type code %A, sha256 `afe8988cd246247a…`

~~~~text
50: PHASE CBCC_A12 %A 2 1 1 !
51: CONST CBCC_A12 : MN : VA : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): CBCC_A12, type code %A, sha256 `d5a488fd0fc8b6bc…`

~~~~text
47: PHASE CBCC_A12 %A 2 1 1 !
48: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## CUB_A13 (Mn–Pr)

- Id: `phase:mn-pr:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 980–1473.6 K, x(Pr) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:cub-a13)

Names (4): _corpus: _corpus:phase:mn-pr:cub-a13  
_paper: _paper:10.1016/j.jallcom.2008.01.092:βMn  
_tdb: _tdb:MnPr-09Wan.tdb:CUB_A13, tdb:MnPr-24Ye.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): CUB_A13, type code %, sha256 `afe8988cd246247a…`

~~~~text
55: PHASE CUB_A13 % 2 1 1 !
56: CONST CUB_A13 : MN : VA : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): CUB_A13, type code %, sha256 `d5a488fd0fc8b6bc…`

~~~~text
52: PHASE CUB_A13 % 2 1 1 !
53: CONST CUB_A13 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## DHCP (Mn–Pr)

- Id: `phase:mn-pr:dhcp`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:dhcp)

Names (1): _corpus: _corpus:phase:mn-pr:dhcp  


## DHCP (Mn–Pr)

- Id: `phase:mn-pr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1203.01 K, x(Pr) 0.98969–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:dhcp-a3)

Names (4): _corpus: _corpus:phase:mn-pr:dhcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.01.092:αPr  
_tdb: _tdb:MnPr-09Wan.tdb:DHCP, tdb:MnPr-24Ye.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): DHCP, type code %, sha256 `afe8988cd246247a…`

~~~~text
45: PHASE DHCP % 1 1 !
46: CONST DHCP : MN PR% : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): DHCP, type code %, sha256 `d5a488fd0fc8b6bc…`

~~~~text
42: PHASE DHCP % 1 1 !
43: CONST DHCP : MN PR% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## FCC_A1 (Mn–Pr)

- Id: `phase:mn-pr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1359.85–1473.6 K, x(Pr) 0–2e-05
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:fcc-a1)

Names (4): _corpus: _corpus:phase:mn-pr:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2008.01.092:γMn  
_tdb: _tdb:MnPr-09Wan.tdb:FCC_A1, tdb:MnPr-24Ye.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): FCC_A1, type code %A, sha256 `afe8988cd246247a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MN% PR : VA : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): FCC_A1, type code %A, sha256 `d5a488fd0fc8b6bc…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : MN% PR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## HCP_A3 (Mn–Pr)

- Id: `phase:mn-pr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:hcp-a3)

Names (3): _corpus: _corpus:phase:mn-pr:hcp-a3  
_tdb: _tdb:MnPr-09Wan.tdb:HCP_A3, tdb:MnPr-24Ye.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): HCP_A3, type code %A, sha256 `afe8988cd246247a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MN : VA : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): HCP_A3, type code %A, sha256 `d5a488fd0fc8b6bc…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase_

## LIQUID (Mn–Pr)

- Id: `phase:mn-pr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 933.71–2500 K, x(Pr) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:liquid)

Names (4): _corpus: _corpus:phase:mn-pr:liquid  
_paper: _paper:10.1016/j.jallcom.2008.01.092:L  
_tdb: _tdb:MnPr-09Wan.tdb:LIQUID, tdb:MnPr-24Ye.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): LIQUID, type code %, sha256 `afe8988cd246247a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MN PR : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): LIQUID, type code %, sha256 `d5a488fd0fc8b6bc…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : MN PR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## MN23PR6_D8A (Mn–Pr)

- Id: `phase:mn-pr:mn23pr6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.7931, Pr 0.2069
- Stability: stable in 2 of 2 calculated diagram(s): 922.39–1065.06 K, x(Pr) 0.2069–0.2069
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pr:mn23pr6-d8a)

Names (4): _corpus: _corpus:phase:mn-pr:mn23pr6-d8a  
_paper: _paper:10.1016/j.jallcom.2008.01.092:Mn23Pr6  
_tdb: _tdb:MnPr-09Wan.tdb:MN23PR6_D8A, tdb:MnPr-24Ye.tdb:MN23PR6_D8A  


### TDB models of MN23PR6_D8A (2): PHASE and CONSTITUENT statements as written

[MnPr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-09Wan.tdb): MN23PR6_D8A, type code %, sha256 `afe8988cd246247a…`

~~~~text
60: PHASE MN23PR6_D8A % 2 23 6 !
61: CONST MN23PR6_D8A : MN : PR : !
~~~~

[MnPr-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPr-24Ye.tdb): MN23PR6_D8A, type code %, sha256 `d5a488fd0fc8b6bc…`

~~~~text
57: PHASE MN23PR6_D8A % 2 23 6 !
58: CONST MN23PR6_D8A : MN : PR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.01.092](https://doi.org/10.1016/j.jallcom.2008.01.092) C.P. Wang, Z. Lin, X.J. Liu, Thermodynamic assessments of the Dy–Mn and Mn–Pr systems, Journal of Alloys and Compounds 469, 123-128 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
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
