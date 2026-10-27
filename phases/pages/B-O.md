# B–O phases

> B–O system: 7 phases (tier B 1, tier C 1, liquid 1, gas 2, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-O.html · Markdown: https://data.orchid-project.org/phases/pages/B-O.md

7 phases (tier B 1, tier C 1, liquid 1, gas 2, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-O) · [full JSON](https://data.orchid-project.org/phases/systems/B-O.json) · [B–O system page](https://data.orchid-project.org/systems/B-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–O system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-o-b-alpha-rhombo); _phase:b-o:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(O) 0–0 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-o-b-beta-rhombo); _phase:b-o:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2347.99 K, x(O) 0–0 | 0 | 1 |
| [B2O3](#phase-b-o-b2o3); _phase:b-o:b2o3_ | B2O3 · hP15 · P3_121 (152) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–723 K, x(O) 0.6–0.6 | 1 | 1 |
| [B6O](#phase-b-o-b6o); _phase:b-o:b6o_ | B6P · hR14 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1060.3 K, x(O) 0.14286–0.14286 | 0 | 1 |
| [GAS](#phase-b-o-gas); _phase:b-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300.5–4000 K, x(O) 0.317–1 | 0 | 1 |
| [LIQUID](#phase-b-o-liquid); _phase:b-o:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 723–4000 K, x(O) 0–0.6 | 1 | 1 |
| [O2GAS](#phase-b-o-o2gas); _phase:b-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–1128 K, x(O) 1–1 | 0 | 1 |

## ALPHA_RHOMBO_B (B–O)

- Id: `phase:b-o:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — BO-23Pha.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-o:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-o:b-alpha-rhombo  
_tdb: _tdb:BO-23Pha.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[BO-23Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb): ALPHA_RHOMBO_B, type code %, sha256 `52cca70a9ed43da1…`

~~~~text
42: PHASE ALPHA_RHOMBO_B % 1 1 !
43: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–O)

- Id: `phase:b-o:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BO-23Pha.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2347.99 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-o:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-o:b-beta-rhombo  
_tdb: _tdb:BO-23Pha.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[BO-23Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb): BETA_RHOMBO_B, type code %, sha256 `52cca70a9ed43da1…`

~~~~text
47: PHASE BETA_RHOMBO_B % 1 1 !
48: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023).  
_assessment that models this phase_

## B2O3 (B–O)

- Id: `phase:b-o:b2o3`; status `assigned`
- Structure: B2O3 · hP15 · P3_121 (152); type `st:b2o3-hp15`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: B 0.4000, O 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–723 K, x(O) 0.6–0.6
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-o:b2o3)

Names (5): _corpus: _corpus:phase:b-o:b2o3  
_mp: _mp:mp-aaaaaalu  
_oqmd: _oqmd:oqmd-9107  
_paper: _paper:10.1111/jace.18958:B2O3  
_tdb: _tdb:BO-23Pha.tdb:B2O3  


### TDB models of B2O3 (1): PHASE and CONSTITUENT statements as written

[BO-23Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb): B2O3, type code %, sha256 `52cca70a9ed43da1…`

~~~~text
57: PHASE B2O3 % 2 2 3 !
58: CONST B2O3 : B : O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023).  
_assessment that models this phase; reports values for this phase_

## B6O (B–O)

- Id: `phase:b-o:b6o`; status `assigned`
- Structure: B6P · hR14 · R-3m (166); type `st:b6p-hr14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.8571, O 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–1060.3 K, x(O) 0.14286–0.14286
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-o:b6o)

Names (2): _corpus: _corpus:phase:b-o:b6o  
_tdb: _tdb:BO-23Pha.tdb:B6O  


### TDB models of B6O (1): PHASE and CONSTITUENT statements as written

[BO-23Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb): B6O, type code %, sha256 `52cca70a9ed43da1…`

~~~~text
52: PHASE B6O % 2 6 1 !
53: CONST B6O : B : O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023).  
_assessment that models this phase_

## GAS (B–O)

- Id: `phase:b-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.5–4000 K, x(O) 0.317–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-o:gas)

Names (2): _corpus: _corpus:phase:b-o:gas  
_tdb: _tdb:BO-23Pha.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[BO-23Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb): GAS, type code %, sha256 `52cca70a9ed43da1…`

~~~~text
63: PHASE GAS:G % 1 1 !
64: CONST GAS:G : B B2 BO BO2 B2O B2O2 B2O3 O O2 O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023).  
_assessment that models this phase_

## LIQUID (B–O)

- Id: `phase:b-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 723–4000 K, x(O) 0–0.6
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-o:liquid)

Names (3): _corpus: _corpus:phase:b-o:liquid  
_paper: _paper:10.1111/jace.18958:liquid  
_tdb: _tdb:BO-23Pha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BO-23Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb): LIQUID, type code %, sha256 `52cca70a9ed43da1…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : B B2O3 O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023).  
_assessment that models this phase; reports values for this phase_

## O2GAS (B–O)

- Id: `phase:b-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1128 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-o:o2gas)

Names (2): _corpus: _corpus:phase:b-o:o2gas  
_tdb: _tdb:BO-23Pha.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[BO-23Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb): O2GAS, type code %, sha256 `52cca70a9ed43da1…`

~~~~text
60: PHASE O2GAS % 1 1 !
61: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023).  
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
