# Ag–Be phases

> Ag–Be system: 5 phases (tier A 3, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-BE.html · Markdown: https://data.orchid-project.org/phases/pages/AG-BE.md

5 phases (tier A 3, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-BE) · [full JSON](https://data.orchid-project.org/phases/systems/AG-BE.json) · [Ag–Be system page](https://data.orchid-project.org/systems/AG-BE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-BE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Be system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG3BE8_C15](#phase-ag-be-ag3be8-c15); _phase:ag-be:ag3be8-c15_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1053.15–1260.09 K, x(Be) 0.73–0.73 | 0 | 1 |
| [BCC_A2](#phase-ag-be-bcc-a2); _phase:ag-be:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1520.5–2499.25 K, x(Be) 0.9971–1 | 0 | 1 |
| [FCC_A1](#phase-ag-be-fcc-a1); _phase:ag-be:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1246.71 K, x(Be) 0–0.00532 | 0 | 1 |
| [HCP_A3](#phase-ag-be-hcp-a3); _phase:ag-be:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1555.5 K, x(Be) 0.99729–1 | 0 | 1 |
| [LIQUID](#phase-ag-be-liquid); _phase:ag-be:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1146.71–2500 K, x(Be) 0–1 | 0 | 1 |

## AG3BE8_C15 (Ag–Be)

- Id: `phase:ag-be:ag3be8-c15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C15; stoichiometry_contradicts_C15:AgBe-04Kor-LB.tdb
- Candidate (name_token): Cu2Mg · C15 · cF24 · Fd-3m (227) — Strukturbericht/word 'C15' in the TDB name
- Candidate (sgte_mmc2): Cu2Mg · C15 · cF24 · Fd-3m (227) — Hallstedt 2025 mmc2 row for AG3BE8_C15: Ag3Be8
- Candidate (tdb_comment): Cu2Mg · cF24 · Fd-3m — AgBe-04Kor-LB.tdb: 'Prototype Cu2Mg (cF24, Fd-3m)'
- Stoichiometry: Ag 0.2700, Be 0.7300
- Stability: stable in 1 of 1 calculated diagram(s): 1053.15–1260.09 K, x(Be) 0.73–0.73
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-be:ag3be8-c15)

Names (2): _corpus: _corpus:phase:ag-be:ag3be8-c15  
_tdb: _tdb:AgBe-04Kor-LB.tdb:AG3BE8_C15  


### TDB models of AG3BE8_C15 (1): PHASE and CONSTITUENT statements as written

[AgBe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBe-04Kor-LB.tdb): AG3BE8_C15, type code %, sha256 `14a24d717fb3deb7…`

~~~~text
42: PHASE AG3BE8_C15 % 2 2.97 8.03 !
43: CONST AG3BE8_C15 : AG : BE : !
~~~~

## BCC_A2 (Ag–Be)

- Id: `phase:ag-be:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1520.5–2499.25 K, x(Be) 0.9971–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-be:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-be:bcc-a2  
_tdb: _tdb:AgBe-04Kor-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgBe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBe-04Kor-LB.tdb): BCC_A2, type code %B, sha256 `14a24d717fb3deb7…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AG BE% : VA : !
~~~~

## FCC_A1 (Ag–Be)

- Id: `phase:ag-be:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1246.71 K, x(Be) 0–0.00532
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-be:fcc-a1)

Names (2): _corpus: _corpus:phase:ag-be:fcc-a1  
_tdb: _tdb:AgBe-04Kor-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgBe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBe-04Kor-LB.tdb): FCC_A1, type code %A, sha256 `14a24d717fb3deb7…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AG% BE : VA : !
~~~~

## HCP_A3 (Ag–Be)

- Id: `phase:ag-be:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1555.5 K, x(Be) 0.99729–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-be:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-be:hcp-a3  
_tdb: _tdb:AgBe-04Kor-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgBe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBe-04Kor-LB.tdb): HCP_A3, type code %A, sha256 `14a24d717fb3deb7…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AG BE% : VA : !
~~~~

## LIQUID (Ag–Be)

- Id: `phase:ag-be:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1146.71–2500 K, x(Be) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-be:liquid)

Names (2): _corpus: _corpus:phase:ag-be:liquid  
_tdb: _tdb:AgBe-04Kor-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgBe-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBe-04Kor-LB.tdb): LIQUID, type code %, sha256 `14a24d717fb3deb7…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AG BE : !
~~~~

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
