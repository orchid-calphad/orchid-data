# Ce–La phases

> Ce–La system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-LA.html · Markdown: https://data.orchid-project.org/phases/pages/CE-LA.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-LA) · [full JSON](https://data.orchid-project.org/phases/systems/CE-LA.json) · [Ce–La system page](https://data.orchid-project.org/systems/CE-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–La system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-la-bcc-a2); _phase:ce-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1000–1192.71 K, x(La) 0–1 | 0 | 2 |
| [DHCP](#phase-ce-la-dhcp-a3); _phase:ce-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–550 K, x(La) 0.03–1 | 0 | 2 |
| [FCC_A1](#phase-ce-la-fcc-a1); _phase:ce-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1134 K, x(La) 0–1 | 0 | 2 |
| [HCP_A3](#phase-ce-la-hcp-a3); _phase:ce-la:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ce-la-liquid); _phase:ce-la:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1072–2500 K, x(La) 0–1 | 0 | 2 |

## BCC_A2 (Ce–La)

- Id: `phase:ce-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1000–1192.71 K, x(La) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-la:bcc-a2)

Names (3): _corpus: _corpus:phase:ce-la:bcc-a2  
_tdb: _tdb:CeLa-10Guo.tdb:BCC_A2, tdb:CeLa-19Yan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CeLa-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-10Guo.tdb): BCC_A2, type code %B, sha256 `cc9bfba02dce858a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CE% LA% : VA% : !
~~~~

[CeLa-19Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-19Yan.tdb): BCC_A2, type code %B, sha256 `2b13e2965561d761…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CE% LA% : VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jre.2019.02.003](https://doi.org/10.1016/j.jre.2019.02.003) K. Yang, J. Wang, Q. Yao, Z. Lu, M. Rong, H. Zhou, G. Rao, J. Rare Earths, 37, 1040-46(2019).  
_assessment that models this phase_
- [doi:10.3139/146.110380](https://doi.org/10.3139/146.110380) C. Guo, Z. Du, C. Li, Int. J. Mater. Res., 101, 1424-31(2010).  
_assessment that models this phase_

## DHCP (Ce–La)

- Id: `phase:ce-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–550 K, x(La) 0.03–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-la:dhcp-a3)

Names (3): _corpus: _corpus:phase:ce-la:dhcp-a3  
_tdb: _tdb:CeLa-10Guo.tdb:DHCP, tdb:CeLa-19Yan.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[CeLa-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-10Guo.tdb): DHCP, type code %A, sha256 `cc9bfba02dce858a…`

~~~~text
40: PHASE DHCP %A 2 1 0.5 !
41: CONST DHCP : CE% LA% : VA% : !
~~~~

[CeLa-19Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-19Yan.tdb): DHCP, type code %A, sha256 `2b13e2965561d761…`

~~~~text
42: PHASE DHCP %A 1 1 !
43: CONST DHCP : CE% LA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jre.2019.02.003](https://doi.org/10.1016/j.jre.2019.02.003) K. Yang, J. Wang, Q. Yao, Z. Lu, M. Rong, H. Zhou, G. Rao, J. Rare Earths, 37, 1040-46(2019).  
_assessment that models this phase_
- [doi:10.3139/146.110380](https://doi.org/10.3139/146.110380) C. Guo, Z. Du, C. Li, Int. J. Mater. Res., 101, 1424-31(2010).  
_assessment that models this phase_

## FCC_A1 (Ce–La)

- Id: `phase:ce-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1134 K, x(La) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-la:fcc-a1)

Names (3): _corpus: _corpus:phase:ce-la:fcc-a1  
_tdb: _tdb:CeLa-10Guo.tdb:FCC_A1, tdb:CeLa-19Yan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CeLa-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-10Guo.tdb): FCC_A1, type code %A, sha256 `cc9bfba02dce858a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CE% LA% : VA% : !
~~~~

[CeLa-19Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-19Yan.tdb): FCC_A1, type code %A, sha256 `2b13e2965561d761…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CE% LA% : VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jre.2019.02.003](https://doi.org/10.1016/j.jre.2019.02.003) K. Yang, J. Wang, Q. Yao, Z. Lu, M. Rong, H. Zhou, G. Rao, J. Rare Earths, 37, 1040-46(2019).  
_assessment that models this phase_
- [doi:10.3139/146.110380](https://doi.org/10.3139/146.110380) C. Guo, Z. Du, C. Li, Int. J. Mater. Res., 101, 1424-31(2010).  
_assessment that models this phase_

## HCP_A3 (Ce–La)

- Id: `phase:ce-la:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-la:hcp-a3)

Names (3): _corpus: _corpus:phase:ce-la:hcp-a3  
_tdb: _tdb:CeLa-10Guo.tdb:HCP_A3, tdb:CeLa-19Yan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CeLa-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-10Guo.tdb): HCP_A3, type code %A, sha256 `cc9bfba02dce858a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CE LA : VA% : !
~~~~

[CeLa-19Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-19Yan.tdb): HCP_A3, type code %A, sha256 `2b13e2965561d761…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CE : VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jre.2019.02.003](https://doi.org/10.1016/j.jre.2019.02.003) K. Yang, J. Wang, Q. Yao, Z. Lu, M. Rong, H. Zhou, G. Rao, J. Rare Earths, 37, 1040-46(2019).  
_assessment that models this phase_
- [doi:10.3139/146.110380](https://doi.org/10.3139/146.110380) C. Guo, Z. Du, C. Li, Int. J. Mater. Res., 101, 1424-31(2010).  
_assessment that models this phase_

## LIQUID (Ce–La)

- Id: `phase:ce-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1072–2500 K, x(La) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-la:liquid)

Names (3): _corpus: _corpus:phase:ce-la:liquid  
_tdb: _tdb:CeLa-10Guo.tdb:LIQUID, tdb:CeLa-19Yan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CeLa-10Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-10Guo.tdb): LIQUID, type code %, sha256 `cc9bfba02dce858a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CE LA : !
~~~~

[CeLa-19Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeLa-19Yan.tdb): LIQUID, type code %, sha256 `2b13e2965561d761…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CE LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jre.2019.02.003](https://doi.org/10.1016/j.jre.2019.02.003) K. Yang, J. Wang, Q. Yao, Z. Lu, M. Rong, H. Zhou, G. Rao, J. Rare Earths, 37, 1040-46(2019).  
_assessment that models this phase_
- [doi:10.3139/146.110380](https://doi.org/10.3139/146.110380) C. Guo, Z. Du, C. Li, Int. J. Mater. Res., 101, 1424-31(2010).  
_assessment that models this phase_

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
