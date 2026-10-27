# Ni–O phases

> Ni–O system: 8 phases (tier A 4, liquid 2, gas 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-O.html · Markdown: https://data.orchid-project.org/phases/pages/NI-O.md

8 phases (tier A 4, liquid 2, gas 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-O) · [full JSON](https://data.orchid-project.org/phases/systems/NI-O.json) · [Ni–O system page](https://data.orchid-project.org/systems/NI-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–O system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [OXIDE_B1](#phase-ni-o-b1-oxide); _phase:ni-o:b1-oxide_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2235.77 K, x(O) 0.5–0.50187 | 0 | 2 |
| [BCC_A2](#phase-ni-o-bcc-a2); _phase:ni-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ni-o-fcc-a1); _phase:ni-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1728.25 K, x(O) 0–0.00171 | 0 | 2 |
| [GAS](#phase-ni-o-gas); _phase:ni-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300.46–2500 K, x(O) 0.99217–1 | 0 | 2 |
| [HCP_A3](#phase-ni-o-hcp-a3); _phase:ni-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-ni-o-ion); _phase:ni-o:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1714.17–2500 K, x(O) 0–0.49912 | 0 | 2 |
| [LIQUID](#phase-ni-o-liquid); _phase:ni-o:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1720–2500 K, x(O) 0–0.49 | 0 | 2 |
| [O2GAS](#phase-ni-o-o2gas); _phase:ni-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1620 K, x(O) 1–1 | 0 | 2 |

## OXIDE_B1 (Ni–O)

- Id: `phase:ni-o:b1-oxide`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2235.77 K, x(O) 0.5–0.50187
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:b1-oxide)

Names (3): _corpus: _corpus:phase:ni-o:b1-oxide  
_tdb: _tdb:NiO-90Tay.tdb:OXIDE_B1, tdb:NiO-95Kow.tdb:OXIDE_B1  


### TDB models of OXIDE_B1 (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): OXIDE_B1, type code %C, sha256 `a612d67283e61479…`

~~~~text
53: PHASE OXIDE_B1:I %C 2 1 1 !
54: CONST OXIDE_B1:I : NI+2% NI+3 VA : O-2 : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): OXIDE_B1, type code %C, sha256 `a7d68a7866eed0eb…`

~~~~text
55: PHASE OXIDE_B1:I %C 2 1 1 !
56: CONST OXIDE_B1:I : NI+2% NI+3 VA : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## BCC_A2 (Ni–O)

- Id: `phase:ni-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:bcc-a2)

Names (3): _corpus: _corpus:phase:ni-o:bcc-a2  
_tdb: _tdb:NiO-90Tay.tdb:BCC_A2, tdb:NiO-95Kow.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): BCC_A2, type code %B, sha256 `a612d67283e61479…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : NI : VA : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): BCC_A2, type code %B, sha256 `a7d68a7866eed0eb…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : NI : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## FCC_A1 (Ni–O)

- Id: `phase:ni-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1728.25 K, x(O) 0–0.00171
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:fcc-a1)

Names (3): _corpus: _corpus:phase:ni-o:fcc-a1  
_tdb: _tdb:NiO-90Tay.tdb:FCC_A1, tdb:NiO-95Kow.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): FCC_A1, type code %A, sha256 `a612d67283e61479…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : NI : VA : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): FCC_A1, type code %A, sha256 `a7d68a7866eed0eb…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : NI : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## GAS (Ni–O)

- Id: `phase:ni-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.46–2500 K, x(O) 0.99217–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:gas)

Names (3): _corpus: _corpus:phase:ni-o:gas  
_tdb: _tdb:NiO-90Tay.tdb:GAS, tdb:NiO-95Kow.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): GAS, type code %, sha256 `a612d67283e61479…`

~~~~text
56: PHASE GAS:G % 1 1 !
57: CONST GAS:G : NI NI2 NIO O O2% O3 : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): GAS, type code %, sha256 `a7d68a7866eed0eb…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : NI NI2 NIO O O2% O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## HCP_A3 (Ni–O)

- Id: `phase:ni-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:hcp-a3)

Names (3): _corpus: _corpus:phase:ni-o:hcp-a3  
_tdb: _tdb:NiO-90Tay.tdb:HCP_A3, tdb:NiO-95Kow.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): HCP_A3, type code %A, sha256 `a612d67283e61479…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : NI : VA : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): HCP_A3, type code %A, sha256 `a7d68a7866eed0eb…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## ION (Ni–O)

- Id: `phase:ni-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1714.17–2500 K, x(O) 0–0.49912
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:ion)

Names (3): _corpus: _corpus:phase:ni-o:ion  
_tdb: _tdb:NiO-90Tay.tdb:ION, tdb:NiO-95Kow.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): ION, type code %, sha256 `a612d67283e61479…`

~~~~text
30: PHASE ION:Y % 2 1 1 !
31: CONST ION:Y : NI+2 : O-2 VA O : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): ION, type code %, sha256 `a7d68a7866eed0eb…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : NI+2 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## LIQUID (Ni–O)

- Id: `phase:ni-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1720–2500 K, x(O) 0–0.49
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:liquid)

Names (3): _corpus: _corpus:phase:ni-o:liquid  
_tdb: _tdb:NiO-90Tay.tdb:LIQUID, tdb:NiO-95Kow.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): LIQUID, type code %, sha256 `a612d67283e61479…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : NI : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): LIQUID, type code %, sha256 `a7d68a7866eed0eb…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : NI NIO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
_assessment that models this phase_

## O2GAS (Ni–O)

- Id: `phase:ni-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1620 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-o:o2gas)

Names (3): _corpus: _corpus:phase:ni-o:o2gas  
_tdb: _tdb:NiO-90Tay.tdb:O2GAS, tdb:NiO-95Kow.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[NiO-90Tay.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb): O2GAS, type code %, sha256 `a612d67283e61479…`

~~~~text
59: PHASE O2GAS % 1 1 !
60: CONST O2GAS : O2 : !
~~~~

[NiO-95Kow.tdb](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb): O2GAS, type code %, sha256 `a7d68a7866eed0eb…`

~~~~text
61: PHASE O2GAS % 1 1 !
62: CONST O2GAS : O2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990).  
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
