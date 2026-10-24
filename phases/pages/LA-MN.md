# La–Mn phases

> La–Mn system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LA-MN.html · Markdown: https://data.orchid-project.org/phases/pages/LA-MN.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LA-MN) · [full JSON](https://data.orchid-project.org/phases/systems/LA-MN.json) · [La–Mn system page](https://data.orchid-project.org/systems/LA-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/LA-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the La–Mn system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-la-mn-bcc-a2); _phase:la-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1030–2499.42 K, x(Mn) 0–1 | 7 | 2 |
| [CBCC_A12](#phase-la-mn-cbcc-a12); _phase:la-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1030.25 K, x(Mn) 0.23–1 | 10 | 2 |
| [CUB_A13](#phase-la-mn-cub-a13); _phase:la-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300.25–1404.99 K, x(Mn) 0.2–1 | 9 | 2 |
| [DHCP](#phase-la-mn-dhcp-a3); _phase:la-mn:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1130 K, x(Mn) 0–0 | 0 | 2 |
| [FCC_A1](#phase-la-mn-fcc-a1); _phase:la-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 550–1426.01 K, x(Mn) 0–1 | 16 | 2 |
| [HCP_A3](#phase-la-mn-hcp-a3); _phase:la-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-la-mn-liquid); _phase:la-mn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 972.01–2500 K, x(Mn) 0–1 | 24 | 2 |

## BCC_A2 (La–Mn)

- Id: `phase:la-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1030–2499.42 K, x(Mn) 0–1
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-mn:bcc-a2)

Names (7): _corpus: _corpus:phase:la-mn:bcc-a2  
_paper: _paper:10.2298/jmmb120717049w:(γLa), paper:10.2298/jmmb120717049w:(δMn), paper:10.4028/www.scientific.net/msf.850.21:γ-La, paper:10.4028/www.scientific.net/msf.850.21:δ-Mn  
_tdb: _tdb:LaMn-12Wan.tdb:BCC_A2, tdb:LaMn-16Zhu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[LaMn-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-12Wan.tdb): BCC_A2, type code %B, sha256 `7161f70fb98ae052…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : LA% MN% : VA : !
~~~~

[LaMn-16Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-16Zhu.tdb): BCC_A2, type code %B, sha256 `222466a058a17a94…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : LA% MN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB120717049W](https://doi.org/10.2298/JMMB120717049W) Y. Wang, B. Hu, S. Liu, Y. Du, J. Mining Metall. B, 48, 391-94(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.4028/www.scientific.net/msf.850.21](https://doi.org/10.4028/www.scientific.net/msf.850.21) Chao Fan Zhu, Shi Dong Lin, Jiang Wang, Mao Hua Rong, Guang Hui Rao, Huai Ying Zhou, Thermodynamic Re-Assessment of the Mn-La Binary System, MSF 850, 21-26 (2016).  
_reports values for this phase_

## CBCC_A12 (La–Mn)

- Id: `phase:la-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1030.25 K, x(Mn) 0.23–1
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-mn:cbcc-a12)

Names (5): _corpus: _corpus:phase:la-mn:cbcc-a12  
_paper: _paper:10.2298/jmmb120717049w:(αMn), paper:10.4028/www.scientific.net/msf.850.21:α-Mn  
_tdb: _tdb:LaMn-12Wan.tdb:CBCC_A12, tdb:LaMn-16Zhu.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[LaMn-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-12Wan.tdb): CBCC_A12, type code %A, sha256 `7161f70fb98ae052…`

~~~~text
45: PHASE CBCC_A12 %A 2 1 1 !
46: CONST CBCC_A12 : MN : VA : !
~~~~

[LaMn-16Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-16Zhu.tdb): CBCC_A12, type code %A, sha256 `222466a058a17a94…`

~~~~text
48: PHASE CBCC_A12 %A 2 1 1 !
49: CONST CBCC_A12 : LA MN% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.2298/JMMB120717049W](https://doi.org/10.2298/JMMB120717049W) Y. Wang, B. Hu, S. Liu, Y. Du, J. Mining Metall. B, 48, 391-94(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.4028/www.scientific.net/msf.850.21](https://doi.org/10.4028/www.scientific.net/msf.850.21) Chao Fan Zhu, Shi Dong Lin, Jiang Wang, Mao Hua Rong, Guang Hui Rao, Huai Ying Zhou, Thermodynamic Re-Assessment of the Mn-La Binary System, MSF 850, 21-26 (2016).  
_reports values for this phase_
- [doi:10.1002/cber.19420751293](https://doi.org/10.1002/cber.19420751293) L. Rolla, A. Iandelli, Ber. Deut. Chem. Ges. 75 (1942) 2091-2095.  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868307](https://doi.org/10.1007/bf02868307) H. W. King, Crystal structures of the elements at 25°C, Bulletin of Alloy Phase Diagrams 2, 401-402 (1981).  
_cited as the source of values for this phase_

## CUB_A13 (La–Mn)

- Id: `phase:la-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.25–1404.99 K, x(Mn) 0.2–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-mn:cub-a13)

Names (5): _corpus: _corpus:phase:la-mn:cub-a13  
_paper: _paper:10.2298/jmmb120717049w:(βMn), paper:10.4028/www.scientific.net/msf.850.21:β-Mn  
_tdb: _tdb:LaMn-12Wan.tdb:CUB_A13, tdb:LaMn-16Zhu.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[LaMn-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-12Wan.tdb): CUB_A13, type code %, sha256 `7161f70fb98ae052…`

~~~~text
50: PHASE CUB_A13 % 2 1 1 !
51: CONST CUB_A13 : MN : VA : !
~~~~

[LaMn-16Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-16Zhu.tdb): CUB_A13, type code %, sha256 `222466a058a17a94…`

~~~~text
53: PHASE CUB_A13 % 2 1 1 !
54: CONST CUB_A13 : LA MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB120717049W](https://doi.org/10.2298/JMMB120717049W) Y. Wang, B. Hu, S. Liu, Y. Du, J. Mining Metall. B, 48, 391-94(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.4028/www.scientific.net/msf.850.21](https://doi.org/10.4028/www.scientific.net/msf.850.21) Chao Fan Zhu, Shi Dong Lin, Jiang Wang, Mao Hua Rong, Guang Hui Rao, Huai Ying Zhou, Thermodynamic Re-Assessment of the Mn-La Binary System, MSF 850, 21-26 (2016).  
_reports values for this phase_
- [doi:10.1007/bf02868307](https://doi.org/10.1007/bf02868307) H. W. King, Crystal structures of the elements at 25°C, Bulletin of Alloy Phase Diagrams 2, 401-402 (1981).  
_cited as the source of values for this phase_

## DHCP (La–Mn)

- Id: `phase:la-mn:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1130 K, x(Mn) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-mn:dhcp-a3)

Names (4): _corpus: _corpus:phase:la-mn:dhcp-a3, corpus:phase:la-mn:dhcp  
_tdb: _tdb:LaMn-12Wan.tdb:DHCP, tdb:LaMn-16Zhu.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[LaMn-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-12Wan.tdb): DHCP, type code %, sha256 `7161f70fb98ae052…`

~~~~text
40: PHASE DHCP % 1 1 !
41: CONST DHCP : LA : !
~~~~

[LaMn-16Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-16Zhu.tdb): DHCP, type code %, sha256 `222466a058a17a94…`

~~~~text
43: PHASE DHCP % 1 1 !
44: CONST DHCP : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB120717049W](https://doi.org/10.2298/JMMB120717049W) Y. Wang, B. Hu, S. Liu, Y. Du, J. Mining Metall. B, 48, 391-94(2012).  
_assessment that models this phase_

## FCC_A1 (La–Mn)

- Id: `phase:la-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 550–1426.01 K, x(Mn) 0–1
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-mn:fcc-a1)

Names (7): _corpus: _corpus:phase:la-mn:fcc-a1  
_paper: _paper:10.2298/jmmb120717049w:(βLa), paper:10.2298/jmmb120717049w:(γMn), paper:10.4028/www.scientific.net/msf.850.21:β-La, paper:10.4028/www.scientific.net/msf.850.21:γ-Mn  
_tdb: _tdb:LaMn-12Wan.tdb:FCC_A1, tdb:LaMn-16Zhu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[LaMn-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-12Wan.tdb): FCC_A1, type code %A, sha256 `7161f70fb98ae052…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : LA% MN% : VA : !
~~~~

[LaMn-16Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-16Zhu.tdb): FCC_A1, type code %A, sha256 `222466a058a17a94…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : LA% MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB120717049W](https://doi.org/10.2298/JMMB120717049W) Y. Wang, B. Hu, S. Liu, Y. Du, J. Mining Metall. B, 48, 391-94(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.4028/www.scientific.net/msf.850.21](https://doi.org/10.4028/www.scientific.net/msf.850.21) Chao Fan Zhu, Shi Dong Lin, Jiang Wang, Mao Hua Rong, Guang Hui Rao, Huai Ying Zhou, Thermodynamic Re-Assessment of the Mn-La Binary System, MSF 850, 21-26 (2016).  
_reports values for this phase_
- [doi:10.1002/cber.19420751293](https://doi.org/10.1002/cber.19420751293) L. Rolla, A. Iandelli, Ber. Deut. Chem. Ges. 75 (1942) 2091-2095.  
_cited as the source of values for this phase_

## HCP_A3 (La–Mn)

- Id: `phase:la-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-mn:hcp-a3)

Names (3): _corpus: _corpus:phase:la-mn:hcp-a3  
_tdb: _tdb:LaMn-12Wan.tdb:HCP_A3, tdb:LaMn-16Zhu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[LaMn-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-12Wan.tdb): HCP_A3, type code %A, sha256 `7161f70fb98ae052…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MN : VA : !
~~~~

[LaMn-16Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-16Zhu.tdb): HCP_A3, type code %A, sha256 `222466a058a17a94…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB120717049W](https://doi.org/10.2298/JMMB120717049W) Y. Wang, B. Hu, S. Liu, Y. Du, J. Mining Metall. B, 48, 391-94(2012).  
_assessment that models this phase_

## LIQUID (La–Mn)

- Id: `phase:la-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 972.01–2500 K, x(Mn) 0–1
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-mn:liquid)

Names (6): _corpus: _corpus:phase:la-mn:liquid  
_paper: _paper:10.2298/jmmb120717049w:Liquid, paper:10.4028/www.scientific.net/msf.850.21:L, paper:10.4028/www.scientific.net/msf.850.21:liquid  
_tdb: _tdb:LaMn-12Wan.tdb:LIQUID, tdb:LaMn-16Zhu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[LaMn-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-12Wan.tdb): LIQUID, type code %, sha256 `7161f70fb98ae052…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : LA MN : !
~~~~

[LaMn-16Zhu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaMn-16Zhu.tdb): LIQUID, type code %, sha256 `222466a058a17a94…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : LA MN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.2298/JMMB120717049W](https://doi.org/10.2298/JMMB120717049W) Y. Wang, B. Hu, S. Liu, Y. Du, J. Mining Metall. B, 48, 391-94(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.4028/www.scientific.net/msf.850.21](https://doi.org/10.4028/www.scientific.net/msf.850.21) Chao Fan Zhu, Shi Dong Lin, Jiang Wang, Mao Hua Rong, Guang Hui Rao, Huai Ying Zhou, Thermodynamic Re-Assessment of the Mn-La Binary System, MSF 850, 21-26 (2016).  
_reports values for this phase_
- [doi:10.1002/cber.19420751293](https://doi.org/10.1002/cber.19420751293) L. Rolla, A. Iandelli, Ber. Deut. Chem. Ges. 75 (1942) 2091-2095.  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868307](https://doi.org/10.1007/bf02868307) H. W. King, Crystal structures of the elements at 25°C, Bulletin of Alloy Phase Diagrams 2, 401-402 (1981).  
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
