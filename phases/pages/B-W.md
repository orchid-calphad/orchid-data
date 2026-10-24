# B–W phases

> B–W system: 10 phases (tier A 5, tier C 3, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-W.html · Markdown: https://data.orchid-project.org/phases/pages/B-W.md

10 phases (tier A 5, tier C 3, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-W) · [full JSON](https://data.orchid-project.org/phases/systems/B-W.json) · [B–W system page](https://data.orchid-project.org/systems/B-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–W system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-w-b-beta-rhombo); _phase:b-w:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2350 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-w-bcc-a2); _phase:b-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.78 K, x(B) 0–0.00151 | 4 | 1 |
| [M2B_C16](#phase-b-w-c16-m2b); _phase:b-w:c16-m2b_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2932.09 K, x(B) 0.33333–0.33333 | 21 | 1 |
| [FCC_A1](#phase-b-w-fcc-a1); _phase:b-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-w-hcp-a3); _phase:b-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-b-w-liquid); _phase:b-w:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2174.06–4000 K, x(B) 0–1 | 20 | 1 |
| [W2B5_D8I](#phase-b-w-w2b5-d8i); _phase:b-w:w2b5-d8i_ | Mo2B5 · D8_i · hR7 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2633.82 K, x(B) 0.67528–0.71224 | 16 | 1 |
| [W2B9](#phase-b-w-w2b9); _phase:b-w:w2b9_ | W2B9 · hP22 · P-3 (147) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2309.91 K, x(B) 0.81818–0.81818 | 4 | 1 |
| [WB_B33](#phase-b-w-wb-b33); _phase:b-w:wb-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 2328.11–2951.98 K, x(B) 0.47381–0.49722 | 13 | 1 |
| [WB_BG](#phase-b-w-wb-bg); _phase:b-w:wb-bg_ | MoB · B_g · tI16 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2436.49 K, x(B) 0.48014–0.5 | 16 | 1 |

## BETA_RHOMBO_B (B–W)

- Id: `phase:b-w:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — WB-95Dus-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2350 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:b-beta-rhombo)

Names (3): _corpus: _corpus:phase:b-w:b-beta-rhombo, corpus:phase:b-w:beta-rhombo-b  
_tdb: _tdb:WB-95Dus-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `9983d096ff608c15…`

~~~~text
46: PHASE BETA_RHOMBO_B % 1 1 !
47: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase_

## BCC_A2 (B–W)

- Id: `phase:b-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.78 K, x(B) 0–0.00151
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:bcc-a2)

Names (3): _corpus: _corpus:phase:b-w:bcc-a2  
_paper: _paper:10.1007/bf02664852:W  
_tdb: _tdb:WB-95Dus-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): BCC_A2, type code %B, sha256 `9983d096ff608c15…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : W : B VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase; reports values for this phase_

## M2B_C16 (B–W)

- Id: `phase:b-w:c16-m2b`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaaabqv and oqmd-4586, space group 140
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M2B); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.3333, W 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–2932.09 K, x(B) 0.33333–0.33333
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:c16-m2b)

Names (6): _corpus: _corpus:phase:b-w:c16-m2b, corpus:phase:b-w:m2b-c16  
_mp: _mp:mp-aaaaabqv  
_oqmd: _oqmd:oqmd-4586  
_paper: _paper:10.1007/bf02664852:W2B  
_tdb: _tdb:WB-95Dus-LB.tdb:M2B_C16  


### TDB models of M2B_C16 (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): M2B_C16, type code %, sha256 `9983d096ff608c15…`

~~~~text
51: PHASE M2B_C16 % 2 2 1 !
52: CONST M2B_C16 : W : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (B–W)

- Id: `phase:b-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:fcc-a1)

Names (2): _corpus: _corpus:phase:b-w:fcc-a1  
_tdb: _tdb:WB-95Dus-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): FCC_A1, type code %A, sha256 `9983d096ff608c15…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : W : B VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase_

## HCP_A3 (B–W)

- Id: `phase:b-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:hcp-a3)

Names (2): _corpus: _corpus:phase:b-w:hcp-a3  
_tdb: _tdb:WB-95Dus-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): HCP_A3, type code %A, sha256 `9983d096ff608c15…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : W : B VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase_

## LIQUID (B–W)

- Id: `phase:b-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2174.06–4000 K, x(B) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:liquid)

Names (3): _corpus: _corpus:phase:b-w:liquid  
_paper: _paper:10.1007/bf02664852:L  
_tdb: _tdb:WB-95Dus-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): LIQUID, type code %, sha256 `9983d096ff608c15…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : B W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase; reports values for this phase_

## W2B5_D8I (B–W)

- Id: `phase:b-w:w2b5-d8i`; status `assigned`
- Structure: Mo2B5 · D8_i · hR7 · R-3m (166); type `st:d8-i-mo2b5-hr7`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2633.82 K, x(B) 0.67528–0.71224
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:w2b5-d8i)

Names (4): _corpus: _corpus:phase:b-w:w2b5-d8i  
_paper: _paper:10.1007/bf02664852:W2B5, paper:10.1007/bf02664852:W2B5-x  
_tdb: _tdb:WB-95Dus-LB.tdb:W2B5_D8I  


### TDB models of W2B5_D8I (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): W2B5_D8I, type code %, sha256 `9983d096ff608c15…`

~~~~text
66: PHASE W2B5_D8I % 2 2 5 !
67: CONST W2B5_D8I : W : B VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase; reports values for this phase_

## W2B9 (B–W)

- Id: `phase:b-w:w2b9`; status `assigned`
- Structure: W2B9 · hP22 · P-3 (147); type `st:w2b9-hp22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.8182, W 0.1818
- Stability: stable in 1 of 1 calculated diagram(s): 300–2309.91 K, x(B) 0.81818–0.81818
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:w2b9)

