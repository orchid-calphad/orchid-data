# La–Pu phases

> La–Pu system: 11 phases (tier A 6, liquid 1, needs_review 4); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LA-PU.html · Markdown: https://data.orchid-project.org/phases/pages/LA-PU.md

11 phases (tier A 6, liquid 1, needs_review 4); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LA-PU) · [full JSON](https://data.orchid-project.org/phases/systems/LA-PU.json) · [La–Pu system page](https://data.orchid-project.org/systems/LA-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/LA-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the La–Pu system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-la-pu-a6-tetragonal); _phase:la-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 736.13–760.89 K, x(Pu) 0.99815–1 | 9 | 1 |
| [BCC_A2](#phase-la-pu-bcc-a2); _phase:la-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 753.89–1240.14 K, x(Pu) 0–1 | 6 | 1 |
| [DHCP](#phase-la-pu-dhcp); _phase:la-pu:dhcp_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 0 |
| [DHCP](#phase-la-pu-dhcp-a3); _phase:la-pu:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1134.99 K, x(Pu) 0–0 | 0 | 1 |
| [FCC_A1](#phase-la-pu-fcc-a1); _phase:la-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 472.48–1134.99 K, x(Pu) 0–1 | 19 | 1 |
| [FCC-A1-2](#phase-la-pu-fcc-a1-2); _phase:la-pu:fcc-a1-2_ |  | needs_review | no calculated diagram | 0 | 0 |
| [HCP_A3](#phase-la-pu-hcp-a3); _phase:la-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-la-pu-liquid); _phase:la-pu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 912.12–4000 K, x(Pu) 0–1 | 11 | 1 |
| [ALPHA_PU](#phase-la-pu-pu-alpha); _phase:la-pu:pu-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1 | 3 | 1 |
| [BETA_PU](#phase-la-pu-pu-beta); _phase:la-pu:pu-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1 | 5 | 1 |
| [GAMMA_PU](#phase-la-pu-pu-gamma); _phase:la-pu:pu-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 487.9–727.04 K, x(Pu) 1–1 | 13 | 1 |

## TETRAGONAL_A6 (La–Pu)

- Id: `phase:la-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 736.13–760.89 K, x(Pu) 0.99815–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:a6-tetragonal)

Names (5): _corpus: _corpus:phase:la-pu:a6-tetragonal, corpus:phase:la-pu:tetragonal-a6  
_paper: _paper:10.1016/j.jnucmat.2014.07.001:(δ'Pu), paper:10.1016/j.jnucmat.2014.07.001:(δPu)  
_tdb: _tdb:LaPu-14Liu.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): TETRAGONAL_A6, type code %, sha256 `b876dfcc548ef419…`

~~~~text
47: PHASE TETRAGONAL_A6 % 1 1 !
48: CONST TETRAGONAL_A6 : LA PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (La–Pu)

- Id: `phase:la-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 753.89–1240.14 K, x(Pu) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:bcc-a2)

Names (3): _corpus: _corpus:phase:la-pu:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2014.07.001:(εPu)  
_tdb: _tdb:LaPu-14Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): BCC_A2, type code %B, sha256 `b876dfcc548ef419…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : LA% PU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase; reports values for this phase_

## DHCP (La–Pu)

- Id: `phase:la-pu:dhcp`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:dhcp)

Names (1): _corpus: _corpus:phase:la-pu:dhcp  


## DHCP (La–Pu)

- Id: `phase:la-pu:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1134.99 K, x(Pu) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:dhcp-a3)

Names (2): _corpus: _corpus:phase:la-pu:dhcp-a3  
_tdb: _tdb:LaPu-14Liu.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): DHCP, type code %, sha256 `b876dfcc548ef419…`

~~~~text
42: PHASE DHCP % 1 1 !
43: CONST DHCP : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase_

## FCC_A1 (La–Pu)

- Id: `phase:la-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 472.48–1134.99 K, x(Pu) 0–1
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:fcc-a1)

Names (3): _corpus: _corpus:phase:la-pu:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2014.07.001:(βLa)  
_tdb: _tdb:LaPu-14Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): FCC_A1, type code %A, sha256 `b876dfcc548ef419…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : LA% PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase; reports values for this phase_

## FCC-A1-2 (La–Pu)

- Id: `phase:la-pu:fcc-a1-2`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:2
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:fcc-a1-2)

Names (1): _corpus: _corpus:phase:la-pu:fcc-a1-2  


## HCP_A3 (La–Pu)

- Id: `phase:la-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:hcp-a3)

Names (2): _corpus: _corpus:phase:la-pu:hcp-a3  
_tdb: _tdb:LaPu-14Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): HCP_A3, type code %A, sha256 `b876dfcc548ef419…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase_

## LIQUID (La–Pu)

- Id: `phase:la-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 912.12–4000 K, x(Pu) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:liquid)

Names (4): _corpus: _corpus:phase:la-pu:liquid  
_paper: _paper:10.1016/j.jnucmat.2014.07.001:L1, paper:10.1016/j.jnucmat.2014.07.001:L2  
_tdb: _tdb:LaPu-14Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): LIQUID, type code %, sha256 `b876dfcc548ef419…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : LA PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase; reports values for this phase_

## ALPHA_PU (La–Pu)

- Id: `phase:la-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): alpha-Pu · mP16 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — LaPu-14Liu.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:pu-alpha)

Names (4): _corpus: _corpus:phase:la-pu:pu-alpha  
_paper: _paper:10.1016/j.jnucmat.2014.07.001:(αLa), paper:10.1016/j.jnucmat.2014.07.001:(αPu)  
_tdb: _tdb:LaPu-14Liu.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): ALPHA_PU, type code %, sha256 `b876dfcc548ef419…`

~~~~text
52: PHASE ALPHA_PU % 1 1 !
53: CONST ALPHA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase; reports values for this phase_

## BETA_PU (La–Pu)

- Id: `phase:la-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): beta-Pu · mC34 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — LaPu-14Liu.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:pu-beta)

Names (4): _corpus: _corpus:phase:la-pu:pu-beta, corpus:phase:la-pu:beta-pu  
_paper: _paper:10.1016/j.jnucmat.2014.07.001:(βPu)  
_tdb: _tdb:LaPu-14Liu.tdb:BETA_PU  


### TDB models of BETA_PU (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): BETA_PU, type code %, sha256 `b876dfcc548ef419…`

~~~~text
57: PHASE BETA_PU % 1 1 !
58: CONST BETA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
_assessment that models this phase; reports values for this phase_

## GAMMA_PU (La–Pu)

- Id: `phase:la-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (literature_printed): gamma-Pu · oF8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — LaPu-14Liu.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 487.9–727.04 K, x(Pu) 1–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-pu:pu-gamma)

Names (5): _corpus: _corpus:phase:la-pu:pu-gamma, corpus:phase:la-pu:gamma-pu  
_paper: _paper:10.1016/j.jnucmat.2014.07.001:(γLa), paper:10.1016/j.jnucmat.2014.07.001:(γPu)  
_tdb: _tdb:LaPu-14Liu.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (1): PHASE and CONSTITUENT statements as written

[LaPu-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/LaPu-14Liu.tdb): GAMMA_PU, type code %, sha256 `b876dfcc548ef419…`

~~~~text
62: PHASE GAMMA_PU % 1 1 !
63: CONST GAMMA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2014.07.001](https://doi.org/10.1016/j.jnucmat.2014.07.001) X.J. Liu, Q. He, D. Wang, Y. Lu, M.H. Chen, J.P. Jia et al., Thermodynamic assessments of the Pu–Zn and La–Pu systems, Journal of Nuclear Materials 453, 169-175 (2014).  
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
