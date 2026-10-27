# Re–U phases

> Re–U system: 8 phases (tier A 4, liquid 1, needs_review 3); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RE-U.html · Markdown: https://data.orchid-project.org/phases/pages/RE-U.md

8 phases (tier A 4, liquid 1, needs_review 3); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RE-U) · [full JSON](https://data.orchid-project.org/phases/systems/RE-U.json) · [Re–U system page](https://data.orchid-project.org/systems/RE-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/RE-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Re–U system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-re-u-a20-orthorhombic); _phase:re-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1047.02 K, x(U) 1–1 | 2 | 1 |
| [BCC_A2](#phase-re-u-bcc-a2); _phase:re-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 962.7–1411.51 K, x(U) 0.88657–1 | 8 | 1 |
| [FCC_A1](#phase-re-u-fcc-a1); _phase:re-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-re-u-hcp-a3); _phase:re-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3494.94 K, x(U) 0–0.00502 | 5 | 1 |
| [LIQUID](#phase-re-u-liquid); _phase:re-u:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1379.79–4000 K, x(U) 0–1 | 12 | 1 |
| [RE2U](#phase-re-u-re2u); _phase:re-u:re2u_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2498.84 K, x(U) 0.33333–0.33333 | 14 | 1 |
| [REU2](#phase-re-u-reu2); _phase:re-u:reu2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1019.9 K, x(U) 0.66667–0.66667 | 6 | 1 |
| [TETRAGONAL_U](#phase-re-u-u-tetragonal); _phase:re-u:u-tetragonal_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 907.59–1048.99 K, x(U) 0.97931–1 | 4 | 1 |

## ORTHORHOMBIC_A20 (Re–U)

- Id: `phase:re-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1047.02 K, x(U) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:a20-orthorhombic)

Names (4): _corpus: _corpus:phase:re-u:a20-orthorhombic, corpus:phase:re-u:orthorhombic-a20  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:α-U  
_tdb: _tdb:ReU-11Ber.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): ORTHORHOMBIC_A20, type code %, sha256 `a43b5b0bf7f00026…`

~~~~text
42: PHASE ORTHORHOMBIC_A20 % 1 1 !
43: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(63)90059-6](https://doi.org/10.1016/0022-5088%2863%2990059-6) R.J. Jackson, D.E. Williams, W.L. Larsen, The uraniumrhenium alloy system, Journal of the Less Common Metals 5, 443-461 (1963).  
_cited as the source of values for this phase_

## BCC_A2 (Re–U)

- Id: `phase:re-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 962.7–1411.51 K, x(U) 0.88657–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:bcc-a2)

Names (3): _corpus: _corpus:phase:re-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:γ-U  
_tdb: _tdb:ReU-11Ber.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): BCC_A2, type code %B, sha256 `a43b5b0bf7f00026…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : RE U : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(63)90059-6](https://doi.org/10.1016/0022-5088%2863%2990059-6) R.J. Jackson, D.E. Williams, W.L. Larsen, The uraniumrhenium alloy system, Journal of the Less Common Metals 5, 443-461 (1963).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(77)90078-2](https://doi.org/10.1016/0022-3115%2877%2990078-2) S.P. Garg, R.J. Ackermann, The high temperature phase diagrams for Th-Mo, Th-Re, U-Mo, and U-Re; derived thermodynamic properties of refractory metal solutes in liquid thorium and uranium, Journal of Nuclear Materials 64, 265-274 (1977).  
_cited as the source of values for this phase_

## FCC_A1 (Re–U)

- Id: `phase:re-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:fcc-a1)

Names (2): _corpus: _corpus:phase:re-u:fcc-a1  
_tdb: _tdb:ReU-11Ber.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): FCC_A1, type code %A, sha256 `a43b5b0bf7f00026…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : RE U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## HCP_A3 (Re–U)

- Id: `phase:re-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3494.94 K, x(U) 0–0.00502
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:hcp-a3)

Names (3): _corpus: _corpus:phase:re-u:hcp-a3  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:(Re)  
_tdb: _tdb:ReU-11Ber.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): HCP_A3, type code %A, sha256 `a43b5b0bf7f00026…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : RE% U : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(77)90078-2](https://doi.org/10.1016/0022-3115%2877%2990078-2) S.P. Garg, R.J. Ackermann, The high temperature phase diagrams for Th-Mo, Th-Re, U-Mo, and U-Re; derived thermodynamic properties of refractory metal solutes in liquid thorium and uranium, Journal of Nuclear Materials 64, 265-274 (1977).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(94)90381-6](https://doi.org/10.1016/0022-3115%2894%2990381-6) Richard E. Mason, Mohamed S. El-Genk, Experimental investigation of the ruthenium-uranium and rhenium-uranium binary systems, Journal of Nuclear Materials 217, 304-321 (1994).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(63)90059-6](https://doi.org/10.1016/0022-5088%2863%2990059-6) R.J. Jackson, D.E. Williams, W.L. Larsen, The uraniumrhenium alloy system, Journal of the Less Common Metals 5, 443-461 (1963).  
_cited as the source of values for this phase_

## LIQUID (Re–U)

- Id: `phase:re-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1379.79–4000 K, x(U) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:liquid)

