# Br–Ca phases

> Br–Ca system: 7 phases (tier A 4, liquid 2, gas 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BR-CA.html · Markdown: https://data.orchid-project.org/phases/pages/BR-CA.md

7 phases (tier A 4, liquid 2, gas 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BR-CA) · [full JSON](https://data.orchid-project.org/phases/systems/BR-CA.json) · [Markdown](https://data.orchid-project.org/phases/pages/BR-CA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Br–Ca system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-br-ca-bcc-a2); _phase:br-ca:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1115–2020 K, x(Br) 0–0 | 0 | 1 |
| [CABR2_C18](#phase-br-ca-cabr2-c18); _phase:br-ca:cabr2-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–710 K, x(Br) 0.66667–0.66667 | 0 | 1 |
| [FCC_A1](#phase-br-ca-fcc-a1); _phase:br-ca:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–710 K, x(Br) 0–0 | 0 | 1 |
| [GAS](#phase-br-ca-gas); _phase:br-ca:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 332.66–2500 K, x(Br) 0–1 | 0 | 1 |
| [HCP_A3](#phase-br-ca-hcp-a3); _phase:br-ca:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-br-ca-ion); _phase:br-ca:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1023.82–2107.36 K, x(Br) 0–0.66667 | 0 | 1 |
| [LIQUID](#phase-br-ca-liquid); _phase:br-ca:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Br) 0.94797–1 | 0 | 1 |

## BCC_A2 (Br–Ca)

- Id: `phase:br-ca:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1115–2020 K, x(Br) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:br-ca:bcc-a2)

Names (2): _corpus: _corpus:phase:br-ca:bcc-a2  
_tdb: _tdb:CaBr-92Sta.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaBr-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaBr-92Sta.tdb): BCC_A2, type code %B, sha256 `69998457925c61ce…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : CA : VA : !
~~~~

## CABR2_C18 (Br–Ca)

- Id: `phase:br-ca:cabr2-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–710 K, x(Br) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:br-ca:cabr2-c18)

Names (2): _corpus: _corpus:phase:br-ca:cabr2-c18  
_tdb: _tdb:CaBr-92Sta.tdb:CABR2_C18  


### TDB models of CABR2_C18 (1): PHASE and CONSTITUENT statements as written

[CaBr-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaBr-92Sta.tdb): CABR2_C18, type code %, sha256 `69998457925c61ce…`

~~~~text
61: PHASE CABR2_C18:I % 2 1 2 !
62: CONST CABR2_C18:I : CA+2 : BR-1 : !
~~~~

## FCC_A1 (Br–Ca)

- Id: `phase:br-ca:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–710 K, x(Br) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:br-ca:fcc-a1)

Names (2): _corpus: _corpus:phase:br-ca:fcc-a1  
_tdb: _tdb:CaBr-92Sta.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaBr-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaBr-92Sta.tdb): FCC_A1, type code %A, sha256 `69998457925c61ce…`

~~~~text
46: PHASE FCC_A1 %A 2 1 1 !
47: CONST FCC_A1 : CA : VA : !
~~~~

## GAS (Br–Ca)

- Id: `phase:br-ca:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 332.66–2500 K, x(Br) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:br-ca:gas)

Names (2): _corpus: _corpus:phase:br-ca:gas  
_tdb: _tdb:CaBr-92Sta.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CaBr-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaBr-92Sta.tdb): GAS, type code %, sha256 `69998457925c61ce…`

~~~~text
64: PHASE GAS:G % 1 1 !
65: CONST GAS:G : CA CA2 CABR CABR2 BR BR2 : !
~~~~

## HCP_A3 (Br–Ca)

- Id: `phase:br-ca:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:br-ca:hcp-a3)

Names (2): _corpus: _corpus:phase:br-ca:hcp-a3  
_tdb: _tdb:CaBr-92Sta.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaBr-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaBr-92Sta.tdb): HCP_A3, type code %A, sha256 `69998457925c61ce…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : CA : VA : !
~~~~

## ION (Br–Ca)

- Id: `phase:br-ca:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1023.82–2107.36 K, x(Br) 0–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:br-ca:ion)

Names (2): _corpus: _corpus:phase:br-ca:ion  
_tdb: _tdb:CaBr-92Sta.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CaBr-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaBr-92Sta.tdb): ION, type code %, sha256 `69998457925c61ce…`

~~~~text
38: PHASE ION:Y % 2 1 1 !
39: CONST ION:Y : CA+2 : BR-1 VA : !
~~~~

## LIQUID (Br–Ca)

- Id: `phase:br-ca:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Br) 0.94797–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:br-ca:liquid)

Names (2): _corpus: _corpus:phase:br-ca:liquid  
_tdb: _tdb:CaBr-92Sta.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaBr-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaBr-92Sta.tdb): LIQUID, type code %, sha256 `69998457925c61ce…`

~~~~text
41: PHASE LIQUID:L % 1 1 !
42: CONST LIQUID:L : CA BR2 : !
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
