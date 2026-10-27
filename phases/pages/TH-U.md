# Th–U phases

> Th–U system: 8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TH-U.html · Markdown: https://data.orchid-project.org/phases/pages/TH-U.md

8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TH-U) · [full JSON](https://data.orchid-project.org/phases/systems/TH-U.json) · [Th–U system page](https://data.orchid-project.org/systems/TH-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/TH-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Th–U system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-th-u-a20-orthorhombic); _phase:th-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–944.37 K, x(U) 0.99779–1 | 0 | 2 |
| [BCC_A2](#phase-th-u-bcc-a2); _phase:th-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1050–2030.99 K, x(U) 0–1 | 6 | 1 |
| [FCC_A1](#phase-th-u-fcc-a1); _phase:th-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1636.19 K, x(U) 0–0.69 | 4 | 2 |
| [HCP_A3](#phase-th-u-hcp-a3); _phase:th-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-th-u-liquid); _phase:th-u:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1380–4000 K, x(U) 0–1 | 6 | 2 |
| [BCC_TH](#phase-th-u-th-bcc); _phase:th-u:th-bcc_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1380–2022.99 K, x(U) 0–0.09137 | 0 | 1 |
| [BCC_U](#phase-th-u-u-bcc); _phase:th-u:u-bcc_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1048.19–1842.99 K, x(U) 0.26–1 | 0 | 1 |
| [TETRAGONAL_U](#phase-th-u-u-tetragonal); _phase:th-u:u-tetragonal_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 942.02–1403.19 K, x(U) 0.99741–1 | 0 | 2 |

## ORTHORHOMBIC_A20 (Th–U)

- Id: `phase:th-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–944.37 K, x(U) 0.99779–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:a20-orthorhombic)

Names (3): _corpus: _corpus:phase:th-u:a20-orthorhombic  
_tdb: _tdb:ThU-09Li.tdb:ORTHORHOMBIC_A20, tdb:ThU-14Ben.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (2): PHASE and CONSTITUENT statements as written

[ThU-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-09Li.tdb): ORTHORHOMBIC_A20, type code %, sha256 `64caf9670047ca6e…`

~~~~text
42: PHASE ORTHORHOMBIC_A20 % 1 1 !
43: CONST ORTHORHOMBIC_A20 : TH U% : !
~~~~

[ThU-14Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-14Ben.tdb): ORTHORHOMBIC_A20, type code %, sha256 `66891b9d678576aa…`

~~~~text
49: PHASE ORTHORHOMBIC_A20 % 1 1 !
50: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) O. Beneš, D. Manara, R.J.M. Konings, Thermodynamic assessment of the Th–U–Pu system, Journal of Nuclear Materials 449, 15-22 (2014).  
_assessment that models this phase_

## BCC_A2 (Th–U)

- Id: `phase:th-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1050–2030.99 K, x(U) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:bcc-a2)

Names (4): _corpus: _corpus:phase:th-u:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.09.051:βTh, paper:10.1016/j.jallcom.2008.09.051:γU  
_tdb: _tdb:ThU-09Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ThU-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-09Li.tdb): BCC_A2, type code %B, sha256 `64caf9670047ca6e…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : TH% U% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Th–U)

- Id: `phase:th-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1636.19 K, x(U) 0–0.69
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:fcc-a1)

Names (4): _corpus: _corpus:phase:th-u:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2008.09.051:αTh  
_tdb: _tdb:ThU-09Li.tdb:FCC_A1, tdb:ThU-14Ben.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ThU-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-09Li.tdb): FCC_A1, type code %A, sha256 `64caf9670047ca6e…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : TH% U : VA : !
~~~~

[ThU-14Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-14Ben.tdb): FCC_A1, type code %A, sha256 `66891b9d678576aa…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : TH% U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) O. Beneš, D. Manara, R.J.M. Konings, Thermodynamic assessment of the Th–U–Pu system, Journal of Nuclear Materials 449, 15-22 (2014).  
_assessment that models this phase_

## HCP_A3 (Th–U)

- Id: `phase:th-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:hcp-a3)

Names (2): _corpus: _corpus:phase:th-u:hcp-a3  
_tdb: _tdb:ThU-09Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ThU-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-09Li.tdb): HCP_A3, type code %A, sha256 `64caf9670047ca6e…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : TH U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009).  
_assessment that models this phase_

## LIQUID (Th–U)

- Id: `phase:th-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1380–4000 K, x(U) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:liquid)

Names (4): _corpus: _corpus:phase:th-u:liquid  
_paper: _paper:10.1016/j.jallcom.2008.09.051:L2  
_tdb: _tdb:ThU-09Li.tdb:LIQUID, tdb:ThU-14Ben.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ThU-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-09Li.tdb): LIQUID, type code %, sha256 `64caf9670047ca6e…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : TH U : !
~~~~

[ThU-14Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-14Ben.tdb): LIQUID, type code %, sha256 `66891b9d678576aa…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : TH U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) O. Beneš, D. Manara, R.J.M. Konings, Thermodynamic assessment of the Th–U–Pu system, Journal of Nuclear Materials 449, 15-22 (2014).  
_assessment that models this phase_

## BCC_TH (Th–U)

- Id: `phase:th-u:th-bcc`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1380–2022.99 K, x(U) 0–0.09137
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:th-bcc)

Names (2): _corpus: _corpus:phase:th-u:th-bcc  
_tdb: _tdb:ThU-14Ben.tdb:BCC_TH  


### TDB models of BCC_TH (1): PHASE and CONSTITUENT statements as written

[ThU-14Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-14Ben.tdb): BCC_TH, type code %B, sha256 `66891b9d678576aa…`

~~~~text
44: PHASE BCC_TH %B 2 1 3 !
45: CONST BCC_TH : TH% U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) O. Beneš, D. Manara, R.J.M. Konings, Thermodynamic assessment of the Th–U–Pu system, Journal of Nuclear Materials 449, 15-22 (2014).  
_assessment that models this phase_

## BCC_U (Th–U)

- Id: `phase:th-u:u-bcc`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1048.19–1842.99 K, x(U) 0.26–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:u-bcc)

Names (2): _corpus: _corpus:phase:th-u:u-bcc  
_tdb: _tdb:ThU-14Ben.tdb:BCC_U  


### TDB models of BCC_U (1): PHASE and CONSTITUENT statements as written

[ThU-14Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-14Ben.tdb): BCC_U, type code %B, sha256 `66891b9d678576aa…`

~~~~text
39: PHASE BCC_U %B 2 1 3 !
40: CONST BCC_U : TH U% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) O. Beneš, D. Manara, R.J.M. Konings, Thermodynamic assessment of the Th–U–Pu system, Journal of Nuclear Materials 449, 15-22 (2014).  
_assessment that models this phase_

## TETRAGONAL_U (Th–U)

- Id: `phase:th-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — ThU-09Li.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — ThU-14Ben.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 2 of 2 calculated diagram(s): 942.02–1403.19 K, x(U) 0.99741–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:th-u:u-tetragonal)

Names (3): _corpus: _corpus:phase:th-u:u-tetragonal  
_tdb: _tdb:ThU-09Li.tdb:TETRAGONAL_U, tdb:ThU-14Ben.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (2): PHASE and CONSTITUENT statements as written

[ThU-09Li.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-09Li.tdb): TETRAGONAL_U, type code %, sha256 `64caf9670047ca6e…`

~~~~text
47: PHASE TETRAGONAL_U % 1 1 !
48: CONST TETRAGONAL_U : TH U% : !
~~~~

[ThU-14Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ThU-14Ben.tdb): TETRAGONAL_U, type code %, sha256 `66891b9d678576aa…`

~~~~text
54: PHASE TETRAGONAL_U % 1 1 !
55: CONST TETRAGONAL_U : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) O. Beneš, D. Manara, R.J.M. Konings, Thermodynamic assessment of the Th–U–Pu system, Journal of Nuclear Materials 449, 15-22 (2014).  
_assessment that models this phase_

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