Names (3): _corpus: _corpus:phase:re-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:Liquid  
_tdb: _tdb:ReU-11Ber.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): LIQUID, type code %, sha256 `a43b5b0bf7f00026…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : RE U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(63)90059-6](https://doi.org/10.1016/0022-5088%2863%2990059-6) R.J. Jackson, D.E. Williams, W.L. Larsen, The uraniumrhenium alloy system, Journal of the Less Common Metals 5, 443-461 (1963).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(77)90078-2](https://doi.org/10.1016/0022-3115%2877%2990078-2) S.P. Garg, R.J. Ackermann, The high temperature phase diagrams for Th-Mo, Th-Re, U-Mo, and U-Re; derived thermodynamic properties of refractory metal solutes in liquid thorium and uranium, Journal of Nuclear Materials 64, 265-274 (1977).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(94)90381-6](https://doi.org/10.1016/0022-3115%2894%2990381-6) Richard E. Mason, Mohamed S. El-Genk, Experimental investigation of the ruthenium-uranium and rhenium-uranium binary systems, Journal of Nuclear Materials 217, 304-321 (1994).  
_cited as the source of values for this phase_

## RE2U (Re–U)

- Id: `phase:re-u:re2u`; status `needs_review`
- No structure assigned. Why: dft_space_group_63_matches_4_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Cmcm (63) — on-hull MP URe2 at x(U)=0.3333
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Re2 U1 at x(U)=0.3333
- Candidate (dft_space_group_and_stoichiometry): Au2V · oC12 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): ZrSi2 · C49 · oC12 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): GaLi2 · oC12 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): Re2U · oC24 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (literature_printed): MgZn2 · hP12 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for RE2U: Re2U (high T, see also Re2U)
- Stoichiometry: Re 0.6667, U 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2498.84 K, x(U) 0.33333–0.33333
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:re2u)

Names (3): _corpus: _corpus:phase:re-u:re2u  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:URe2  
_tdb: _tdb:ReU-11Ber.tdb:RE2U  


### TDB models of RE2U (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): RE2U, type code %, sha256 `a43b5b0bf7f00026…`

~~~~text
53: PHASE RE2U % 2 2 1 !
54: CONST RE2U : RE : U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(63)90059-6](https://doi.org/10.1016/0022-5088%2863%2990059-6) R.J. Jackson, D.E. Williams, W.L. Larsen, The uraniumrhenium alloy system, Journal of the Less Common Metals 5, 443-461 (1963).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(77)90078-2](https://doi.org/10.1016/0022-3115%2877%2990078-2) S.P. Garg, R.J. Ackermann, The high temperature phase diagrams for Th-Mo, Th-Re, U-Mo, and U-Re; derived thermodynamic properties of refractory metal solutes in liquid thorium and uranium, Journal of Nuclear Materials 64, 265-274 (1977).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(94)90381-6](https://doi.org/10.1016/0022-3115%2894%2990381-6) Richard E. Mason, Mohamed S. El-Genk, Experimental investigation of the ruthenium-uranium and rhenium-uranium binary systems, Journal of Nuclear Materials 217, 304-321 (1994).  
_cited as the source of values for this phase_

## REU2 (Re–U)

- Id: `phase:re-u:reu2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (ReU2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (ReU2) — Hallstedt 2025 mmc2 row for REU2: ReU2
- Stoichiometry: Re 0.3333, U 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1019.9 K, x(U) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:reu2)

Names (3): _corpus: _corpus:phase:re-u:reu2  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:U2Re  
_tdb: _tdb:ReU-11Ber.tdb:REU2  


### TDB models of REU2 (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): REU2, type code %, sha256 `a43b5b0bf7f00026…`

~~~~text
58: PHASE REU2 % 2 1 2 !
59: CONST REU2 : RE : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(63)90059-6](https://doi.org/10.1016/0022-5088%2863%2990059-6) R.J. Jackson, D.E. Williams, W.L. Larsen, The uraniumrhenium alloy system, Journal of the Less Common Metals 5, 443-461 (1963).  
_cited as the source of values for this phase_

## TETRAGONAL_U (Re–U)

- Id: `phase:re-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — ReU-11Ber.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 1 of 1 calculated diagram(s): 907.59–1048.99 K, x(U) 0.97931–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-u:u-tetragonal)

Names (4): _corpus: _corpus:phase:re-u:u-tetragonal, corpus:phase:re-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:β-U  
_tdb: _tdb:ReU-11Ber.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (1): PHASE and CONSTITUENT statements as written

[ReU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb): TETRAGONAL_U, type code %, sha256 `a43b5b0bf7f00026…`

~~~~text
47: PHASE TETRAGONAL_U % 1 1 !
48: CONST TETRAGONAL_U : RE U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(63)90059-6](https://doi.org/10.1016/0022-5088%2863%2990059-6) R.J. Jackson, D.E. Williams, W.L. Larsen, The uraniumrhenium alloy system, Journal of the Less Common Metals 5, 443-461 (1963).  
_cited as the source of values for this phase_

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
