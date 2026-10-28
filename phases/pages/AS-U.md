# As–U phases

> As–U system: 10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-U.html · Markdown: https://data.orchid-project.org/phases/pages/AS-U.md

10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-U) · [full JSON](https://data.orchid-project.org/phases/systems/AS-U.json) · [As–U system page](https://data.orchid-project.org/systems/AS-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/AS-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–U system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-as-u-a20-orthorhombic); _phase:as-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–942.02 K, x(As) 0–0 | 3 | 1 |
| [RHOMBOHEDRAL_A7](#phase-as-u-a7-rhombohedral); _phase:as-u:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1089.86 K, x(As) 1–1 | 2 | 1 |
| [BCC_A2](#phase-as-u-bcc-a2); _phase:as-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1048.99–1407.99 K, x(As) 0–0 | 6 | 1 |
| [FCC_A1](#phase-as-u-fcc-a1); _phase:as-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-as-u-hcp-a3); _phase:as-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-as-u-liquid); _phase:as-u:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1089.86–4000 K, x(As) 0–1 | 11 | 1 |
| [TETRAGONAL_U](#phase-as-u-u-tetragonal); _phase:as-u:u-tetragonal_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 942.02–1048.99 K, x(As) 0–0 | 6 | 1 |
| [U3AS4_D73](#phase-as-u-u3as4-d73); _phase:as-u:u3as4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1773.06 K, x(As) 0.57143–0.57143 | 4 | 1 |
| [UAS_B1](#phase-as-u-uas-b1); _phase:as-u:uas-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2978.04 K, x(As) 0.5–0.5 | 13 | 1 |
| [UAS2](#phase-as-u-uas2); _phase:as-u:uas2_ | UAs2 · tP6 · P4/nmm (129) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1271.78 K, x(As) 0.66667–0.66667 | 4 | 1 |

## ORTHORHOMBIC_A20 (As–U)

- Id: `phase:as-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–942.02 K, x(As) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:a20-orthorhombic)

Names (4): _corpus: _corpus:phase:as-u:a20-orthorhombic, corpus:phase:as-u:orthorhombic-a20  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:(αU)  
_tdb: _tdb:UAs-13Wan.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): ORTHORHOMBIC_A20, type code %, sha256 `c7741be41943a282…`

~~~~text
48: PHASE ORTHORHOMBIC_A20 % 1 1 !
49: CONST ORTHORHOMBIC_A20 : AS U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2411157](https://doi.org/10.1149/1.2411157) Robert Benz, M. C. Tinkle, Uranium-Uranium Monoarsenide Phase Diagram, J. Electrochem. Soc. 115, 322 (1968).  
_cited as the source of values for this phase_

## RHOMBOHEDRAL_A7 (As–U)

- Id: `phase:as-u:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1089.86 K, x(As) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:as-u:a7-rhombohedral, corpus:phase:as-u:rhombohedral-a7  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:(As)  
_tdb: _tdb:UAs-13Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `c7741be41943a282…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : AS% U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (As–U)

- Id: `phase:as-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1048.99–1407.99 K, x(As) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:bcc-a2)

Names (3): _corpus: _corpus:phase:as-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:(γU)  
_tdb: _tdb:UAs-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): BCC_A2, type code %B, sha256 `c7741be41943a282…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AS U% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2411157](https://doi.org/10.1149/1.2411157) Robert Benz, M. C. Tinkle, Uranium-Uranium Monoarsenide Phase Diagram, J. Electrochem. Soc. 115, 322 (1968).  
_cited as the source of values for this phase_

## FCC_A1 (As–U)

- Id: `phase:as-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:fcc-a1)

Names (2): _corpus: _corpus:phase:as-u:fcc-a1  
_tdb: _tdb:UAs-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): FCC_A1, type code %A, sha256 `c7741be41943a282…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AS U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase_

## HCP_A3 (As–U)

- Id: `phase:as-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:hcp-a3)

Names (2): _corpus: _corpus:phase:as-u:hcp-a3  
_tdb: _tdb:UAs-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): HCP_A3, type code %A, sha256 `c7741be41943a282…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AS U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase_

## LIQUID (As–U)

- Id: `phase:as-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1089.86–4000 K, x(As) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:liquid)

Names (3): _corpus: _corpus:phase:as-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:L  
_tdb: _tdb:UAs-13Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): LIQUID, type code %, sha256 `c7741be41943a282…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AS U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2411157](https://doi.org/10.1149/1.2411157) Robert Benz, M. C. Tinkle, Uranium-Uranium Monoarsenide Phase Diagram, J. Electrochem. Soc. 115, 322 (1968).  
_cited as the source of values for this phase_

## TETRAGONAL_U (As–U)

- Id: `phase:as-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UAs-13Wan.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 1 of 1 calculated diagram(s): 942.02–1048.99 K, x(As) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:u-tetragonal)

