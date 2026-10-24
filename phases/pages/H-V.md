# H–V phases

> H–V system: 10 phases (tier A 4, liquid 1, gas 2, needs_review 3); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-V.html · Markdown: https://data.orchid-project.org/phases/pages/H-V.md

10 phases (tier A 4, liquid 1, gas 2, needs_review 3); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-V) · [full JSON](https://data.orchid-project.org/phases/systems/H-V.json) · [H–V system page](https://data.orchid-project.org/systems/H-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–V system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-v-bcc-a2); _phase:h-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2188.28 K, x(H) 0–0.42255 | 0 | 1 |
| [FCC_A1](#phase-h-v-fcc-a1); _phase:h-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-h-v-gas); _phase:h-v:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300.25–4000 K, x(H) 0–1 | 0 | 1 |
| [H2GAS](#phase-h-v-h2gas); _phase:h-v:h2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–1092.75 K, x(H) 1–1 | 0 | 1 |
| [HCP_A3](#phase-h-v-hcp-a3); _phase:h-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-h-v-liquid); _phase:h-v:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2183–3757.23 K, x(H) 0–0.00508 | 0 | 1 |
| [V3H2](#phase-h-v-v3h2); _phase:h-v:v3h2_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [VH_BETA_2](#phase-h-v-vh-2-beta); _phase:h-v:vh-2-beta_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [VH_BETA_ORD](#phase-h-v-vh-beta-ord); _phase:h-v:vh-beta-ord_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–467.32 K, x(H) 0.29435–0.48121 | 0 | 1 |
| [VH2_C1](#phase-h-v-vh2-c1); _phase:h-v:vh2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 2 | 1 |

## BCC_A2 (H–V)

- Id: `phase:h-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2188.28 K, x(H) 0–0.42255
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:bcc-a2)

Names (2): _corpus: _corpus:phase:h-v:bcc-a2  
_tdb: _tdb:VH-08Uki.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): BCC_A2, type code %B, sha256 `0027aaa295da99fa…`

~~~~text
40: PHASE BCC_A2 %B 2 1 6 !
41: CONST BCC_A2 : V : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## FCC_A1 (H–V)

- Id: `phase:h-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:fcc-a1)

Names (2): _corpus: _corpus:phase:h-v:fcc-a1  
_tdb: _tdb:VH-08Uki.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): FCC_A1, type code %A, sha256 `0027aaa295da99fa…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : V : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## GAS (H–V)

- Id: `phase:h-v:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.25–4000 K, x(H) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:gas)

Names (2): _corpus: _corpus:phase:h-v:gas  
_tdb: _tdb:VH-08Uki.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): GAS, type code %, sha256 `0027aaa295da99fa…`

~~~~text
69: PHASE GAS:G % 1 1 !
70: CONST GAS:G : H H2 V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## H2GAS (H–V)

- Id: `phase:h-v:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1092.75 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:h2gas)

Names (2): _corpus: _corpus:phase:h-v:h2gas  
_tdb: _tdb:VH-08Uki.tdb:H2GAS  


### TDB models of H2GAS (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): H2GAS, type code %, sha256 `0027aaa295da99fa…`

~~~~text
72: PHASE H2GAS % 1 1 !
73: CONST H2GAS : H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## HCP_A3 (H–V)

- Id: `phase:h-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:hcp-a3)

Names (2): _corpus: _corpus:phase:h-v:hcp-a3  
_tdb: _tdb:VH-08Uki.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): HCP_A3, type code %A, sha256 `0027aaa295da99fa…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : V : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## LIQUID (H–V)

- Id: `phase:h-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2183–3757.23 K, x(H) 0–0.00508
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:liquid)

Names (2): _corpus: _corpus:phase:h-v:liquid  
_tdb: _tdb:VH-08Uki.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): LIQUID, type code %, sha256 `0027aaa295da99fa…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : H V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## V3H2 (H–V)

- Id: `phase:h-v:v3h2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (V3H2) — Hallstedt 2025 mmc2 row for V3H2: V3H2
- Stoichiometry: H 0.4000, V 0.6000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:v3h2)

Names (2): _corpus: _corpus:phase:h-v:v3h2  
_tdb: _tdb:VH-08Uki.tdb:V3H2  


### TDB models of V3H2 (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): V3H2, type code %, sha256 `0027aaa295da99fa…`

~~~~text
61: PHASE V3H2 % 2 3 2 !
62: CONST V3H2 : V : H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## VH_BETA_2 (H–V)

- Id: `phase:h-v:vh-2-beta`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:2; no_structure_token
- Candidate (sgte_mmc2): V2H · tI56 · I4_1/amd (141) — Hallstedt 2025 mmc2 row for VH_BETA_2: VH-beta-2 (disordered)
- Candidate (tdb_comment): V2H · tI56 · I4_1/amd — VH-08Uki.tdb: 'Prototype V2H (tI56, I4_1/amd), beta-2'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:vh-2-beta)

Names (2): _corpus: _corpus:phase:h-v:vh-2-beta  
_tdb: _tdb:VH-08Uki.tdb:VH_BETA_2  


### TDB models of VH_BETA_2 (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): VH_BETA_2, type code %, sha256 `0027aaa295da99fa…`

~~~~text
51: PHASE VH_BETA_2 % 2 1 1 !
52: CONST VH_BETA_2 : H% VA : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## VH_BETA_ORD (H–V)

- Id: `phase:h-v:vh-beta-ord`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:ORD; no_structure_token
- Candidate (sgte_mmc2): V2H · mC6 · C2/m (12) — Hallstedt 2025 mmc2 row for VH_BETA_ORD: VH-beta-1 (ordered)
- Candidate (tdb_comment): V2H · mC6 · C2/m — VH-08Uki.tdb: 'Prototype V2H (mC6, C2/m), beta-1'
- Stability: stable in 1 of 1 calculated diagram(s): 300–467.32 K, x(H) 0.29435–0.48121
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:vh-beta-ord)

Names (2): _corpus: _corpus:phase:h-v:vh-beta-ord  
_tdb: _tdb:VH-08Uki.tdb:VH_BETA_ORD  


### TDB models of VH_BETA_ORD (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): VH_BETA_ORD, type code %O, sha256 `0027aaa295da99fa…`

~~~~text
56: PHASE VH_BETA_ORD %O 3 0.5 0.5 1 !
57: CONST VH_BETA_ORD : H% VA : H VA% : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase_

## VH2_C1 (H–V)

- Id: `phase:h-v:vh2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-v:vh2-c1)

Names (3): _corpus: _corpus:phase:h-v:vh2-c1  
_paper: _paper:10.2320/matertrans.mb200810:δ-VH2  
_tdb: _tdb:VH-08Uki.tdb:VH2_C1  


### TDB models of VH2_C1 (1): PHASE and CONSTITUENT statements as written

[VH-08Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/VH-08Uki.tdb): VH2_C1, type code %, sha256 `0027aaa295da99fa…`

~~~~text
66: PHASE VH2_C1 % 2 1 2 !
67: CONST VH2_C1 : V : H% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MB200810](https://doi.org/10.2320/matertrans.MB200810) S. Ukita, H. Ohtani, M. Hasebe, Mater. Trans. (JIM), 49, 2528-33(2008).  
_assessment that models this phase; reports values for this phase_

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
