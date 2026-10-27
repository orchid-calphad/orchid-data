# B–Sc phases

> B–Sc system: 7 phases (tier A 4, liquid 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-SC.html · Markdown: https://data.orchid-project.org/phases/pages/B-SC.md

7 phases (tier A 4, liquid 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-SC) · [full JSON](https://data.orchid-project.org/phases/systems/B-SC.json) · [B–Sc system page](https://data.orchid-project.org/systems/B-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Sc system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-sc-b-beta-rhombo); _phase:b-sc:b-beta-rhombo_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2359.42 K, x(B) 0.98395–1 | 4 | 2 |
| [BCC_A2](#phase-b-sc-bcc-a2); _phase:b-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1607.98–3999.24 K, x(B) 0–1e-05 | 3 | 2 |
| [FCC_A1](#phase-b-sc-fcc-a1); _phase:b-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-b-sc-hcp-a3); _phase:b-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1812.99 K, x(B) 0–0 | 3 | 2 |
| [LIQUID](#phase-b-sc-liquid); _phase:b-sc:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1546.19–4000 K, x(B) 0–1 | 22 | 2 |
| [SCB12_D2F](#phase-b-sc-scb12-d2f); _phase:b-sc:scb12-d2f_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2316.53 K, x(B) 0.92308–0.92308 | 13 | 2 |
| [SCB2_C32](#phase-b-sc-scb2-c32); _phase:b-sc:scb2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2523.25 K, x(B) 0.66667–0.66667 | 14 | 2 |

## BETA_RHOMBO_B (B–Sc)

- Id: `phase:b-sc:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ScB-09Liu.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ScB-90Spe-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–2359.42 K, x(B) 0.98395–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-sc:b-beta-rhombo)

Names (5): _corpus: _corpus:phase:b-sc:b-beta-rhombo, corpus:phase:b-sc:beta-rhombo-b  
_paper: _paper:10.1016/j.jallcom.2008.02.018:βB  
_tdb: _tdb:ScB-09Liu.tdb:BETA_RHOMBO_B, tdb:ScB-90Spe-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[ScB-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-09Liu.tdb): BETA_RHOMBO_B, type code %, sha256 `4ddfc8ae1edee788…`

~~~~text
40: PHASE BETA_RHOMBO_B % 1 1 !
41: CONST BETA_RHOMBO_B : B% SC : !
~~~~

[ScB-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-90Spe-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `a196e50efc20f9b4…`

~~~~text
50: PHASE BETA_RHOMBO_B % 1 1 !
51: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02843307](https://doi.org/10.1007/BF02843307) K.E. Spear, P.K. Liao, Bull. Alloy Phase Diag., 11, 321-24(1990).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-4596(78)90089-0](https://doi.org/10.1016/0022-4596%2878%2990089-0) Bengt Callmer, A single-crystal diffractometry investigation of scandium in β-rhombohedral boron, Journal of Solid State Chemistry 23, 391-398 (1978).  
_cited as the source of values for this phase_

## BCC_A2 (B–Sc)

- Id: `phase:b-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1607.98–3999.24 K, x(B) 0–1e-05
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-sc:bcc-a2)

Names (5): _corpus: _corpus:phase:b-sc:bcc-a2  
_paper: _paper:10.1007/bf02843307:βSc, paper:10.1016/j.jallcom.2008.02.018:βSc  
_tdb: _tdb:ScB-09Liu.tdb:BCC_A2, tdb:ScB-90Spe-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ScB-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-09Liu.tdb): BCC_A2, type code %B, sha256 `4ddfc8ae1edee788…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : B SC% : VA : !
~~~~

[ScB-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-90Spe-LB.tdb): BCC_A2, type code %B, sha256 `a196e50efc20f9b4…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : SC : B VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02843307](https://doi.org/10.1007/BF02843307) K.E. Spear, P.K. Liao, Bull. Alloy Phase Diag., 11, 321-24(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (B–Sc)

- Id: `phase:b-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-sc:fcc-a1)

Names (3): _corpus: _corpus:phase:b-sc:fcc-a1  
_tdb: _tdb:ScB-09Liu.tdb:FCC_A1, tdb:ScB-90Spe-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ScB-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-09Liu.tdb): FCC_A1, type code %A, sha256 `4ddfc8ae1edee788…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : B SC : VA : !
~~~~

[ScB-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-90Spe-LB.tdb): FCC_A1, type code %A, sha256 `a196e50efc20f9b4…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : SC : B VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02843307](https://doi.org/10.1007/BF02843307) K.E. Spear, P.K. Liao, Bull. Alloy Phase Diag., 11, 321-24(1990).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase_

## HCP_A3 (B–Sc)

- Id: `phase:b-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1812.99 K, x(B) 0–0
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-sc:hcp-a3)

Names (5): _corpus: _corpus:phase:b-sc:hcp-a3  
_paper: _paper:10.1007/bf02843307:(αSc), paper:10.1016/j.jallcom.2008.02.018:αSc  
_tdb: _tdb:ScB-09Liu.tdb:HCP_A3, tdb:ScB-90Spe-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ScB-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-09Liu.tdb): HCP_A3, type code %A, sha256 `4ddfc8ae1edee788…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : B SC% : VA : !
~~~~

[ScB-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-90Spe-LB.tdb): HCP_A3, type code %A, sha256 `a196e50efc20f9b4…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : SC : B VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02843307](https://doi.org/10.1007/BF02843307) K.E. Spear, P.K. Liao, Bull. Alloy Phase Diag., 11, 321-24(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (B–Sc)

- Id: `phase:b-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1546.19–4000 K, x(B) 0–1
- Literature: 22 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-sc:liquid)

Names (6): _corpus: _corpus:phase:b-sc:liquid  
_paper: _paper:10.1007/bf02843307:L, paper:10.1007/bf02843307:liquid, paper:10.1016/j.jallcom.2008.02.018:L  
_tdb: _tdb:ScB-09Liu.tdb:LIQUID, tdb:ScB-90Spe-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ScB-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-09Liu.tdb): LIQUID, type code %, sha256 `4ddfc8ae1edee788…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : B SC : !
~~~~

[ScB-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-90Spe-LB.tdb): LIQUID, type code %, sha256 `a196e50efc20f9b4…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : B SC : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02843307](https://doi.org/10.1007/BF02843307) K.E. Spear, P.K. Liao, Bull. Alloy Phase Diag., 11, 321-24(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-4596(78)90089-0](https://doi.org/10.1016/0022-4596%2878%2990089-0) Bengt Callmer, A single-crystal diffractometry investigation of scandium in β-rhombohedral boron, Journal of Solid State Chemistry 23, 391-398 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(70)90017-6](https://doi.org/10.1016/0025-5408%2870%2990017-6) P. Peshev, J. Etourneau, R. Naslain, Sur le systeme bore-scandium, Materials Research Bulletin 5, 319-327 (1970).  
_cited as the source of values for this phase_

## SCB12_D2F (B–Sc)

- Id: `phase:b-sc:scb12-d2f`; status `needs_review`
- No structure assigned. Why: sgte_mmc2_row_disagrees_with_name:SCB12_D2F; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Fm-3m (225) — on-hull MP ScB12 at x(SC)=0.0769
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD B12 Sc1 at x(SC)=0.0769
- Candidate (literature_printed): ScB12 · tI26 — printed with a label mapped to this phase
- Candidate (name_token): UB12 · D2_f · cF52 · Fm-3m (225) — Strukturbericht/word 'D2F' in the TDB name
- Candidate (sgte_mmc2): UB12 · D2_f · cF52 · Fm-3m (225) — Hallstedt 2025 mmc2 row for SCB12_D2F: ScB12 (alt. prototype ScB12)
- Candidate (sgte_mmc2): ScB12 · tI26 · I4/mmm (139) — Hallstedt 2025 mmc2 row for SCB12_D2F: ScB12 (see UB12)
- Candidate (tdb_comment): UB12 · cF52 · Fm-3m — ScB-09Liu.tdb: 'Prototype UB12 (cF52, Fm-3m)'
- Candidate (tdb_comment): UB12 · cF52 · Fm-3m — ScB-90Spe-LB.tdb: 'Prototype UB12 (cF52, Fm-3m)'
- Stoichiometry: B 0.9231, Sc 0.0769
- Stability: stable in 2 of 2 calculated diagram(s): 300–2316.53 K, x(B) 0.92308–0.92308
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-sc:scb12-d2f)

Names (5): _corpus: _corpus:phase:b-sc:scb12-d2f  
_paper: _paper:10.1007/bf02843307:ScB12, paper:10.1016/j.jallcom.2008.02.018:ScB12  
_tdb: _tdb:ScB-09Liu.tdb:SCB12_D2F, tdb:ScB-90Spe-LB.tdb:SCB12_D2F  


### TDB models of SCB12_D2F (2): PHASE and CONSTITUENT statements as written

[ScB-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-09Liu.tdb): SCB12_D2F, type code %, sha256 `4ddfc8ae1edee788…`

~~~~text
52: PHASE SCB12_D2F % 2 1 12 !
53: CONST SCB12_D2F : SC : B : !
~~~~

[ScB-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-90Spe-LB.tdb): SCB12_D2F, type code %, sha256 `a196e50efc20f9b4…`

~~~~text
62: PHASE SCB12_D2F % 2 1 12 !
63: CONST SCB12_D2F : SC : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02843307](https://doi.org/10.1007/BF02843307) K.E. Spear, P.K. Liao, Bull. Alloy Phase Diag., 11, 321-24(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-4596(78)90089-0](https://doi.org/10.1016/0022-4596%2878%2990089-0) Bengt Callmer, A single-crystal diffractometry investigation of scandium in β-rhombohedral boron, Journal of Solid State Chemistry 23, 391-398 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(70)90017-6](https://doi.org/10.1016/0025-5408%2870%2990017-6) P. Peshev, J. Etourneau, R. Naslain, Sur le systeme bore-scandium, Materials Research Bulletin 5, 319-327 (1970).  
_cited as the source of values for this phase_

## SCB2_C32 (B–Sc)

- Id: `phase:b-sc:scb2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadiq and oqmd-8428, space group 191
- Stoichiometry: B 0.6667, Sc 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–2523.25 K, x(B) 0.66667–0.66667
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-sc:scb2-c32)

Names (7): _corpus: _corpus:phase:b-sc:scb2-c32  
_mp: _mp:mp-aaaaadiq  
_oqmd: _oqmd:oqmd-8428  
_paper: _paper:10.1007/bf02843307:ScB2, paper:10.1016/j.jallcom.2008.02.018:ScB2  
_tdb: _tdb:ScB-09Liu.tdb:SCB2_C32, tdb:ScB-90Spe-LB.tdb:SCB2_C32  


### TDB models of SCB2_C32 (2): PHASE and CONSTITUENT statements as written

[ScB-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-09Liu.tdb): SCB2_C32, type code %, sha256 `4ddfc8ae1edee788…`

~~~~text
45: PHASE SCB2_C32 % 2 1 2 !
46: CONST SCB2_C32 : SC : B : !
~~~~

[ScB-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ScB-90Spe-LB.tdb): SCB2_C32, type code %, sha256 `a196e50efc20f9b4…`

~~~~text
55: PHASE SCB2_C32 % 2 1 2 !
56: CONST SCB2_C32 : SC : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02843307](https://doi.org/10.1007/BF02843307) K.E. Spear, P.K. Liao, Bull. Alloy Phase Diag., 11, 321-24(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
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