Names (4): _corpus: _corpus:phase:as-u:u-tetragonal, corpus:phase:as-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:(βU)  
_tdb: _tdb:UAs-13Wan.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): TETRAGONAL_U, type code %, sha256 `c7741be41943a282…`

~~~~text
53: PHASE TETRAGONAL_U % 1 1 !
54: CONST TETRAGONAL_U : AS U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2411157](https://doi.org/10.1149/1.2411157) Robert Benz, M. C. Tinkle, Uranium-Uranium Monoarsenide Phase Diagram, J. Electrochem. Soc. 115, 322 (1968).  
_cited as the source of values for this phase_

## U3AS4_D73 (As–U)

- Id: `phase:as-u:u3as4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaaxi and oqmd-7715, space group 220
- Stoichiometry: As 0.5714, U 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–1773.06 K, x(As) 0.57143–0.57143
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:u3as4-d73)

Names (5): _corpus: _corpus:phase:as-u:u3as4-d73  
_mp: _mp:mp-aaaaaaxi  
_oqmd: _oqmd:oqmd-7715  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:As4U3  
_tdb: _tdb:UAs-13Wan.tdb:U3AS4_D73  


### TDB models of U3AS4_D73 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): U3AS4_D73, type code %, sha256 `c7741be41943a282…`

~~~~text
63: PHASE U3AS4_D73 % 2 3 4 !
64: CONST U3AS4_D73 : U : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_

## UAS_B1 (As–U)

- Id: `phase:as-u:uas-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadcy and oqmd-8282, space group 225
- Stoichiometry: As 0.5000, U 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2978.04 K, x(As) 0.5–0.5
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:uas-b1)

Names (5): _corpus: _corpus:phase:as-u:uas-b1  
_mp: _mp:mp-aaaaadcy  
_oqmd: _oqmd:oqmd-8282  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:AsU  
_tdb: _tdb:UAs-13Wan.tdb:UAS_B1  


### TDB models of UAS_B1 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): UAS_B1, type code %, sha256 `c7741be41943a282…`

~~~~text
58: PHASE UAS_B1 % 2 1 1 !
59: CONST UAS_B1 : U : AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2411157](https://doi.org/10.1149/1.2411157) Robert Benz, M. C. Tinkle, Uranium-Uranium Monoarsenide Phase Diagram, J. Electrochem. Soc. 115, 322 (1968).  
_cited as the source of values for this phase_

## UAS2 (As–U)

- Id: `phase:as-u:uas2`; status `assigned`
- Structure: UAs2 · tP6 · P4/nmm (129); type `st:uas2-tp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_129_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: As 0.6667, U 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1271.78 K, x(As) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-u:uas2)

Names (3): _corpus: _corpus:phase:as-u:uas2  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:As2U  
_tdb: _tdb:UAs-13Wan.tdb:UAS2  


### TDB models of UAS2 (1): PHASE and CONSTITUENT statements as written

[UAs-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UAs-13Wan.tdb): UAS2, type code %, sha256 `c7741be41943a282…`

~~~~text
68: PHASE UAS2 % 2 1 2 !
69: CONST UAS2 : U : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_

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
