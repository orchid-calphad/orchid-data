# B–Gd phases

> B–Gd system: 11 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-GD.html · Markdown: https://data.orchid-project.org/phases/pages/B-GD.md

11 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-GD) · [full JSON](https://data.orchid-project.org/phases/systems/B-GD.json) · [Markdown](https://data.orchid-project.org/phases/pages/B-GD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Gd system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-gd-b-alpha-rhombo); _phase:b-gd:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-gd-b-beta-rhombo); _phase:b-gd:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2348 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-gd-bcc-a2); _phase:b-gd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1508.06–3999.31 K, x(B) 0–0 | 0 | 1 |
| [FCC_A1](#phase-b-gd-fcc-a1); _phase:b-gd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GD2B5](#phase-b-gd-gd2b5); _phase:b-gd:gd2b5_ | Gd2B5 · mP28 · P2_1/c (14) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2373.51 K, x(B) 0.71429–0.71429 | 0 | 1 |
| [GDB2_C32](#phase-b-gd-gdb2-c32); _phase:b-gd:gdb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1535.93–2328.35 K, x(B) 0.66667–0.66667 | 0 | 1 |
| [GDB4_D1E](#phase-b-gd-gdb4-d1e); _phase:b-gd:gdb4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2923.04 K, x(B) 0.8–0.8 | 0 | 1 |
| [GDB6_D21](#phase-b-gd-gdb6-d21); _phase:b-gd:gdb6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2772.07 K, x(B) 0.85714–0.85714 | 0 | 1 |
| [GDB66](#phase-b-gd-gdb66); _phase:b-gd:gdb66_ | YB66 · cF1936 · Fm-3c (226) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2464.11 K, x(B) 0.98507–0.98507 | 0 | 1 |
| [HCP_A3](#phase-b-gd-hcp-a3); _phase:b-gd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1508.06 K, x(B) 0–0 | 0 | 1 |
| [LIQUID](#phase-b-gd-liquid); _phase:b-gd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1446.58–4000 K, x(B) 0–1 | 0 | 1 |

## ALPHA_RHOMBO_B (B–Gd)

- Id: `phase:b-gd:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — GdB-22Wei.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-gd:b-alpha-rhombo  
_tdb: _tdb:GdB-22Wei.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): ALPHA_RHOMBO_B, type code %, sha256 `9a35afbabb850afc…`

~~~~text
48: PHASE ALPHA_RHOMBO_B % 1 1 !
49: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Gd)

- Id: `phase:b-gd:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — GdB-22Wei.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2348 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-gd:b-beta-rhombo  
_tdb: _tdb:GdB-22Wei.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): BETA_RHOMBO_B, type code %, sha256 `9a35afbabb850afc…`

~~~~text
53: PHASE BETA_RHOMBO_B % 1 1 !
54: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## BCC_A2 (B–Gd)

- Id: `phase:b-gd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1508.06–3999.31 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:bcc-a2)

Names (2): _corpus: _corpus:phase:b-gd:bcc-a2  
_tdb: _tdb:GdB-22Wei.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): BCC_A2, type code %B, sha256 `9a35afbabb850afc…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : GD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## FCC_A1 (B–Gd)

- Id: `phase:b-gd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:fcc-a1)

Names (2): _corpus: _corpus:phase:b-gd:fcc-a1  
_tdb: _tdb:GdB-22Wei.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): FCC_A1, type code %A, sha256 `9a35afbabb850afc…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : GD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## GD2B5 (B–Gd)

- Id: `phase:b-gd:gd2b5`; status `assigned`
- Structure: Gd2B5 · mP28 · P2_1/c (14); type `st:gd2b5-mp28`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: B 0.7143, Gd 0.2857
- Stability: stable in 1 of 1 calculated diagram(s): 300–2373.51 K, x(B) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:gd2b5)

Names (4): _corpus: _corpus:phase:b-gd:gd2b5  
_mp: _mp:mp-aaaabpza  
_oqmd: _oqmd:oqmd-2052247  
_tdb: _tdb:GdB-22Wei.tdb:GD2B5  


### TDB models of GD2B5 (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): GD2B5, type code %, sha256 `9a35afbabb850afc…`

~~~~text
63: PHASE GD2B5 % 2 2 5 !
64: CONST GD2B5 : GD : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## GDB2_C32 (B–Gd)

- Id: `phase:b-gd:gdb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.6667, Gd 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1535.93–2328.35 K, x(B) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:gdb2-c32)

Names (2): _corpus: _corpus:phase:b-gd:gdb2-c32  
_tdb: _tdb:GdB-22Wei.tdb:GDB2_C32  


### TDB models of GDB2_C32 (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): GDB2_C32, type code %, sha256 `9a35afbabb850afc…`

~~~~text
58: PHASE GDB2_C32 % 2 1 2 !
59: CONST GDB2_C32 : GD : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## GDB4_D1E (B–Gd)

- Id: `phase:b-gd:gdb4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackxlr and oqmd-1453214, space group 127
- Stoichiometry: B 0.8000, Gd 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2923.04 K, x(B) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:gdb4-d1e)

Names (4): _corpus: _corpus:phase:b-gd:gdb4-d1e  
_mp: _mp:mp-aaackxlr  
_oqmd: _oqmd:oqmd-1453214  
_tdb: _tdb:GdB-22Wei.tdb:GDB4_D1E  


### TDB models of GDB4_D1E (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): GDB4_D1E, type code %, sha256 `9a35afbabb850afc…`

~~~~text
68: PHASE GDB4_D1E % 2 1 4 !
69: CONST GDB4_D1E : GD : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## GDB6_D21 (B–Gd)

- Id: `phase:b-gd:gdb6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.8571, Gd 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–2772.07 K, x(B) 0.85714–0.85714
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:gdb6-d21)

Names (2): _corpus: _corpus:phase:b-gd:gdb6-d21  
_tdb: _tdb:GdB-22Wei.tdb:GDB6_D21  


### TDB models of GDB6_D21 (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): GDB6_D21, type code %, sha256 `9a35afbabb850afc…`

~~~~text
73: PHASE GDB6_D21 % 2 1 6 !
74: CONST GDB6_D21 : GD : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## GDB66 (B–Gd)

- Id: `phase:b-gd:gdb66`; status `assigned`
- Structure: YB66 · cF1936 · Fm-3c (226); type `st:yb66-cf1936`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.9851, Gd 0.0149
- Stability: stable in 1 of 1 calculated diagram(s): 300–2464.11 K, x(B) 0.98507–0.98507
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:gdb66)

Names (2): _corpus: _corpus:phase:b-gd:gdb66  
_tdb: _tdb:GdB-22Wei.tdb:GDB66  


### TDB models of GDB66 (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): GDB66, type code %, sha256 `9a35afbabb850afc…`

~~~~text
78: PHASE GDB66 % 2 1 66 !
79: CONST GDB66 : GD : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## HCP_A3 (B–Gd)

- Id: `phase:b-gd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1508.06 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:hcp-a3)

Names (2): _corpus: _corpus:phase:b-gd:hcp-a3  
_tdb: _tdb:GdB-22Wei.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): HCP_A3, type code %, sha256 `9a35afbabb850afc…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : GD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## LIQUID (B–Gd)

- Id: `phase:b-gd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1446.58–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-gd:liquid)

Names (2): _corpus: _corpus:phase:b-gd:liquid  
_tdb: _tdb:GdB-22Wei.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GdB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/GdB-22Wei.tdb): LIQUID, type code %, sha256 `9a35afbabb850afc…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : B GD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
