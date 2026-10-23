# Re–W phases

> Re–W system: 8 phases (tier A 6, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RE-W.html · Markdown: https://data.orchid-project.org/phases/pages/RE-W.md

8 phases (tier A 6, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RE-W) · [full JSON](https://data.orchid-project.org/phases/systems/RE-W.json) · [Re–W system page](https://data.orchid-project.org/systems/RE-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/RE-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Re–W system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [CHI_A12](#phase-re-w-a12-chi); _phase:re-w:a12-chi_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2398.06 K, x(W) 0.17241–0.291 | 7 | 2 |
| [BCC_A2](#phase-re-w-bcc-a2); _phase:re-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3694.9 K, x(W) 0.62691–1 | 7 | 2 |
| [SIGMA_D8B](#phase-re-w-d8b-sigma); _phase:re-w:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 919.01–3271.84 K, x(W) 0.28421–0.5822 | 4 | 2 |
| [DIS_SIGMA](#phase-re-w-dis-sigma); _phase:re-w:dis-sigma_ |  | needs_review | no calculated diagram | 0 | 1 |
| [FCC_A1](#phase-re-w-fcc-a1); _phase:re-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-re-w-hcp-a3); _phase:re-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3459 K, x(W) 0–0.16386 | 7 | 2 |
| [LIQUID](#phase-re-w-liquid); _phase:re-w:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 3103.9–4000 K, x(W) 0–1 | 4 | 2 |
| [SIGMA_OLD](#phase-re-w-old-sigma); _phase:re-w:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 850.63–2490.07 K, x(W) 0.2853–0.56605 | 4 | 1 |

## CHI_A12 (Re–W)

- Id: `phase:re-w:a12-chi`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2398.06 K, x(W) 0.17241–0.291
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:a12-chi)

Names (7): _corpus: _corpus:phase:re-w:a12-chi, corpus:phase:re-w:chi-a12  
_paper: _paper:10.1016/s0925-8388(99)00597-6:hcp (hcp/χ), paper:10.1016/s0925-8388(99)00597-6:χ, paper:10.1016/s0925-8388(99)00597-6:χ (χ/hcp)  
_tdb: _tdb:ReW-00Liu-LB.tdb:CHI_A12, tdb:ReW-02Fri.tdb:CHI_A12  


### TDB models of CHI_A12 (2): PHASE and CONSTITUENT statements as written

[ReW-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb): CHI_A12, type code %, sha256 `d374ef87267bcebe…`

~~~~text
40: PHASE CHI_A12 % 3 24 10 24 !
41: CONST CHI_A12 : RE : RE W : RE W : !
~~~~

[ReW-02Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-02Fri.tdb): CHI_A12, type code %, sha256 `e4eb2c9648c73235…`

~~~~text
47: PHASE CHI_A12 % 3 24 10 24 !
48: CONST CHI_A12 : RE : W : RE W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/PhysRevB.66.012203](https://doi.org/10.1103/PhysRevB.66.012203) S.G. Fries, B. Sundman, Phys. Rev. B, 66, 012203(2002).  
_assessment that models this phase_

## BCC_A2 (Re–W)

- Id: `phase:re-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3694.9 K, x(W) 0.62691–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:bcc-a2)

Names (6): _corpus: _corpus:phase:re-w:bcc-a2  
_paper: _paper:10.1016/s0925-8388(99)00597-6:bcc, paper:10.1016/s0925-8388(99)00597-6:bcc (bcc/σ), paper:10.1016/s0925-8388(99)00597-6:σ (σ/bcc) range high  
_tdb: _tdb:ReW-00Liu-LB.tdb:BCC_A2, tdb:ReW-02Fri.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ReW-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb): BCC_A2, type code %B, sha256 `d374ef87267bcebe…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : RE W% : VA : !
~~~~

[ReW-02Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-02Fri.tdb): BCC_A2, type code %B, sha256 `e4eb2c9648c73235…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : RE W% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/PhysRevB.66.012203](https://doi.org/10.1103/PhysRevB.66.012203) S.G. Fries, B. Sundman, Phys. Rev. B, 66, 012203(2002).  
_assessment that models this phase_

## SIGMA_D8B (Re–W)

- Id: `phase:re-w:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in ReW-02Fri.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 919.01–3271.84 K, x(W) 0.28421–0.5822
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:d8b-sigma)

Names (5): _corpus: _corpus:phase:re-w:d8b-sigma, corpus:phase:re-w:sigma-d8b  
_paper: _paper:10.1016/s0925-8388(99)00597-6:σ  
_tdb: _tdb:ReW-00Liu-LB.tdb:SIGMA_D8B, tdb:ReW-02Fri.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (2): PHASE and CONSTITUENT statements as written

[ReW-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb): SIGMA_D8B, type code %, sha256 `d374ef87267bcebe…`

~~~~text
45: PHASE SIGMA_D8B % 3 10 4 16 !
46: CONST SIGMA_D8B : RE : W : RE W : !
~~~~

[ReW-02Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-02Fri.tdb): SIGMA_D8B, type code %P, sha256 `e4eb2c9648c73235…`

~~~~text
57: PHASE SIGMA_D8B %P 5 2 4 8 8 8 !
58: CONST SIGMA_D8B : RE W : RE W : RE W : RE W : RE W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/PhysRevB.66.012203](https://doi.org/10.1103/PhysRevB.66.012203) S.G. Fries, B. Sundman, Phys. Rev. B, 66, 012203(2002).  
_assessment that models this phase_

## DIS_SIGMA (Re–W)

- Id: `phase:re-w:dis-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:dis-sigma)

Names (2): _corpus: _corpus:phase:re-w:dis-sigma  
_tdb: _tdb:ReW-02Fri.tdb:DIS_SIGMA  


### TDB models of DIS_SIGMA (1): PHASE and CONSTITUENT statements as written

[ReW-02Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-02Fri.tdb): DIS_SIGMA, type code %, sha256 `e4eb2c9648c73235…`

~~~~text
52: PHASE DIS_SIGMA % 1 1 !
53: CONST DIS_SIGMA : RE W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1103/PhysRevB.66.012203](https://doi.org/10.1103/PhysRevB.66.012203) S.G. Fries, B. Sundman, Phys. Rev. B, 66, 012203(2002).  
_assessment that models this phase_

## FCC_A1 (Re–W)

- Id: `phase:re-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:fcc-a1)

Names (3): _corpus: _corpus:phase:re-w:fcc-a1  
_tdb: _tdb:ReW-00Liu-LB.tdb:FCC_A1, tdb:ReW-02Fri.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ReW-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb): FCC_A1, type code %A, sha256 `d374ef87267bcebe…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : RE W : VA : !
~~~~

[ReW-02Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-02Fri.tdb): FCC_A1, type code %A, sha256 `e4eb2c9648c73235…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : RE W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase_
- [doi:10.1103/PhysRevB.66.012203](https://doi.org/10.1103/PhysRevB.66.012203) S.G. Fries, B. Sundman, Phys. Rev. B, 66, 012203(2002).  
_assessment that models this phase_

## HCP_A3 (Re–W)

- Id: `phase:re-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3459 K, x(W) 0–0.16386
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:hcp-a3)

Names (6): _corpus: _corpus:phase:re-w:hcp-a3  
_paper: _paper:10.1016/s0925-8388(99)00597-6:hcp, paper:10.1016/s0925-8388(99)00597-6:σ (σ/(χ or hcp)), paper:10.1016/s0925-8388(99)00597-6:σ (σ/(χ or hcp)) range high  
_tdb: _tdb:ReW-00Liu-LB.tdb:HCP_A3, tdb:ReW-02Fri.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ReW-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb): HCP_A3, type code %A, sha256 `d374ef87267bcebe…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : RE% W : VA : !
~~~~

[ReW-02Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-02Fri.tdb): HCP_A3, type code %A, sha256 `e4eb2c9648c73235…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : RE% W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/PhysRevB.66.012203](https://doi.org/10.1103/PhysRevB.66.012203) S.G. Fries, B. Sundman, Phys. Rev. B, 66, 012203(2002).  
_assessment that models this phase_

## LIQUID (Re–W)

- Id: `phase:re-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 3103.9–4000 K, x(W) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:liquid)

Names (4): _corpus: _corpus:phase:re-w:liquid  
_paper: _paper:10.1016/s0925-8388(99)00597-6:liq  
_tdb: _tdb:ReW-00Liu-LB.tdb:LIQUID, tdb:ReW-02Fri.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ReW-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb): LIQUID, type code %, sha256 `d374ef87267bcebe…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : RE W : !
~~~~

[ReW-02Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-02Fri.tdb): LIQUID, type code %, sha256 `e4eb2c9648c73235…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : RE W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/PhysRevB.66.012203](https://doi.org/10.1103/PhysRevB.66.012203) S.G. Fries, B. Sundman, Phys. Rev. B, 66, 012203(2002).  
_assessment that models this phase_

## SIGMA_OLD (Re–W)

- Id: `phase:re-w:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 850.63–2490.07 K, x(W) 0.2853–0.56605
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-w:old-sigma)

Names (4): _corpus: _corpus:phase:re-w:old-sigma, corpus:phase:re-w:sigma-old  
_paper: _paper:10.1016/s0925-8388(99)00597-6:σ  
_tdb: _tdb:ReW-00Liu-LB.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (1): PHASE and CONSTITUENT statements as written

[ReW-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb): SIGMA_OLD, type code %, sha256 `d374ef87267bcebe…`

~~~~text
50: PHASE SIGMA_OLD % 3 8 4 18 !
51: CONST SIGMA_OLD : RE : W : RE W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
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
