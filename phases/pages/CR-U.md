# Cr–U phases

> Cr–U system: 6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-U.html · Markdown: https://data.orchid-project.org/phases/pages/CR-U.md

6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-U) · [full JSON](https://data.orchid-project.org/phases/systems/CR-U.json) · [Cr–U system page](https://data.orchid-project.org/systems/CR-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–U system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-cr-u-a20-orthorhombic); _phase:cr-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1047.09 K, x(U) 1–1 | 0 | 1 |
| [BCC_A2](#phase-cr-u-bcc-a2); _phase:cr-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2578.4 K, x(U) 0–1 | 6 | 1 |
| [FCC_A1](#phase-cr-u-fcc-a1); _phase:cr-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cr-u-hcp-a3); _phase:cr-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cr-u-liquid); _phase:cr-u:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1133.4–4000 K, x(U) 0–1 | 2 | 1 |
| [TETRAGONAL_U](#phase-cr-u-u-tetragonal); _phase:cr-u:u-tetragonal_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 912.09–1097.5 K, x(U) 0.98379–1 | 4 | 1 |

## ORTHORHOMBIC_A20 (Cr–U)

- Id: `phase:cr-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1047.09 K, x(U) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-u:a20-orthorhombic)

Names (3): _corpus: _corpus:phase:cr-u:a20-orthorhombic, corpus:phase:cr-u:orthorhombic-a20  
_tdb: _tdb:CrU-11Ber.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (1): PHASE and CONSTITUENT statements as written

[CrU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrU-11Ber.tdb): ORTHORHOMBIC_A20, type code %, sha256 `0603e4a72229dc3b…`

~~~~text
40: PHASE ORTHORHOMBIC_A20 % 1 1 !
41: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## BCC_A2 (Cr–U)

- Id: `phase:cr-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2578.4 K, x(U) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-u:bcc-a2)

Names (4): _corpus: _corpus:phase:cr-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:(Cr), paper:10.1016/j.jnucmat.2011.01.043:(γ-U)  
_tdb: _tdb:CrU-11Ber.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CrU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrU-11Ber.tdb): BCC_A2, type code %B, sha256 `0603e4a72229dc3b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% U% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.440209](https://doi.org/10.1063/1.440209) M. Venkatraman, J.P. Neumann, D.E. Peterson, Bull. Alloy Phase Diagrams 6 (5) (1985) 425–429; M. Venkatraman, J.P. Neumann, D.E. Peterson, J. Chem. Phys. 73 (2) (1980) 908–912.  
_cited as the source of values for this phase_

## FCC_A1 (Cr–U)

- Id: `phase:cr-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-u:fcc-a1)

Names (2): _corpus: _corpus:phase:cr-u:fcc-a1  
_tdb: _tdb:CrU-11Ber.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CrU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrU-11Ber.tdb): FCC_A1, type code %A, sha256 `0603e4a72229dc3b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## HCP_A3 (Cr–U)

- Id: `phase:cr-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-u:hcp-a3)

Names (2): _corpus: _corpus:phase:cr-u:hcp-a3  
_tdb: _tdb:CrU-11Ber.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CrU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrU-11Ber.tdb): HCP_A3, type code %A, sha256 `0603e4a72229dc3b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## LIQUID (Cr–U)

- Id: `phase:cr-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1133.4–4000 K, x(U) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-u:liquid)

Names (3): _corpus: _corpus:phase:cr-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:L  
_tdb: _tdb:CrU-11Ber.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CrU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrU-11Ber.tdb): LIQUID, type code %, sha256 `0603e4a72229dc3b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.440209](https://doi.org/10.1063/1.440209) M. Venkatraman, J.P. Neumann, D.E. Peterson, Bull. Alloy Phase Diagrams 6 (5) (1985) 425–429; M. Venkatraman, J.P. Neumann, D.E. Peterson, J. Chem. Phys. 73 (2) (1980) 908–912.  
_cited as the source of values for this phase_

## TETRAGONAL_U (Cr–U)

- Id: `phase:cr-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — CrU-11Ber.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 1 of 1 calculated diagram(s): 912.09–1097.5 K, x(U) 0.98379–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-u:u-tetragonal)

Names (4): _corpus: _corpus:phase:cr-u:u-tetragonal, corpus:phase:cr-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:(β-U)  
_tdb: _tdb:CrU-11Ber.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (1): PHASE and CONSTITUENT statements as written

[CrU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/CrU-11Ber.tdb): TETRAGONAL_U, type code %, sha256 `0603e4a72229dc3b…`

~~~~text
45: PHASE TETRAGONAL_U % 1 1 !
46: CONST TETRAGONAL_U : CR U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.440209](https://doi.org/10.1063/1.440209) M. Venkatraman, J.P. Neumann, D.E. Peterson, Bull. Alloy Phase Diagrams 6 (5) (1985) 425–429; M. Venkatraman, J.P. Neumann, D.E. Peterson, J. Chem. Phys. 73 (2) (1980) 908–912.  
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
