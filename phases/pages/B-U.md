# B–U phases

> B–U system: 10 phases (tier A 7, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-U.html · Markdown: https://data.orchid-project.org/phases/pages/B-U.md

10 phases (tier A 7, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-U) · [full JSON](https://data.orchid-project.org/phases/systems/B-U.json) · [B–U system page](https://data.orchid-project.org/systems/B-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–U system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-b-u-a20-orthorhombic); _phase:b-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–942.02 K, x(B) 0–0 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-u-b-beta-rhombo); _phase:b-u:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2351.71 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-u-bcc-a2); _phase:b-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1048.99–3272.99 K, x(B) 0–0 | 0 | 1 |
| [FCC_A1](#phase-b-u-fcc-a1); _phase:b-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-u-hcp-a3); _phase:b-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-b-u-liquid); _phase:b-u:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1381.19–4000 K, x(B) 0–1 | 18 | 1 |
| [TETRAGONAL_U](#phase-b-u-u-tetragonal); _phase:b-u:u-tetragonal_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 942.02–1048.99 K, x(B) 0–0 | 0 | 1 |
| [UB12_D2F](#phase-b-u-ub12-d2f); _phase:b-u:ub12-d2f_ | UB12 · D2_f · cF52 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2457.96 K, x(B) 0.92308–0.92308 | 7 | 1 |
| [UB2_C32](#phase-b-u-ub2-c32); _phase:b-u:ub2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2670.95 K, x(B) 0.66667–0.66667 | 8 | 1 |
| [UB4_D1E](#phase-b-u-ub4-d1e); _phase:b-u:ub4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2722.24 K, x(B) 0.8–0.8 | 3 | 1 |

## ORTHORHOMBIC_A20 (B–U)

- Id: `phase:b-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–942.02 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:a20-orthorhombic)

Names (2): _corpus: _corpus:phase:b-u:a20-orthorhombic  
_tdb: _tdb:UB-01Che.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): ORTHORHOMBIC_A20, type code %, sha256 `6807da8a6672bb65…`

~~~~text
43: PHASE ORTHORHOMBIC_A20 % 1 1 !
44: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–U)

- Id: `phase:b-u:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — UB-01Che.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2351.71 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-u:b-beta-rhombo  
_tdb: _tdb:UB-01Che.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): BETA_RHOMBO_B, type code %, sha256 `6807da8a6672bb65…`

~~~~text
53: PHASE BETA_RHOMBO_B % 1 1 !
54: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## BCC_A2 (B–U)

- Id: `phase:b-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1048.99–3272.99 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:bcc-a2)

Names (2): _corpus: _corpus:phase:b-u:bcc-a2  
_tdb: _tdb:UB-01Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): BCC_A2, type code %B, sha256 `6807da8a6672bb65…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## FCC_A1 (B–U)

- Id: `phase:b-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:fcc-a1)

Names (2): _corpus: _corpus:phase:b-u:fcc-a1  
_tdb: _tdb:UB-01Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): FCC_A1, type code %A, sha256 `6807da8a6672bb65…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## HCP_A3 (B–U)

- Id: `phase:b-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:hcp-a3)

Names (2): _corpus: _corpus:phase:b-u:hcp-a3  
_tdb: _tdb:UB-01Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): HCP_A3, type code %A, sha256 `6807da8a6672bb65…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## LIQUID (B–U)

- Id: `phase:b-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1381.19–4000 K, x(B) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:liquid)

Names (3): _corpus: _corpus:phase:b-u:liquid  
_paper: _paper:10.1016/s0022-3115(00)00713-3:L  
_tdb: _tdb:UB-01Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): LIQUID, type code %, sha256 `6807da8a6672bb65…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : B U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_

## TETRAGONAL_U (B–U)

- Id: `phase:b-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UB-01Che.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stoichiometry: U 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 942.02–1048.99 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:u-tetragonal)

Names (2): _corpus: _corpus:phase:b-u:u-tetragonal  
_tdb: _tdb:UB-01Che.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): TETRAGONAL_U, type code %, sha256 `6807da8a6672bb65…`

~~~~text
48: PHASE TETRAGONAL_U % 1 1 !
49: CONST TETRAGONAL_U : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## UB12_D2F (B–U)

- Id: `phase:b-u:ub12-d2f`; status `assigned`
- Structure: UB12 · D2_f · cF52 · Fm-3m (225); type `st:d2-f-ub12-cf52`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabhal and oqmd-4445, space group 225
- Stoichiometry: B 0.9231, U 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–2457.96 K, x(B) 0.92308–0.92308
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:ub12-d2f)

Names (5): _corpus: _corpus:phase:b-u:ub12-d2f  
_mp: _mp:mp-aaaabhal  
_oqmd: _oqmd:oqmd-4445  
_paper: _paper:10.1016/s0022-3115(00)00713-3:UB12  
_tdb: _tdb:UB-01Che.tdb:UB12_D2F  


### TDB models of UB12_D2F (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): UB12_D2F, type code %, sha256 `6807da8a6672bb65…`

~~~~text
68: PHASE UB12_D2F % 2 1 12 !
69: CONST UB12_D2F : U : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_

## UB2_C32 (B–U)

- Id: `phase:b-u:ub2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacgg and oqmd-646133, space group 191
- Stoichiometry: B 0.6667, U 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2670.95 K, x(B) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:ub2-c32)

Names (5): _corpus: _corpus:phase:b-u:ub2-c32  
_mp: _mp:mp-aaaaacgg  
_oqmd: _oqmd:oqmd-646133  
_paper: _paper:10.1016/s0022-3115(00)00713-3:UB2  
_tdb: _tdb:UB-01Che.tdb:UB2_C32  


### TDB models of UB2_C32 (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): UB2_C32, type code %, sha256 `6807da8a6672bb65…`

~~~~text
58: PHASE UB2_C32 % 2 1 2 !
59: CONST UB2_C32 : U : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_

## UB4_D1E (B–U)

- Id: `phase:b-u:ub4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaaxv and oqmd-4686, space group 127
- Stoichiometry: B 0.8000, U 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2722.24 K, x(B) 0.8–0.8
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-u:ub4-d1e)

Names (5): _corpus: _corpus:phase:b-u:ub4-d1e  
_mp: _mp:mp-aaaaaaxv  
_oqmd: _oqmd:oqmd-4686  
_paper: _paper:10.1016/s0022-3115(00)00713-3:UB4  
_tdb: _tdb:UB-01Che.tdb:UB4_D1E  


### TDB models of UB4_D1E (1): PHASE and CONSTITUENT statements as written

[UB-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UB-01Che.tdb): UB4_D1E, type code %, sha256 `6807da8a6672bb65…`

~~~~text
63: PHASE UB4_D1E % 2 1 4 !
64: CONST UB4_D1E : U : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
