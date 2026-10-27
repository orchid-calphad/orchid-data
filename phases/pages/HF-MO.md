# Hf–Mo phases

> Hf–Mo system: 7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-MO.html · Markdown: https://data.orchid-project.org/phases/pages/HF-MO.md

7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-MO) · [full JSON](https://data.orchid-project.org/phases/systems/HF-MO.json) · [Hf–Mo system page](https://data.orchid-project.org/systems/HF-MO.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-MO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Mo system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-mo-bcc-a2); _phase:hf-mo:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.77 K, x(Mo) 0–1 | 0 | 2 |
| [C14_LAVES](#phase-hf-mo-c14-laves); _phase:hf-mo:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C15_LAVES](#phase-hf-mo-c15-laves); _phase:hf-mo:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2150 K, x(Mo) 0.64111–0.66667 | 0 | 2 |
| [C36_LAVES](#phase-hf-mo-c36-laves); _phase:hf-mo:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2061.11–2441.95 K, x(Mo) 0.63571–0.6638 | 0 | 2 |
| [FCC_A1](#phase-hf-mo-fcc-a1); _phase:hf-mo:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-hf-mo-hcp-a3); _phase:hf-mo:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2548.52 K, x(Mo) 0–0.01763 | 0 | 2 |
| [LIQUID](#phase-hf-mo-liquid); _phase:hf-mo:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2140.61–4000 K, x(Mo) 0–1 | 0 | 2 |

## BCC_A2 (Hf–Mo)

- Id: `phase:hf-mo:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.77 K, x(Mo) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mo:bcc-a2)

Names (3): _corpus: _corpus:phase:hf-mo:bcc-a2  
_tdb: _tdb:HfMo-02Sha-LB.tdb:BCC_A2, tdb:HfMo-20Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfMo-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-02Sha-LB.tdb): BCC_A2, type code %B, sha256 `05fc90dfe4897c9d…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : HF MO : VA : !
~~~~

[HfMo-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-20Zha.tdb): BCC_A2, type code %B, sha256 `c2fd244a29112241…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : HF MO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## C14_LAVES (Hf–Mo)

- Id: `phase:hf-mo:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfMo-20Zha.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mo:c14-laves)

Names (2): _corpus: _corpus:phase:hf-mo:c14-laves  
_tdb: _tdb:HfMo-20Zha.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[HfMo-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-20Zha.tdb): C14_LAVES, type code %, sha256 `c2fd244a29112241…`

~~~~text
45: PHASE C14_LAVES % 2 2 1 !
46: CONST C14_LAVES : HF MO% : HF% MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_

## C15_LAVES (Hf–Mo)

- Id: `phase:hf-mo:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfMo-02Sha-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in HfMo-20Zha.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–2150 K, x(Mo) 0.64111–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mo:c15-laves)

Names (3): _corpus: _corpus:phase:hf-mo:c15-laves  
_tdb: _tdb:HfMo-02Sha-LB.tdb:C15_LAVES, tdb:HfMo-20Zha.tdb:C15_LAVES  


### TDB models of C15_LAVES (2): PHASE and CONSTITUENT statements as written

[HfMo-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-02Sha-LB.tdb): C15_LAVES, type code %, sha256 `05fc90dfe4897c9d…`

~~~~text
42: PHASE C15_LAVES % 2 2 1 !
43: CONST C15_LAVES : HF MO% : HF% MO : !
~~~~

[HfMo-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-20Zha.tdb): C15_LAVES, type code %, sha256 `c2fd244a29112241…`

~~~~text
50: PHASE C15_LAVES % 2 2 1 !
51: CONST C15_LAVES : HF MO% : HF% MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## C36_LAVES (Hf–Mo)

- Id: `phase:hf-mo:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfMo-02Sha-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in HfMo-20Zha.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 2061.11–2441.95 K, x(Mo) 0.63571–0.6638
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mo:c36-laves)

Names (3): _corpus: _corpus:phase:hf-mo:c36-laves  
_tdb: _tdb:HfMo-02Sha-LB.tdb:C36_LAVES, tdb:HfMo-20Zha.tdb:C36_LAVES  


### TDB models of C36_LAVES (2): PHASE and CONSTITUENT statements as written

[HfMo-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-02Sha-LB.tdb): C36_LAVES, type code %, sha256 `05fc90dfe4897c9d…`

~~~~text
47: PHASE C36_LAVES % 2 2 1 !
48: CONST C36_LAVES : HF MO% : HF% MO : !
~~~~

[HfMo-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-20Zha.tdb): C36_LAVES, type code %, sha256 `c2fd244a29112241…`

~~~~text
55: PHASE C36_LAVES % 2 2 1 !
56: CONST C36_LAVES : HF MO% : HF% MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## FCC_A1 (Hf–Mo)

- Id: `phase:hf-mo:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mo:fcc-a1)

Names (3): _corpus: _corpus:phase:hf-mo:fcc-a1  
_tdb: _tdb:HfMo-02Sha-LB.tdb:FCC_A1, tdb:HfMo-20Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HfMo-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-02Sha-LB.tdb): FCC_A1, type code %A, sha256 `05fc90dfe4897c9d…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : HF MO : VA : !
~~~~

[HfMo-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-20Zha.tdb): FCC_A1, type code %A, sha256 `c2fd244a29112241…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : HF MO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## HCP_A3 (Hf–Mo)

- Id: `phase:hf-mo:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2548.52 K, x(Mo) 0–0.01763
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mo:hcp-a3)

Names (3): _corpus: _corpus:phase:hf-mo:hcp-a3  
_tdb: _tdb:HfMo-02Sha-LB.tdb:HCP_A3, tdb:HfMo-20Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HfMo-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-02Sha-LB.tdb): HCP_A3, type code %A, sha256 `05fc90dfe4897c9d…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : HF% MO : VA : !
~~~~

[HfMo-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-20Zha.tdb): HCP_A3, type code %A, sha256 `c2fd244a29112241…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : HF% MO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## LIQUID (Hf–Mo)

- Id: `phase:hf-mo:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2140.61–4000 K, x(Mo) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mo:liquid)

Names (3): _corpus: _corpus:phase:hf-mo:liquid  
_tdb: _tdb:HfMo-02Sha-LB.tdb:LIQUID, tdb:HfMo-20Zha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HfMo-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-02Sha-LB.tdb): LIQUID, type code %, sha256 `05fc90dfe4897c9d…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : HF MO : !
~~~~

[HfMo-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMo-20Zha.tdb): LIQUID, type code %, sha256 `c2fd244a29112241…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : HF MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
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
