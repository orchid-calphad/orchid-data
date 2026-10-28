# Mn–U phases

> Mn–U system: 10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-U.html · Markdown: https://data.orchid-project.org/phases/pages/MN-U.md

10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-U) · [full JSON](https://data.orchid-project.org/phases/systems/MN-U.json) · [Mn–U system page](https://data.orchid-project.org/systems/MN-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–U system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-mn-u-a20-orthorhombic); _phase:mn-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1047.02 K, x(U) 1–1 | 1 | 1 |
| [BCC_A2](#phase-mn-u-bcc-a2); _phase:mn-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1020–1530 K, x(U) 0–1 | 3 | 1 |
| [CBCC_A12](#phase-mn-u-cbcc-a12); _phase:mn-u:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1102.5 K, x(U) 0–0 | 1 | 1 |
| [CUB_A13](#phase-mn-u-cub-a13); _phase:mn-u:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 970.76–1384.45 K, x(U) 0–0.01143 | 4 | 1 |
| [FCC_A1](#phase-mn-u-fcc-a1); _phase:mn-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1360–1420 K, x(U) 0–0.00375 | 2 | 1 |
| [HCP_A3](#phase-mn-u-hcp-a3); _phase:mn-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-mn-u-liquid); _phase:mn-u:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 991.35–4000 K, x(U) 0–1 | 12 | 1 |
| [MN2U_C15](#phase-mn-u-mn2u-c15); _phase:mn-u:mn2u-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1393.3 K, x(U) 0.33333–0.33333 | 7 | 1 |
| [MNU6_D2C](#phase-mn-u-mnu6-d2c); _phase:mn-u:mnu6-d2c_ | MnU6 · D2_c · tI28 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–997.68 K, x(U) 0.85714–0.85714 | 5 | 1 |
| [TETRAGONAL_U](#phase-mn-u-u-tetragonal); _phase:mn-u:u-tetragonal_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 900.86–1055.3 K, x(U) 0.98568–1 | 5 | 1 |

## ORTHORHOMBIC_A20 (Mn–U)

- Id: `phase:mn-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1047.02 K, x(U) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:a20-orthorhombic)

Names (4): _corpus: _corpus:phase:mn-u:a20-orthorhombic, corpus:phase:mn-u:orthorhombic-a20  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:αU  
_tdb: _tdb:MnU-08Liu.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): ORTHORHOMBIC_A20, type code %, sha256 `edda765ad8b359b9…`

~~~~text
53: PHASE ORTHORHOMBIC_A20 % 1 1 !
54: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Mn–U)

- Id: `phase:mn-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1020–1530 K, x(U) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:bcc-a2)

Names (4): _corpus: _corpus:phase:mn-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:γU, paper:10.1016/j.jnucmat.2008.07.008:δMn  
_tdb: _tdb:MnU-08Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): BCC_A2, type code %B, sha256 `edda765ad8b359b9…`

~~~~text
33: PHASE BCC_A2 %B 2 1 1.5 !
34: CONST BCC_A2 : MN% U% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## CBCC_A12 (Mn–U)

- Id: `phase:mn-u:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1102.5 K, x(U) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:cbcc-a12)

Names (3): _corpus: _corpus:phase:mn-u:cbcc-a12  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:αMn  
_tdb: _tdb:MnU-08Liu.tdb:CBCC_A12  


### TDB models of CBCC_A12 (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): CBCC_A12, type code %A, sha256 `edda765ad8b359b9…`

~~~~text
43: PHASE CBCC_A12 %A 2 1 1 !
44: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## CUB_A13 (Mn–U)

- Id: `phase:mn-u:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 970.76–1384.45 K, x(U) 0–0.01143
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:cub-a13)

Names (3): _corpus: _corpus:phase:mn-u:cub-a13  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:βMn  
_tdb: _tdb:MnU-08Liu.tdb:CUB_A13  


### TDB models of CUB_A13 (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): CUB_A13, type code %, sha256 `edda765ad8b359b9…`

~~~~text
48: PHASE CUB_A13 % 2 1 1 !
49: CONST CUB_A13 : MN% U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Mn–U)

- Id: `phase:mn-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1360–1420 K, x(U) 0–0.00375
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:fcc-a1)

Names (3): _corpus: _corpus:phase:mn-u:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:γMn  
_tdb: _tdb:MnU-08Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): FCC_A1, type code %A, sha256 `edda765ad8b359b9…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MN% U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Mn–U)

- Id: `phase:mn-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:hcp-a3)

Names (2): _corpus: _corpus:phase:mn-u:hcp-a3  
_tdb: _tdb:MnU-08Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): HCP_A3, type code %, sha256 `edda765ad8b359b9…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : MN U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase_

## LIQUID (Mn–U)

- Id: `phase:mn-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 991.35–4000 K, x(U) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:liquid)

Names (3): _corpus: _corpus:phase:mn-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:L  
_tdb: _tdb:MnU-08Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): LIQUID, type code %, sha256 `edda765ad8b359b9…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MN U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## MN2U_C15 (Mn–U)

- Id: `phase:mn-u:mn2u-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.6667, U 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1393.3 K, x(U) 0.33333–0.33333
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:mn2u-c15)

Names (3): _corpus: _corpus:phase:mn-u:mn2u-c15  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:Mn2U  
_tdb: _tdb:MnU-08Liu.tdb:MN2U_C15  


### TDB models of MN2U_C15 (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): MN2U_C15, type code %, sha256 `edda765ad8b359b9…`

~~~~text
63: PHASE MN2U_C15 % 2 2 1 !
64: CONST MN2U_C15 : MN : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## MNU6_D2C (Mn–U)

- Id: `phase:mn-u:mnu6-d2c`; status `assigned`
- Structure: MnU6 · D2_c · tI28 · I4/mcm (140); type `st:d2-c-mnu6-ti28`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.1429, U 0.8571
- Stability: stable in 1 of 1 calculated diagram(s): 300–997.68 K, x(U) 0.85714–0.85714
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:mnu6-d2c)

Names (3): _corpus: _corpus:phase:mn-u:mnu6-d2c  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:MnU6  
_tdb: _tdb:MnU-08Liu.tdb:MNU6_D2C  


### TDB models of MNU6_D2C (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): MNU6_D2C, type code %, sha256 `edda765ad8b359b9…`

~~~~text
68: PHASE MNU6_D2C % 2 1 6 !
69: CONST MNU6_D2C : MN : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
_assessment that models this phase; reports values for this phase_

## TETRAGONAL_U (Mn–U)

- Id: `phase:mn-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — MnU-08Liu.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 1 of 1 calculated diagram(s): 900.86–1055.3 K, x(U) 0.98568–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-u:u-tetragonal)

Names (4): _corpus: _corpus:phase:mn-u:u-tetragonal, corpus:phase:mn-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2008.07.008:βU  
_tdb: _tdb:MnU-08Liu.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (1): PHASE and CONSTITUENT statements as written

[MnU-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb): TETRAGONAL_U, type code %, sha256 `edda765ad8b359b9…`

~~~~text
58: PHASE TETRAGONAL_U % 1 1 !
59: CONST TETRAGONAL_U : MN U% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008).  
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
