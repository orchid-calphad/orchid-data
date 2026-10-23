# Li–N phases

> Li–N system: 7 phases (tier A 3, tier B 1, liquid 1, gas 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LI-N.html · Markdown: https://data.orchid-project.org/phases/pages/LI-N.md

7 phases (tier A 3, tier B 1, liquid 1, gas 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LI-N) · [full JSON](https://data.orchid-project.org/phases/systems/LI-N.json) · [Li–N system page](https://data.orchid-project.org/systems/LI-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/LI-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Li–N system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-li-n-bcc-a2); _phase:li-n:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1611.35 K, x(N) 0–0 | 0 | 1 |
| [FCC_A1](#phase-li-n-fcc-a1); _phase:li-n:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-li-n-gas); _phase:li-n:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 301.14–2500 K, x(N) 0–1 | 0 | 1 |
| [HCP_A3](#phase-li-n-hcp-a3); _phase:li-n:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LI3N](#phase-li-n-li3n); _phase:li-n:li3n_ | Li3N · hP4 · P6/mmm (191) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1081.92 K, x(N) 0.25–0.25 | 0 | 1 |
| [LIQUID](#phase-li-n-liquid); _phase:li-n:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 453.32–1616.12 K, x(N) 0–0.22069 | 0 | 1 |
| [N2GAS](#phase-li-n-n2gas); _phase:li-n:n2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–735 K, x(N) 1–1 | 0 | 1 |

## BCC_A2 (Li–N)

- Id: `phase:li-n:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1611.35 K, x(N) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-n:bcc-a2)

Names (2): _corpus: _corpus:phase:li-n:bcc-a2  
_tdb: _tdb:LiN-05Fra-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LiN-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiN-05Fra-LB.tdb): BCC_A2, type code %B, sha256 `7dd01471c6b331e6…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : LI : N VA% : !
~~~~

## FCC_A1 (Li–N)

- Id: `phase:li-n:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-n:fcc-a1)

Names (2): _corpus: _corpus:phase:li-n:fcc-a1  
_tdb: _tdb:LiN-05Fra-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LiN-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiN-05Fra-LB.tdb): FCC_A1, type code %A, sha256 `7dd01471c6b331e6…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : LI : N VA% : !
~~~~

## GAS (Li–N)

- Id: `phase:li-n:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.14–2500 K, x(N) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-n:gas)

Names (2): _corpus: _corpus:phase:li-n:gas  
_tdb: _tdb:LiN-05Fra-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[LiN-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiN-05Fra-LB.tdb): GAS, type code %, sha256 `7dd01471c6b331e6…`

~~~~text
51: PHASE GAS:G % 1 1 !
52: CONST GAS:G : LI LI2 N2 : !
~~~~

## HCP_A3 (Li–N)

- Id: `phase:li-n:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-n:hcp-a3)

Names (2): _corpus: _corpus:phase:li-n:hcp-a3  
_tdb: _tdb:LiN-05Fra-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LiN-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiN-05Fra-LB.tdb): HCP_A3, type code %, sha256 `7dd01471c6b331e6…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : LI : N VA% : !
~~~~

## LI3N (Li–N)

- Id: `phase:li-n:li3n`; status `assigned`
- Structure: Li3N · hP4 · P6/mmm (191); type `st:li3n-hp4`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Li 0.7500, N 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1081.92 K, x(N) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-n:li3n)

Names (4): _corpus: _corpus:phase:li-n:li3n  
_mp: _mp:mp-aaaaadip  
_oqmd: _oqmd:oqmd-6431  
_tdb: _tdb:LiN-05Fra-LB.tdb:LI3N  


### TDB models of LI3N (1): PHASE and CONSTITUENT statements as written

[LiN-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiN-05Fra-LB.tdb): LI3N, type code %, sha256 `7dd01471c6b331e6…`

~~~~text
45: PHASE LI3N % 2 3 1 !
46: CONST LI3N : LI : N : !
~~~~

## LIQUID (Li–N)

- Id: `phase:li-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 453.32–1616.12 K, x(N) 0–0.22069
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-n:liquid)

Names (2): _corpus: _corpus:phase:li-n:liquid  
_tdb: _tdb:LiN-05Fra-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LiN-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiN-05Fra-LB.tdb): LIQUID, type code %, sha256 `7dd01471c6b331e6…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : LI N : !
~~~~

## N2GAS (Li–N)

- Id: `phase:li-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–735 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-n:n2gas)

Names (2): _corpus: _corpus:phase:li-n:n2gas  
_tdb: _tdb:LiN-05Fra-LB.tdb:N2GAS  


### TDB models of N2GAS (1): PHASE and CONSTITUENT statements as written

[LiN-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiN-05Fra-LB.tdb): N2GAS, type code %, sha256 `7dd01471c6b331e6…`

~~~~text
48: PHASE N2GAS % 1 1 !
49: CONST N2GAS : N2 : !
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
