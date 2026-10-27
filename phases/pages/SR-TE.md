# Sr–Te phases

> Sr–Te system: 8 phases (tier A 5, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SR-TE.html · Markdown: https://data.orchid-project.org/phases/pages/SR-TE.md

8 phases (tier A 5, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SR-TE) · [full JSON](https://data.orchid-project.org/phases/systems/SR-TE.json) · [Sr–Te system page](https://data.orchid-project.org/systems/SR-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/SR-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sr–Te system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-sr-te-a8-hexagonal); _phase:sr-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 2 | 1 |
| [BCC_A2](#phase-sr-te-bcc-a2); _phase:sr-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 820–1057 K, x(Te) 0–0 | 2 | 1 |
| [FCC_A1](#phase-sr-te-fcc-a1); _phase:sr-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–820 K, x(Te) 0–0 | 0 | 1 |
| [HCP_A3](#phase-sr-te-hcp-a3); _phase:sr-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-sr-te-liquid); _phase:sr-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 722.66–2500 K, x(Te) 0–1 | 10 | 1 |
| [SR2TE3](#phase-sr-te-sr2te3); _phase:sr-te:sr2te3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1193.03 K, x(Te) 0.6–0.6 | 4 | 1 |
| [SRTE_B1](#phase-sr-te-srte-b1); _phase:sr-te:srte-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1764 K, x(Te) 0.5–0.5 | 6 | 1 |
| [SRTE2](#phase-sr-te-srte2); _phase:sr-te:srte2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1123.15 K, x(Te) 0.66667–0.66667 | 4 | 1 |

## HEXAGONAL_A8 (Sr–Te)

- Id: `phase:sr-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:sr-te:a8-hexagonal, corpus:phase:sr-te:hexagonal-a8  
_paper: _paper:10.1007/s11669-022-00950-z:(Te)  
_tdb: _tdb:SrTe-22Yu.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): HEXAGONAL_A8, type code %, sha256 `e40e229b044ae412…`

~~~~text
47: PHASE HEXAGONAL_A8 % 1 1 !
48: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Sr–Te)

- Id: `phase:sr-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Sr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 820–1057 K, x(Te) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:bcc-a2)

Names (3): _corpus: _corpus:phase:sr-te:bcc-a2  
_paper: _paper:10.1007/s11669-022-00950-z:(Sr)  
_tdb: _tdb:SrTe-22Yu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): BCC_A2, type code %B, sha256 `e40e229b044ae412…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Sr–Te)

- Id: `phase:sr-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Sr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–820 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:fcc-a1)

Names (2): _corpus: _corpus:phase:sr-te:fcc-a1  
_tdb: _tdb:SrTe-22Yu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): FCC_A1, type code %A, sha256 `e40e229b044ae412…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase_

## HCP_A3 (Sr–Te)

- Id: `phase:sr-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sr 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:hcp-a3)

Names (2): _corpus: _corpus:phase:sr-te:hcp-a3  
_tdb: _tdb:SrTe-22Yu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): HCP_A3, type code %A, sha256 `e40e229b044ae412…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : SR : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase_

## LIQUID (Sr–Te)

- Id: `phase:sr-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 722.66–2500 K, x(Te) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:liquid)

Names (3): _corpus: _corpus:phase:sr-te:liquid  
_paper: _paper:10.1007/s11669-022-00950-z:L  
_tdb: _tdb:SrTe-22Yu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): LIQUID, type code %, sha256 `e40e229b044ae412…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : SR TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_

## SR2TE3 (Sr–Te)

- Id: `phase:sr-te:sr2te3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Sr2Te3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Sr2Te3) — Hallstedt 2025 mmc2 row for SR2TE3: Sr2Te3
- Stoichiometry: Sr 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1193.03 K, x(Te) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:sr2te3)

Names (3): _corpus: _corpus:phase:sr-te:sr2te3  
_paper: _paper:10.1007/s11669-022-00950-z:Sr2Te3  
_tdb: _tdb:SrTe-22Yu.tdb:SR2TE3  


### TDB models of SR2TE3 (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): SR2TE3, type code %, sha256 `e40e229b044ae412…`

~~~~text
57: PHASE SR2TE3 % 2 2 3 !
58: CONST SR2TE3 : SR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_

## SRTE_B1 (Sr–Te)

- Id: `phase:sr-te:srte-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacxi and oqmd-656717, space group 225
- Stoichiometry: Sr 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1764 K, x(Te) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:srte-b1)

Names (5): _corpus: _corpus:phase:sr-te:srte-b1  
_mp: _mp:mp-aaaaacxi  
_oqmd: _oqmd:oqmd-656717  
_paper: _paper:10.1007/s11669-022-00950-z:SrTe  
_tdb: _tdb:SrTe-22Yu.tdb:SRTE_B1  


### TDB models of SRTE_B1 (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): SRTE_B1, type code %, sha256 `e40e229b044ae412…`

~~~~text
52: PHASE SRTE_B1 % 2 1 1 !
53: CONST SRTE_B1 : SR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_

## SRTE2 (Sr–Te)

- Id: `phase:sr-te:srte2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (SrTe2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (SrTe2) — Hallstedt 2025 mmc2 row for SRTE2: SrTe2
- Stoichiometry: Sr 0.3333, Te 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1123.15 K, x(Te) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-te:srte2)

Names (3): _corpus: _corpus:phase:sr-te:srte2  
_paper: _paper:10.1007/s11669-022-00950-z:SrTe2  
_tdb: _tdb:SrTe-22Yu.tdb:SRTE2  


### TDB models of SRTE2 (1): PHASE and CONSTITUENT statements as written

[SrTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb): SRTE2, type code %, sha256 `e40e229b044ae412…`

~~~~text
62: PHASE SRTE2 % 2 1 2 !
63: CONST SRTE2 : SR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_

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