Names (3): _corpus: _corpus:phase:b-w:w2b9  
_paper: _paper:10.1007/bf02664852:W1-xB3  
_tdb: _tdb:WB-95Dus-LB.tdb:W2B9  


### TDB models of W2B9 (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): W2B9, type code %, sha256 `9983d096ff608c15…`

~~~~text
71: PHASE W2B9 % 2 2 9 !
72: CONST W2B9 : W : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase; reports values for this phase_

## WB_B33 (B–W)

- Id: `phase:b-w:wb-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 2328.11–2951.98 K, x(B) 0.47381–0.49722
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:wb-b33)

Names (3): _corpus: _corpus:phase:b-w:wb-b33  
_paper: _paper:10.1007/bf02664852:βWB  
_tdb: _tdb:WB-95Dus-LB.tdb:WB_B33  


### TDB models of WB_B33 (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): WB_B33, type code %, sha256 `9983d096ff608c15…`

~~~~text
61: PHASE WB_B33 % 2 1 1 !
62: CONST WB_B33 : W : B VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase; reports values for this phase_

## WB_BG (B–W)

- Id: `phase:b-w:wb-bg`; status `assigned`
- Structure: MoB · B_g · tI16 · I4_1/amd (141); type `st:b-g-mob-ti16`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2436.49 K, x(B) 0.48014–0.5
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-w:wb-bg)

Names (3): _corpus: _corpus:phase:b-w:wb-bg  
_paper: _paper:10.1007/bf02664852:αWB  
_tdb: _tdb:WB-95Dus-LB.tdb:WB_BG  


### TDB models of WB_BG (1): PHASE and CONSTITUENT statements as written

[WB-95Dus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WB-95Dus-LB.tdb): WB_BG, type code %, sha256 `9983d096ff608c15…`

~~~~text
56: PHASE WB_BG % 2 1 1 !
57: CONST WB_BG : W : B VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02664852](https://doi.org/10.1007/BF02664852) H. Duschanek, P. Rogl, J. Phase Equilib., 16, 150-61(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(76)90180-6](https://doi.org/10.1016/0022-5088%2876%2990180-6) A.R. Miedema, On the heat of formation of solid alloys. II, Journal of the Less Common Metals 46, 67-83 (1976).  
_cited as the source of values for this phase_

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
