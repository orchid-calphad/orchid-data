# B–N phases

> B–N system: 9 phases (tier A 1, liquid 2, gas 2, needs_review 4); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-N.html · Markdown: https://data.orchid-project.org/phases/pages/B-N.md

9 phases (tier A 1, liquid 2, gas 2, needs_review 4); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-N) · [full JSON](https://data.orchid-project.org/phases/systems/B-N.json) · [B–N system page](https://data.orchid-project.org/systems/B-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–N system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-n-b-alpha-rhombo); _phase:b-n:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(N) 0–0 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-n-b-beta-rhombo); _phase:b-n:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2376.26 K, x(N) 0–0 | 0 | 2 |
| [BN_B3](#phase-b-n-bn-b3); _phase:b-n:bn-b3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1855.12 K, x(N) 0.5–0.5 | 0 | 1 |
| [BN_B4](#phase-b-n-bn-b4); _phase:b-n:bn-b4_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BN_BK](#phase-b-n-bn-bk); _phase:b-n:bn-bk_ | BN · B_k · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1855.12–2777.04 K, x(N) 0.5–0.5 | 0 | 2 |
| [GAS](#phase-b-n-gas); _phase:b-n:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300.12–4000 K, x(N) 0.64279–1 | 0 | 2 |
| [ION](#phase-b-n-ion); _phase:b-n:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2344.76–4000 K, x(N) 0–0.01663 | 0 | 1 |
| [LIQUID](#phase-b-n-liquid); _phase:b-n:liquid_ | liquid | liquid | no calculated diagram | 0 | 1 |
| [N2GAS](#phase-b-n-n2gas); _phase:b-n:n2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2090.12 K, x(N) 1–1 | 0 | 2 |

## ALPHA_RHOMBO_B (B–N)

- Id: `phase:b-n:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — BN-19Sri.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(N) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-n:b-alpha-rhombo  
_tdb: _tdb:BN-19Sri.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): ALPHA_RHOMBO_B, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
40: PHASE ALPHA_RHOMBO_B % 1 1 !
41: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–N)

- Id: `phase:b-n:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BN-19Sri.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BN-96Kas-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2376.26 K, x(N) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:b-beta-rhombo)

Names (3): _corpus: _corpus:phase:b-n:b-beta-rhombo  
_tdb: _tdb:BN-19Sri.tdb:BETA_RHOMBO_B, tdb:BN-96Kas-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): BETA_RHOMBO_B, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
35: PHASE BETA_RHOMBO_B % 1 1 !
36: CONST BETA_RHOMBO_B : B : !
~~~~

[BN-96Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-96Kas-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `096fb32cd247bf91…`

~~~~text
39: PHASE BETA_RHOMBO_B % 1 1 !
40: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## BN_B3 (B–N)

- Id: `phase:b-n:bn-b3`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; structure_token_is_also_a_formula
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP BN at x(N)=0.5000
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD B1 N1 at x(N)=0.5000
- Candidate (sgte_mmc2): ZnS (sphalerite) · B3 · cF8 · F-43m (216) — Hallstedt 2025 mmc2 row for BN_B3: c-BN (metastable)
- Candidate (tdb_comment): ZnS 3C · cF8 · F-43m — BN-19Sri.tdb: 'Prototype ZnS 3C (cF8, F-43m), metastable'
- Stoichiometry: B 0.5000, N 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1855.12 K, x(N) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:bn-b3)

Names (2): _corpus: _corpus:phase:b-n:bn-b3  
_tdb: _tdb:BN-19Sri.tdb:BN_B3  


### TDB models of BN_B3 (1): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): BN_B3, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
50: PHASE BN_B3 % 2 1 1 !
51: CONST BN_B3 : B : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## BN_B4 (B–N)

- Id: `phase:b-n:bn-b4`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; structure_token_is_also_a_formula
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP BN at x(N)=0.5000
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD B1 N1 at x(N)=0.5000
- Candidate (sgte_mmc2): ZnS (wurtzite) · B4 · hP4 · P6_3mc (186) — Hallstedt 2025 mmc2 row for BN_B4: w-BN (metastable)
- Candidate (tdb_comment): ZnS 2H · hP4 · P6_3mc — BN-19Sri.tdb: 'Prototype ZnS 2H (hP4, P6_3mc), metastable'
- Stoichiometry: B 0.5000, N 0.5000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:bn-b4)

Names (2): _corpus: _corpus:phase:b-n:bn-b4  
_tdb: _tdb:BN-19Sri.tdb:BN_B4  


### TDB models of BN_B4 (1): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): BN_B4, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
55: PHASE BN_B4 % 2 1 1 !
56: CONST BN_B4 : B : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## BN_BK (B–N)

- Id: `phase:b-n:bn-bk`; status `assigned`
- Structure: BN · B_k · hP4 · P6_3/mmc (194); type `st:b-k-bn-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.5000, N 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 1855.12–2777.04 K, x(N) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:bn-bk)

Names (3): _corpus: _corpus:phase:b-n:bn-bk  
_tdb: _tdb:BN-19Sri.tdb:BN_BK, tdb:BN-96Kas-LB.tdb:BN_BK  


### TDB models of BN_BK (2): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): BN_BK, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
45: PHASE BN_BK % 2 1 1 !
46: CONST BN_BK : B : N : !
~~~~

[BN-96Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-96Kas-LB.tdb): BN_BK, type code %, sha256 `096fb32cd247bf91…`

~~~~text
44: PHASE BN_BK % 2 1 1 !
45: CONST BN_BK : B : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## GAS (B–N)

- Id: `phase:b-n:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.12–4000 K, x(N) 0.64279–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:gas)

Names (3): _corpus: _corpus:phase:b-n:gas  
_tdb: _tdb:BN-19Sri.tdb:GAS, tdb:BN-96Kas-LB.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): GAS, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : B B2 BN N N2 N3 : !
~~~~

[BN-96Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-96Kas-LB.tdb): GAS, type code %, sha256 `096fb32cd247bf91…`

~~~~text
47: PHASE GAS:G % 1 1 !
48: CONST GAS:G : B B2 BN N N2 N3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## ION (B–N)

- Id: `phase:b-n:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2344.76–4000 K, x(N) 0–0.01663
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:ion)

Names (2): _corpus: _corpus:phase:b-n:ion  
_tdb: _tdb:BN-19Sri.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): ION, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
30: PHASE ION:Y % 2 1 1 !
31: CONST ION:Y : B+3 : VA BN N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## LIQUID (B–N)

- Id: `phase:b-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:liquid)

Names (2): _corpus: _corpus:phase:b-n:liquid  
_tdb: _tdb:BN-96Kas-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BN-96Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-96Kas-LB.tdb): LIQUID, type code %, sha256 `096fb32cd247bf91…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : B N : !
~~~~

## N2GAS (B–N)

- Id: `phase:b-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2090.12 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-n:n2gas)

Names (3): _corpus: _corpus:phase:b-n:n2gas  
_tdb: _tdb:BN-19Sri.tdb:N2GAS, tdb:BN-96Kas-LB.tdb:N2GAS  


### TDB models of N2GAS (2): PHASE and CONSTITUENT statements as written

[BN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-19Sri.tdb): N2GAS, type code %, sha256 `d5a7851e9945cdc0…`

~~~~text
61: PHASE N2GAS % 1 1 !
62: CONST N2GAS : N2 : !
~~~~

[BN-96Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BN-96Kas-LB.tdb): N2GAS, type code %, sha256 `096fb32cd247bf91…`

~~~~text
50: PHASE N2GAS % 1 1 !
51: CONST N2GAS : N2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

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
