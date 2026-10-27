# Ca–F phases

> Ca–F system: 7 phases (tier A 4, liquid 2, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-F.html · Markdown: https://data.orchid-project.org/phases/pages/CA-F.md

7 phases (tier A 4, liquid 2, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-F) · [full JSON](https://data.orchid-project.org/phases/systems/CA-F.json) · [Ca–F system page](https://data.orchid-project.org/systems/CA-F.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-F.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–F system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-f-bcc-a2); _phase:ca-f:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 990.43–1115 K, x(F) 0–0 | 0 | 1 |
| [CAF2_C1](#phase-ca-f-caf2-c1); _phase:ca-f:caf2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1548.93 K, x(F) 0.66667–0.66667 | 0 | 1 |
| [FCC_A1](#phase-ca-f-fcc-a1); _phase:ca-f:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–545 K, x(F) 0–0 | 0 | 1 |
| [GAS](#phase-ca-f-gas); _phase:ca-f:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(F) 0–1 | 0 | 1 |
| [HCP_A3](#phase-ca-f-hcp-a3); _phase:ca-f:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-ca-f-ion); _phase:ca-f:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1095.43–2500 K, x(F) 0–0.66667 | 0 | 1 |
| [LIQUID](#phase-ca-f-liquid); _phase:ca-f:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |

## BCC_A2 (Ca–F)

- Id: `phase:ca-f:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 990.43–1115 K, x(F) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-f:bcc-a2)

Names (2): _corpus: _corpus:phase:ca-f:bcc-a2  
_tdb: _tdb:CaF-92Sta.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaF-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaF-92Sta.tdb): BCC_A2, type code %B, sha256 `29aa8dd5819e979a…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : CA : VA : !
~~~~

## CAF2_C1 (Ca–F)

- Id: `phase:ca-f:caf2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1548.93 K, x(F) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-f:caf2-c1)

Names (2): _corpus: _corpus:phase:ca-f:caf2-c1  
_tdb: _tdb:CaF-92Sta.tdb:CAF2_C1  


### TDB models of CAF2_C1 (1): PHASE and CONSTITUENT statements as written

[CaF-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaF-92Sta.tdb): CAF2_C1, type code %, sha256 `29aa8dd5819e979a…`

~~~~text
58: PHASE CAF2_C1:I % 2 1 2 !
59: CONST CAF2_C1:I : CA+2 : F-1 : !
~~~~

## FCC_A1 (Ca–F)

- Id: `phase:ca-f:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–545 K, x(F) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-f:fcc-a1)

Names (2): _corpus: _corpus:phase:ca-f:fcc-a1  
_tdb: _tdb:CaF-92Sta.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaF-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaF-92Sta.tdb): FCC_A1, type code %A, sha256 `29aa8dd5819e979a…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : CA : VA : !
~~~~

## GAS (Ca–F)

- Id: `phase:ca-f:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(F) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-f:gas)

Names (2): _corpus: _corpus:phase:ca-f:gas  
_tdb: _tdb:CaF-92Sta.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CaF-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaF-92Sta.tdb): GAS, type code %, sha256 `29aa8dd5819e979a…`

~~~~text
61: PHASE GAS:G % 1 1 !
62: CONST GAS:G : CA CA2 CAF CAF2 F F2 : !
~~~~

## HCP_A3 (Ca–F)

- Id: `phase:ca-f:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-f:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-f:hcp-a3  
_tdb: _tdb:CaF-92Sta.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaF-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaF-92Sta.tdb): HCP_A3, type code %A, sha256 `29aa8dd5819e979a…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : CA : VA : !
~~~~

## ION (Ca–F)

- Id: `phase:ca-f:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1095.43–2500 K, x(F) 0–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-f:ion)

Names (2): _corpus: _corpus:phase:ca-f:ion  
_tdb: _tdb:CaF-92Sta.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CaF-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaF-92Sta.tdb): ION, type code %, sha256 `29aa8dd5819e979a…`

~~~~text
35: PHASE ION:Y % 2 1 1 !
36: CONST ION:Y : CA+2 : F-1 VA : !
~~~~

## LIQUID (Ca–F)

- Id: `phase:ca-f:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Ca 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-f:liquid)

Names (2): _corpus: _corpus:phase:ca-f:liquid  
_tdb: _tdb:CaF-92Sta.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaF-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaF-92Sta.tdb): LIQUID, type code %, sha256 `29aa8dd5819e979a…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : CA : !
~~~~

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
