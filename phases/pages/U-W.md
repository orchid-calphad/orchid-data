# U–W phases

> U–W system: 6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/U-W.html · Markdown: https://data.orchid-project.org/phases/pages/U-W.md

6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=U-W) · [full JSON](https://data.orchid-project.org/phases/systems/U-W.json) · [U–W system page](https://data.orchid-project.org/systems/U-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/U-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the U–W system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-u-w-a20-orthorhombic); _phase:u-w:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–947.02 K, x(W) 0–0 | 0 | 2 |
| [BCC_A2](#phase-u-w-bcc-a2); _phase:u-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.88 K, x(W) 0–1 | 8 | 2 |
| [FCC_A1](#phase-u-w-fcc-a1); _phase:u-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-u-w-hcp-a3); _phase:u-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-u-w-liquid); _phase:u-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1404.22–4000 K, x(W) 0–1 | 19 | 2 |
| [TETRAGONAL_U](#phase-u-w-u-tetragonal); _phase:u-w:u-tetragonal_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 942.02–1089.95 K, x(W) 0–1e-05 | 2 | 2 |

## ORTHORHOMBIC_A20 (U–W)

- Id: `phase:u-w:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–947.02 K, x(W) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-w:a20-orthorhombic)

Names (4): _corpus: _corpus:phase:u-w:a20-orthorhombic, corpus:phase:u-w:orthorhombic-a20  
_tdb: _tdb:UW-08Wan.tdb:ORTHORHOMBIC_A20, tdb:UW-11Ber.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (2): PHASE and CONSTITUENT statements as written

[UW-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-08Wan.tdb): ORTHORHOMBIC_A20, type code %, sha256 `b39bc5b283c025c0…`

~~~~text
40: PHASE ORTHORHOMBIC_A20 % 1 1 !
41: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[UW-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-11Ber.tdb): ORTHORHOMBIC_A20, type code %, sha256 `4aad821713451c83…`

~~~~text
41: PHASE ORTHORHOMBIC_A20 % 1 1 !
42: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic calculation of phase equilibria of the U–Ga and U–W systems, Journal of Nuclear Materials 380, 105-110 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## BCC_A2 (U–W)

- Id: `phase:u-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.88 K, x(W) 0–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-w:bcc-a2)

Names (7): _corpus: _corpus:phase:u-w:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2008.07.009:bcc (W), paper:10.1016/j.jnucmat.2008.07.009:β (U), paper:10.1016/j.jnucmat.2011.01.043:(W), paper:10.1016/j.jnucmat.2011.01.043:(γ-U)  
_tdb: _tdb:UW-08Wan.tdb:BCC_A2, tdb:UW-11Ber.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[UW-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-08Wan.tdb): BCC_A2, type code %B, sha256 `b39bc5b283c025c0…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : U% W% : VA : !
~~~~

[UW-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-11Ber.tdb): BCC_A2, type code %B, sha256 `4aad821713451c83…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : U% W% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic calculation of phase equilibria of the U–Ga and U–W systems, Journal of Nuclear Materials 380, 105-110 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (U–W)

- Id: `phase:u-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-w:fcc-a1)

Names (3): _corpus: _corpus:phase:u-w:fcc-a1  
_tdb: _tdb:UW-08Wan.tdb:FCC_A1, tdb:UW-11Ber.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[UW-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-08Wan.tdb): FCC_A1, type code %A, sha256 `b39bc5b283c025c0…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : U W : VA : !
~~~~

[UW-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-11Ber.tdb): FCC_A1, type code %A, sha256 `4aad821713451c83…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : U W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic calculation of phase equilibria of the U–Ga and U–W systems, Journal of Nuclear Materials 380, 105-110 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## HCP_A3 (U–W)

- Id: `phase:u-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-w:hcp-a3)

Names (3): _corpus: _corpus:phase:u-w:hcp-a3  
_tdb: _tdb:UW-08Wan.tdb:HCP_A3, tdb:UW-11Ber.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[UW-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-08Wan.tdb): HCP_A3, type code %A, sha256 `b39bc5b283c025c0…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : U W : VA : !
~~~~

[UW-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-11Ber.tdb): HCP_A3, type code %A, sha256 `4aad821713451c83…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : U W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic calculation of phase equilibria of the U–Ga and U–W systems, Journal of Nuclear Materials 380, 105-110 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## LIQUID (U–W)

- Id: `phase:u-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1404.22–4000 K, x(W) 0–1
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-w:liquid)

Names (6): _corpus: _corpus:phase:u-w:liquid  
_paper: _paper:10.1016/j.jnucmat.2008.07.009:L, paper:10.1016/j.jnucmat.2008.07.009:liquid, paper:10.1016/j.jnucmat.2011.01.043:L  
_tdb: _tdb:UW-08Wan.tdb:LIQUID, tdb:UW-11Ber.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[UW-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-08Wan.tdb): LIQUID, type code %, sha256 `b39bc5b283c025c0…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : U W : !
~~~~

[UW-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-11Ber.tdb): LIQUID, type code %, sha256 `4aad821713451c83…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : U W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic calculation of phase equilibria of the U–Ga and U–W systems, Journal of Nuclear Materials 380, 105-110 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_

## TETRAGONAL_U (U–W)

- Id: `phase:u-w:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UW-08Wan.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UW-11Ber.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 2 of 2 calculated diagram(s): 942.02–1089.95 K, x(W) 0–1e-05
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:u-w:u-tetragonal)

Names (5): _corpus: _corpus:phase:u-w:u-tetragonal, corpus:phase:u-w:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:(β-U)  
_tdb: _tdb:UW-08Wan.tdb:TETRAGONAL_U, tdb:UW-11Ber.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (2): PHASE and CONSTITUENT statements as written

[UW-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-08Wan.tdb): TETRAGONAL_U, type code %, sha256 `b39bc5b283c025c0…`

~~~~text
45: PHASE TETRAGONAL_U % 1 1 !
46: CONST TETRAGONAL_U : U : !
~~~~

[UW-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/UW-11Ber.tdb): TETRAGONAL_U, type code %, sha256 `4aad821713451c83…`

~~~~text
46: PHASE TETRAGONAL_U % 1 1 !
47: CONST TETRAGONAL_U : U% W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic calculation of phase equilibria of the U–Ga and U–W systems, Journal of Nuclear Materials 380, 105-110 (2008).  
_assessment that models this phase_

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
