# Ag–W phases

> Ag–W system: 5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-W.html · Markdown: https://data.orchid-project.org/phases/pages/AG-W.md

5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-W) · [full JSON](https://data.orchid-project.org/phases/systems/AG-W.json) · [Ag–W system page](https://data.orchid-project.org/systems/AG-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–W system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-w-bcc-a2); _phase:ag-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0.99981–1 | 0 | 2 |
| [FCC_A1](#phase-ag-w-fcc-a1); _phase:ag-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1235.19 K, x(W) 0–0.00067 | 0 | 2 |
| [GAS](#phase-ag-w-gas); _phase:ag-w:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 2429.89–4000 K, x(W) 0–0.00036 | 0 | 2 |
| [HCP_A3](#phase-ag-w-hcp-a3); _phase:ag-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ag-w-liquid); _phase:ag-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1233.19–4000 K, x(W) 0–1 | 0 | 2 |

## BCC_A2 (Ag–W)

- Id: `phase:ag-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0.99981–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-w:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-w:bcc-a2  
_tdb: _tdb:AgW-04Kor.tdb:BCC_A2, tdb:AgW-88Vij-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgW-04Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-04Kor.tdb): BCC_A2, type code %B, sha256 `212303e11572f78f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AG W% : VA : !
~~~~

[AgW-88Vij-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-88Vij-LB.tdb): BCC_A2, type code %B, sha256 `42fe9139c5ec2c06…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG W% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-84(1988).  
_assessment that models this phase_

## FCC_A1 (Ag–W)

- Id: `phase:ag-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1235.19 K, x(W) 0–0.00067
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-w:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-w:fcc-a1  
_tdb: _tdb:AgW-04Kor.tdb:FCC_A1, tdb:AgW-88Vij-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgW-04Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-04Kor.tdb): FCC_A1, type code %A, sha256 `212303e11572f78f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AG% W : VA : !
~~~~

[AgW-88Vij-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-88Vij-LB.tdb): FCC_A1, type code %A, sha256 `42fe9139c5ec2c06…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-84(1988).  
_assessment that models this phase_

## GAS (Ag–W)

- Id: `phase:ag-w:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2429.89–4000 K, x(W) 0–0.00036
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-w:gas)

Names (3): _corpus: _corpus:phase:ag-w:gas  
_tdb: _tdb:AgW-04Kor.tdb:GAS, tdb:AgW-88Vij-LB.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[AgW-04Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-04Kor.tdb): GAS, type code %, sha256 `212303e11572f78f…`

~~~~text
44: PHASE GAS:G % 1 1 !
45: CONST GAS:G : AG AG2 W : !
~~~~

[AgW-88Vij-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-88Vij-LB.tdb): GAS, type code %, sha256 `42fe9139c5ec2c06…`

~~~~text
43: PHASE GAS:G % 1 1 !
44: CONST GAS:G : AG AG2 W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-84(1988).  
_assessment that models this phase_

## HCP_A3 (Ag–W)

- Id: `phase:ag-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-w:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-w:hcp-a3  
_tdb: _tdb:AgW-04Kor.tdb:HCP_A3, tdb:AgW-88Vij-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgW-04Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-04Kor.tdb): HCP_A3, type code %A, sha256 `212303e11572f78f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AG W : VA : !
~~~~

[AgW-88Vij-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-88Vij-LB.tdb): HCP_A3, type code %A, sha256 `42fe9139c5ec2c06…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-84(1988).  
_assessment that models this phase_

## LIQUID (Ag–W)

- Id: `phase:ag-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1233.19–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-w:liquid)

Names (3): _corpus: _corpus:phase:ag-w:liquid  
_tdb: _tdb:AgW-04Kor.tdb:LIQUID, tdb:AgW-88Vij-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgW-04Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-04Kor.tdb): LIQUID, type code %, sha256 `212303e11572f78f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AG W : !
~~~~

[AgW-88Vij-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgW-88Vij-LB.tdb): LIQUID, type code %, sha256 `42fe9139c5ec2c06…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90019-3](https://doi.org/10.1016/0364-5916%2888%2990019-3) M. Vijayakumar, A.M. Sriramamurthy, S.V. Nagender Naidu, Calphad, 12, 177-84(1988).  
_assessment that models this phase_

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
