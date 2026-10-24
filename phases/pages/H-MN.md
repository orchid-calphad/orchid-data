# H–Mn phases

> H–Mn system: 8 phases (tier A 5, liquid 1, gas 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-MN.html · Markdown: https://data.orchid-project.org/phases/pages/H-MN.md

8 phases (tier A 5, liquid 1, gas 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-MN) · [full JSON](https://data.orchid-project.org/phases/systems/H-MN.json) · [H–Mn system page](https://data.orchid-project.org/systems/H-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Mn system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-mn-bcc-a2); _phase:h-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1410.37–2334 K, x(H) 0–0.00203 | 4 | 2 |
| [CBCC_A12](#phase-h-mn-cbcc-a12); _phase:h-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–980 K, x(H) 0–0.00076 | 2 | 2 |
| [CUB_A13](#phase-h-mn-cub-a13); _phase:h-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 977.19–1359.99 K, x(H) 0–0.00164 | 4 | 2 |
| [FCC_A1](#phase-h-mn-fcc-a1); _phase:h-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1358.05–1415.18 K, x(H) 0–0.002 | 4 | 2 |
| [GAS](#phase-h-mn-gas); _phase:h-mn:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1 | 6 | 2 |
| [H2GAS](#phase-h-mn-h2gas); _phase:h-mn:h2gas_ | gas | gas | stable in 1 of 2 calculated diagram(s): 300.44–771.69 K, x(H) 1–1 | 0 | 2 |
| [HCP_A3](#phase-h-mn-hcp-a3); _phase:h-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 300–396.69 K, x(H) 0.47216–0.49531 | 0 | 2 |
| [LIQUID](#phase-h-mn-liquid); _phase:h-mn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1515.26–2339.53 K, x(H) 0–0.00454 | 2 | 2 |

## BCC_A2 (H–Mn)

- Id: `phase:h-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1410.37–2334 K, x(H) 0–0.00203
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:bcc-a2)

Names (4): _corpus: _corpus:phase:h-mn:bcc-a2  
_paper: _paper:10.1007/s11669-018-0622-7:(δMn)  
_tdb: _tdb:MnH-11Lob.tdb:BCC_A2, tdb:MnH-18Lia.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): BCC_A2, type code %B, sha256 `d20c86d703fa6e37…`

~~~~text
38: PHASE BCC_A2 %B 2 1 1 !
39: CONST BCC_A2 : MN : H VA% : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): BCC_A2, type code %B, sha256 `ee68c7da6eef802b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : MN : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
_assessment that models this phase_

## CBCC_A12 (H–Mn)

- Id: `phase:h-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–980 K, x(H) 0–0.00076
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:cbcc-a12)

Names (4): _corpus: _corpus:phase:h-mn:cbcc-a12  
_paper: _paper:10.1007/s11669-018-0622-7:(αMn)  
_tdb: _tdb:MnH-11Lob.tdb:CBCC_A12, tdb:MnH-18Lia.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): CBCC_A12, type code %, sha256 `d20c86d703fa6e37…`

~~~~text
48: PHASE CBCC_A12 % 2 1 1 !
49: CONST CBCC_A12 : MN : H VA% : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): CBCC_A12, type code %, sha256 `ee68c7da6eef802b…`

~~~~text
50: PHASE CBCC_A12 % 2 1 1 !
51: CONST CBCC_A12 : MN : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
_assessment that models this phase_

## CUB_A13 (H–Mn)

- Id: `phase:h-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 977.19–1359.99 K, x(H) 0–0.00164
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:cub-a13)

Names (4): _corpus: _corpus:phase:h-mn:cub-a13  
_paper: _paper:10.1007/s11669-018-0622-7:(βMn)  
_tdb: _tdb:MnH-11Lob.tdb:CUB_A13, tdb:MnH-18Lia.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): CUB_A13, type code %, sha256 `d20c86d703fa6e37…`

~~~~text
53: PHASE CUB_A13 % 2 1 1 !
54: CONST CUB_A13 : MN : H VA% : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): CUB_A13, type code %, sha256 `ee68c7da6eef802b…`

~~~~text
55: PHASE CUB_A13 % 2 1 1 !
56: CONST CUB_A13 : MN : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
_assessment that models this phase_

## FCC_A1 (H–Mn)

- Id: `phase:h-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1358.05–1415.18 K, x(H) 0–0.002
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:fcc-a1)

Names (4): _corpus: _corpus:phase:h-mn:fcc-a1  
_paper: _paper:10.1007/s11669-018-0622-7:(γMn)  
_tdb: _tdb:MnH-11Lob.tdb:FCC_A1, tdb:MnH-18Lia.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): FCC_A1, type code %A, sha256 `d20c86d703fa6e37…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MN : H VA% : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): FCC_A1, type code %A, sha256 `ee68c7da6eef802b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : MN : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
_assessment that models this phase_

## GAS (H–Mn)

- Id: `phase:h-mn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:gas)

Names (4): _corpus: _corpus:phase:h-mn:gas  
_paper: _paper:10.1007/s11669-018-0622-7:Gas  
_tdb: _tdb:MnH-11Lob.tdb:GAS, tdb:MnH-18Lia.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): GAS, type code %, sha256 `d20c86d703fa6e37…`

~~~~text
56: PHASE GAS:G % 1 1 !
57: CONST GAS:G : H H2 MN MNH : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): GAS, type code %, sha256 `ee68c7da6eef802b…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : H H2 MN MNH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
_assessment that models this phase_

## H2GAS (H–Mn)

- Id: `phase:h-mn:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300.44–771.69 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:h2gas)

Names (3): _corpus: _corpus:phase:h-mn:h2gas  
_tdb: _tdb:MnH-11Lob.tdb:H2GAS, tdb:MnH-18Lia.tdb:H2GAS  


### TDB models of H2GAS (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): H2GAS, type code %, sha256 `d20c86d703fa6e37…`

~~~~text
59: PHASE H2GAS % 1 1 !
60: CONST H2GAS : H2 : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): H2GAS, type code %, sha256 `ee68c7da6eef802b…`

~~~~text
61: PHASE H2GAS % 1 1 !
62: CONST H2GAS : H2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
_assessment that models this phase_
- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase_

## HCP_A3 (H–Mn)

- Id: `phase:h-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–396.69 K, x(H) 0.47216–0.49531
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:hcp-a3)

Names (3): _corpus: _corpus:phase:h-mn:hcp-a3  
_tdb: _tdb:MnH-11Lob.tdb:HCP_A3, tdb:MnH-18Lia.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): HCP_A3, type code %A, sha256 `d20c86d703fa6e37…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : MN : H VA% : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): HCP_A3, type code %A, sha256 `ee68c7da6eef802b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 1 !
46: CONST HCP_A3 : MN : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
_assessment that models this phase_
- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase_

## LIQUID (H–Mn)

- Id: `phase:h-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1515.26–2339.53 K, x(H) 0–0.00454
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mn:liquid)

Names (4): _corpus: _corpus:phase:h-mn:liquid  
_paper: _paper:10.1007/s11669-018-0622-7:L  
_tdb: _tdb:MnH-11Lob.tdb:LIQUID, tdb:MnH-18Lia.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MnH-11Lob.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb): LIQUID, type code %, sha256 `d20c86d703fa6e37…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : MN H : !
~~~~

[MnH-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb): LIQUID, type code %, sha256 `ee68c7da6eef802b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : MN H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011).  
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
