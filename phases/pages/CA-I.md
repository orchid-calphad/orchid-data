# Ca–I phases

> Ca–I system: 8 phases (tier A 4, liquid 2, gas 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-I.html · Markdown: https://data.orchid-project.org/phases/pages/CA-I.md

8 phases (tier A 4, liquid 2, gas 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-I) · [full JSON](https://data.orchid-project.org/phases/systems/CA-I.json) · [Ca–I system page](https://data.orchid-project.org/systems/CA-I.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-I.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–I system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-i-bcc-a2); _phase:ca-i:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CAI2_C6](#phase-ca-i-cai2-c6); _phase:ca-i:cai2-c6_ | CdI2 · C6 · hP3 · P-3m1 (164) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–665 K, x(I) 0.66667–0.66667 | 0 | 1 |
| [FCC_A1](#phase-ca-i-fcc-a1); _phase:ca-i:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–665 K, x(I) 0–0 | 0 | 1 |
| [GAS](#phase-ca-i-gas); _phase:ca-i:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1788.09–1795.49 K, x(I) 0–0.2952 | 0 | 1 |
| [HCP_A3](#phase-ca-i-hcp-a3); _phase:ca-i:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ORTHORHOMBIC_I](#phase-ca-i-i-orthorhombic); _phase:ca-i:i-orthorhombic_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–386.7 K, x(I) 1–1 | 0 | 1 |
| [ION](#phase-ca-i-ion); _phase:ca-i:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 386.06–1795.49 K, x(I) 0–1 | 0 | 1 |
| [LIQUID](#phase-ca-i-liquid); _phase:ca-i:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |

## BCC_A2 (Ca–I)

- Id: `phase:ca-i:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:bcc-a2)

Names (2): _corpus: _corpus:phase:ca-i:bcc-a2  
_tdb: _tdb:CaI-92Sta.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): BCC_A2, type code %B, sha256 `f96626f929260b85…`

~~~~text
50: PHASE BCC_A2 %B 2 1 3 !
51: CONST BCC_A2 : CA : VA : !
~~~~

## CAI2_C6 (Ca–I)

- Id: `phase:ca-i:cai2-c6`; status `assigned`
- Structure: CdI2 · C6 · hP3 · P-3m1 (164); type `st:c6-cdi2-hp3`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–665 K, x(I) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:cai2-c6)

Names (2): _corpus: _corpus:phase:ca-i:cai2-c6  
_tdb: _tdb:CaI-92Sta.tdb:CAI2_C6  


### TDB models of CAI2_C6 (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): CAI2_C6, type code %, sha256 `f96626f929260b85…`

~~~~text
65: PHASE CAI2_C6:I % 2 1 2 !
66: CONST CAI2_C6:I : CA+2 : I-1 : !
~~~~

## FCC_A1 (Ca–I)

- Id: `phase:ca-i:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–665 K, x(I) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:fcc-a1)

Names (2): _corpus: _corpus:phase:ca-i:fcc-a1  
_tdb: _tdb:CaI-92Sta.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): FCC_A1, type code %A, sha256 `f96626f929260b85…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : CA : VA : !
~~~~

## GAS (Ca–I)

- Id: `phase:ca-i:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1788.09–1795.49 K, x(I) 0–0.2952
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:gas)

Names (2): _corpus: _corpus:phase:ca-i:gas  
_tdb: _tdb:CaI-92Sta.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): GAS, type code %, sha256 `f96626f929260b85…`

~~~~text
68: PHASE GAS:G % 1 1 !
69: CONST GAS:G : CA CA2 CAI CAI2 I I2 : !
~~~~

## HCP_A3 (Ca–I)

- Id: `phase:ca-i:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-i:hcp-a3  
_tdb: _tdb:CaI-92Sta.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): HCP_A3, type code %A, sha256 `f96626f929260b85…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : CA : VA : !
~~~~

## ORTHORHOMBIC_I (Ca–I)

- Id: `phase:ca-i:i-orthorhombic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:ORTHORHOMBIC; no_structure_token
- Candidate (sgte_mmc2): I2 · A14 · oC8 · Cmce (64) — Hallstedt 2025 mmc2 row for ORTHORHOMBIC_I: I2
- Candidate (tdb_comment): I2 · oC8 · Cmce, A14 — CaI-92Sta.tdb: 'Prototype I2 (oC8, Cmce, A14)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–386.7 K, x(I) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:i-orthorhombic)

Names (2): _corpus: _corpus:phase:ca-i:i-orthorhombic  
_tdb: _tdb:CaI-92Sta.tdb:ORTHORHOMBIC_I  


### TDB models of ORTHORHOMBIC_I (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): ORTHORHOMBIC_I, type code %, sha256 `f96626f929260b85…`

~~~~text
60: PHASE ORTHORHOMBIC_I % 1 1 !
61: CONST ORTHORHOMBIC_I : I2 : !
~~~~

## ION (Ca–I)

- Id: `phase:ca-i:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 386.06–1795.49 K, x(I) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:ion)

Names (2): _corpus: _corpus:phase:ca-i:ion  
_tdb: _tdb:CaI-92Sta.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): ION, type code %, sha256 `f96626f929260b85…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : CA+2 : I-1 VA I2 : !
~~~~

## LIQUID (Ca–I)

- Id: `phase:ca-i:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-i:liquid)

Names (2): _corpus: _corpus:phase:ca-i:liquid  
_tdb: _tdb:CaI-92Sta.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaI-92Sta.tdb](https://orchid-project.org/data/databases/sgte-binary/CaI-92Sta.tdb): LIQUID, type code %, sha256 `f96626f929260b85…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : CA I2 : !
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
