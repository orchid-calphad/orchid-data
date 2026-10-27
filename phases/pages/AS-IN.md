# As–In phases

> As–In system: 8 phases (tier A 6, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-IN.html · Markdown: https://data.orchid-project.org/phases/pages/AS-IN.md

8 phases (tier A 6, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-IN) · [full JSON](https://data.orchid-project.org/phases/systems/AS-IN.json) · [As–In system page](https://data.orchid-project.org/systems/AS-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/AS-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–In system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-as-in-a6-tetragonal); _phase:as-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(As) 0–0 | 0 | 1 |
| [RHOMBOHEDRAL_A7](#phase-as-in-a7-rhombohedral); _phase:as-in:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–888.71 K, x(As) 0.99831–1 | 0 | 1 |
| [ZINCBLENDE_B3](#phase-as-in-b3-zincblende); _phase:as-in:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1210.87 K, x(As) 0.5–0.5 | 0 | 1 |
| [BCC_A2](#phase-as-in-bcc-a2); _phase:as-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-as-in-fcc-a1); _phase:as-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-as-in-gas); _phase:as-in:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 888.71–2500 K, x(As) 0–1 | 0 | 1 |
| [HCP_A3](#phase-as-in-hcp-a3); _phase:as-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-as-in-liquid); _phase:as-in:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2303.09 K, x(As) 0–0.60938 | 0 | 1 |

## TETRAGONAL_A6 (As–In)

- Id: `phase:as-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(As) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:a6-tetragonal)

Names (2): _corpus: _corpus:phase:as-in:a6-tetragonal  
_tdb: _tdb:InAs-90Cha-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): TETRAGONAL_A6, type code %, sha256 `8a3241f4ff3ca63a…`

~~~~text
51: PHASE TETRAGONAL_A6 % 1 1 !
52: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (As–In)

- Id: `phase:as-in:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–888.71 K, x(As) 0.99831–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:as-in:a7-rhombohedral  
_tdb: _tdb:InAs-90Cha-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8a3241f4ff3ca63a…`

~~~~text
56: PHASE RHOMBOHEDRAL_A7 % 1 1 !
57: CONST RHOMBOHEDRAL_A7 : AS% IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
_assessment that models this phase_

## ZINCBLENDE_B3 (As–In)

- Id: `phase:as-in:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabeaz and oqmd-4656, space group 216
- Stoichiometry: As 0.5000, In 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1210.87 K, x(As) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:b3-zincblende)

Names (4): _corpus: _corpus:phase:as-in:b3-zincblende  
_mp: _mp:mp-aaaabeaz  
_oqmd: _oqmd:oqmd-4656  
_tdb: _tdb:InAs-90Cha-LB.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `8a3241f4ff3ca63a…`

~~~~text
61: PHASE ZINCBLENDE_B3 % 2 1 1 !
62: CONST ZINCBLENDE_B3 : IN : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
_assessment that models this phase_

## BCC_A2 (As–In)

- Id: `phase:as-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:bcc-a2)

Names (2): _corpus: _corpus:phase:as-in:bcc-a2  
_tdb: _tdb:InAs-90Cha-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): BCC_A2, type code %B, sha256 `8a3241f4ff3ca63a…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : AS IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
_assessment that models this phase_

## FCC_A1 (As–In)

- Id: `phase:as-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:fcc-a1)

Names (2): _corpus: _corpus:phase:as-in:fcc-a1  
_tdb: _tdb:InAs-90Cha-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): FCC_A1, type code %A, sha256 `8a3241f4ff3ca63a…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AS IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
_assessment that models this phase_

## GAS (As–In)

- Id: `phase:as-in:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 888.71–2500 K, x(As) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:gas)

Names (2): _corpus: _corpus:phase:as-in:gas  
_tdb: _tdb:InAs-90Cha-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): GAS, type code %, sha256 `8a3241f4ff3ca63a…`

~~~~text
64: PHASE GAS:G % 1 1 !
65: CONST GAS:G : AS AS2 AS4 ASIN IN IN2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
_assessment that models this phase_

## HCP_A3 (As–In)

- Id: `phase:as-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:hcp-a3)

Names (2): _corpus: _corpus:phase:as-in:hcp-a3  
_tdb: _tdb:InAs-90Cha-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): HCP_A3, type code %A, sha256 `8a3241f4ff3ca63a…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : AS IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
_assessment that models this phase_

## LIQUID (As–In)

- Id: `phase:as-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2303.09 K, x(As) 0–0.60938
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-in:liquid)

Names (2): _corpus: _corpus:phase:as-in:liquid  
_tdb: _tdb:InAs-90Cha-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InAs-90Cha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InAs-90Cha-LB.tdb): LIQUID, type code %, sha256 `8a3241f4ff3ca63a…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : AS IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(90)90021-Q](https://doi.org/10.1016/0364-5916%2890%2990021-Q) C. Chatillon, I. Ansara, A. Watson, B.B. Argent, Calphad, 14, 203-14(1990).  
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
