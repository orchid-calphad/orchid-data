# O–Sr phases

> O–Sr system: 8 phases (tier A 4, liquid 1, gas 2, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-SR.html · Markdown: https://data.orchid-project.org/phases/pages/O-SR.md

8 phases (tier A 4, liquid 1, gas 2, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-SR) · [full JSON](https://data.orchid-project.org/phases/systems/O-SR.json) · [O–Sr system page](https://data.orchid-project.org/systems/O-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Sr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-sr-bcc-a2); _phase:o-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1047–2500 K, x(O) 0–0 | 0 | 1 |
| [FCC_A1](#phase-o-sr-fcc-a1); _phase:o-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–817.5 K, x(O) 0–0 | 0 | 1 |
| [GAS](#phase-o-sr-gas); _phase:o-sr:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1644.54–2500 K, x(O) 0–0.99996 | 0 | 1 |
| [HCP_A3](#phase-o-sr-hcp-a3); _phase:o-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-o-sr-ion); _phase:o-sr:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1047–2500 K, x(O) 0–0.07 | 0 | 1 |
| [O2GAS](#phase-o-sr-o2gas); _phase:o-sr:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–325 K, x(O) 1–1 | 0 | 1 |
| [SRO_B1](#phase-o-sr-sro-b1); _phase:o-sr:sro-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0.5–0.5 | 7 | 1 |
| [SRO2_C11A](#phase-o-sr-sro2-c11a); _phase:o-sr:sro2-c11a_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–495 K, x(O) 0.66667–0.66667 | 0 | 1 |

## BCC_A2 (O–Sr)

- Id: `phase:o-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Sr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1047–2500 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:bcc-a2)

Names (2): _corpus: _corpus:phase:o-sr:bcc-a2  
_tdb: _tdb:SrO-96Ris-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): BCC_A2, type code %B, sha256 `a0cbfdaeb5428ddd…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
_assessment that models this phase_

## FCC_A1 (O–Sr)

- Id: `phase:o-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–817.5 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:fcc-a1)

Names (2): _corpus: _corpus:phase:o-sr:fcc-a1  
_tdb: _tdb:SrO-96Ris-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): FCC_A1, type code %A, sha256 `a0cbfdaeb5428ddd…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : SR : VA% O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
_assessment that models this phase_

## GAS (O–Sr)

- Id: `phase:o-sr:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1644.54–2500 K, x(O) 0–0.99996
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:gas)

Names (2): _corpus: _corpus:phase:o-sr:gas  
_tdb: _tdb:SrO-96Ris-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): GAS, type code %, sha256 `a0cbfdaeb5428ddd…`

~~~~text
68: PHASE GAS:G % 1 1 !
69: CONST GAS:G : O O2 O3 SR SR2 SRO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
_assessment that models this phase_

## HCP_A3 (O–Sr)

- Id: `phase:o-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sr 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:hcp-a3)

Names (2): _corpus: _corpus:phase:o-sr:hcp-a3  
_tdb: _tdb:SrO-96Ris-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): HCP_A3, type code %A, sha256 `a0cbfdaeb5428ddd…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
_assessment that models this phase_

## ION (O–Sr)

- Id: `phase:o-sr:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1047–2500 K, x(O) 0–0.07
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:ion)

Names (2): _corpus: _corpus:phase:o-sr:ion  
_tdb: _tdb:SrO-96Ris-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): ION, type code %, sha256 `a0cbfdaeb5428ddd…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : SR+2 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
_assessment that models this phase_

## O2GAS (O–Sr)

- Id: `phase:o-sr:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–325 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:o2gas)

Names (2): _corpus: _corpus:phase:o-sr:o2gas  
_tdb: _tdb:SrO-96Ris-LB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): O2GAS, type code %, sha256 `a0cbfdaeb5428ddd…`

~~~~text
65: PHASE O2GAS % 1 1 !
66: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
_assessment that models this phase_

## SRO_B1 (O–Sr)

- Id: `phase:o-sr:sro-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0.5–0.5
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:sro-b1)

Names (3): _corpus: _corpus:phase:o-sr:sro-b1  
_paper: _paper:10.1016/s0364-5916(96)00037-5:SrO  
_tdb: _tdb:SrO-96Ris-LB.tdb:SRO_B1  


### TDB models of SRO_B1 (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): SRO_B1, type code %, sha256 `a0cbfdaeb5428ddd…`

~~~~text
57: PHASE SRO_B1:I % 2 1 1 !
58: CONST SRO_B1:I : SR+2 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0038-092x(65)90162-3](https://doi.org/10.1016/0038-092x%2865%2990162-3) Marc Foex, Measurement of the solidification points of several refractory oxides by means of a solar furnace, Solar Energy 9, 61-67 (1965).  
_cited as the source of values for this phase_

## SRO2_C11A (O–Sr)

- Id: `phase:o-sr:sro2-c11a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_C11_a; site_ratios_contradict_C11_a:SrO-96Ris-LB.tdb
- Candidate (name_token): CaC2 · C11_a · tI6 · I4/mmm (139) — Strukturbericht/word 'C11A' in the TDB name
- Candidate (sgte_mmc2): CaC2 · C11_a · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for SRO2_C11A: SrO2 (peroxide)
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — SrO-96Ris-LB.tdb: 'Prototype CaC2 (tI6, I4/mmm); Strontium peroxide'
- Stability: stable in 1 of 1 calculated diagram(s): 300–495 K, x(O) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-sr:sro2-c11a)

Names (2): _corpus: _corpus:phase:o-sr:sro2-c11a  
_tdb: _tdb:SrO-96Ris-LB.tdb:SRO2_C11A  


### TDB models of SRO2_C11A (1): PHASE and CONSTITUENT statements as written

[SrO-96Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SrO-96Ris-LB.tdb): SRO2_C11A, type code %, sha256 `a0cbfdaeb5428ddd…`

~~~~text
62: PHASE SRO2_C11A:I % 2 1 1 !
63: CONST SRO2_C11A:I : SR+2 : O2-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00037-5](https://doi.org/10.1016/S0364-5916%2896%2900037-5) D. Risold, B. Hallstedt, L.J. Gauckler, Calphad, 20, 353-61(1996).  
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
