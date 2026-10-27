# Cu–W phases

> Cu–W system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-W.html · Markdown: https://data.orchid-project.org/phases/pages/CU-W.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-W) · [full JSON](https://data.orchid-project.org/phases/systems/CU-W.json) · [Cu–W system page](https://data.orchid-project.org/systems/CU-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–W system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-w-bcc-a2); _phase:cu-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.9 K, x(W) 0.97455–1 | 0 | 3 |
| [FCC_A1](#phase-cu-w-fcc-a1); _phase:cu-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1357.88 K, x(W) 0–0.0001 | 0 | 3 |
| [HCP_A3](#phase-cu-w-hcp-a3); _phase:cu-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-cu-w-liquid); _phase:cu-w:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1349.79–4000 K, x(W) 0–1 | 0 | 3 |

## BCC_A2 (Cu–W)

- Id: `phase:cu-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.9 K, x(W) 0.97455–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-w:bcc-a2)

Names (4): _corpus: _corpus:phase:cu-w:bcc-a2  
_tdb: _tdb:CuW-12Hal.tdb:BCC_A2, tdb:CuW-88Qiu.tdb:BCC_A2, tdb:CuW-88Vij.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CuW-12Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-12Hal.tdb): BCC_A2, type code %B, sha256 `5cf02c00c226875b…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CU W% : VA : !
~~~~

[CuW-88Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Qiu.tdb): BCC_A2, type code %B, sha256 `37e827d1d1b3fd9d…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CU W% : VA : !
~~~~

[CuW-88Vij.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Vij.tdb): BCC_A2, type code %B, sha256 `a36e72f5d45e5920…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CU W% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-184(1988).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1988-791204](https://doi.org/10.1515/ijmr-1988-791204) C. Qiu, Z.P. Jin, P.Y. Huang, Z. Metallkd., 79, 767-769(1988).  
_assessment that models this phase_

## FCC_A1 (Cu–W)

- Id: `phase:cu-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1357.88 K, x(W) 0–0.0001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-w:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-w:fcc-a1  
_tdb: _tdb:CuW-12Hal.tdb:FCC_A1, tdb:CuW-88Qiu.tdb:FCC_A1, tdb:CuW-88Vij.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CuW-12Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-12Hal.tdb): FCC_A1, type code %A, sha256 `5cf02c00c226875b…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CU% W : VA : !
~~~~

[CuW-88Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Qiu.tdb): FCC_A1, type code %A, sha256 `37e827d1d1b3fd9d…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CU% W : VA : !
~~~~

[CuW-88Vij.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Vij.tdb): FCC_A1, type code %A, sha256 `a36e72f5d45e5920…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CU% W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-184(1988).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1988-791204](https://doi.org/10.1515/ijmr-1988-791204) C. Qiu, Z.P. Jin, P.Y. Huang, Z. Metallkd., 79, 767-769(1988).  
_assessment that models this phase_

## HCP_A3 (Cu–W)

- Id: `phase:cu-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-w:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-w:hcp-a3  
_tdb: _tdb:CuW-12Hal.tdb:HCP_A3, tdb:CuW-88Qiu.tdb:HCP_A3, tdb:CuW-88Vij.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CuW-12Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-12Hal.tdb): HCP_A3, type code %A, sha256 `5cf02c00c226875b…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CU W : VA : !
~~~~

[CuW-88Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Qiu.tdb): HCP_A3, type code %A, sha256 `37e827d1d1b3fd9d…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CU W : VA : !
~~~~

[CuW-88Vij.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Vij.tdb): HCP_A3, type code %A, sha256 `a36e72f5d45e5920…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CU W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-184(1988).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1988-791204](https://doi.org/10.1515/ijmr-1988-791204) C. Qiu, Z.P. Jin, P.Y. Huang, Z. Metallkd., 79, 767-769(1988).  
_assessment that models this phase_

## LIQUID (Cu–W)

- Id: `phase:cu-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1349.79–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-w:liquid)

Names (4): _corpus: _corpus:phase:cu-w:liquid  
_tdb: _tdb:CuW-12Hal.tdb:LIQUID, tdb:CuW-88Qiu.tdb:LIQUID, tdb:CuW-88Vij.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CuW-12Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-12Hal.tdb): LIQUID, type code %, sha256 `5cf02c00c226875b…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CU W : !
~~~~

[CuW-88Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Qiu.tdb): LIQUID, type code %, sha256 `37e827d1d1b3fd9d…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CU W : !
~~~~

[CuW-88Vij.tdb](https://orchid-project.org/data/databases/sgte-binary/CuW-88Vij.tdb): LIQUID, type code %, sha256 `a36e72f5d45e5920…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CU W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-184(1988).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1988-791204](https://doi.org/10.1515/ijmr-1988-791204) C. Qiu, Z.P. Jin, P.Y. Huang, Z. Metallkd., 79, 767-769(1988).  
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
