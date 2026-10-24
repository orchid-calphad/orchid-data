# N–Ta phases

> N–Ta system: 6 phases (tier A 2, liquid 1, gas 1, needs_review 1, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-TA.html · Markdown: https://data.orchid-project.org/phases/pages/N-TA.md

6 phases (tier A 2, liquid 1, gas 1, needs_review 1, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-TA) · [full JSON](https://data.orchid-project.org/phases/systems/N-TA.json) · [N–Ta system page](https://data.orchid-project.org/systems/N-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–Ta system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-n-ta-bcc-a2); _phase:n-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.96 K, x(N) 0–0.10705 | 0 | 1 |
| [FCC_A1](#phase-n-ta-fcc-a1); _phase:n-ta:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 1 of 1 calculated diagram(s): 1966.92–2281.07 K, x(N) 0.41782–0.44066 | 0 | 1 |
| [HCP_A3](#phase-n-ta-hcp-a3); _phase:n-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2993.7 K, x(N) 0.2347–0.33333 | 0 | 1 |
| [LIQUID](#phase-n-ta-liquid); _phase:n-ta:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2591.13–4000 K, x(N) 0–0.2384 | 0 | 1 |
| [N2GAS](#phase-n-ta-n2gas); _phase:n-ta:n2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(N) 1–1 | 0 | 1 |
| [TAN_EPS](#phase-n-ta-tan-eps); _phase:n-ta:tan-eps_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2079.56 K, x(N) 0.5–0.5 | 0 | 1 |

## BCC_A2 (N–Ta)

- Id: `phase:n-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.96 K, x(N) 0–0.10705
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ta:bcc-a2)

Names (2): _corpus: _corpus:phase:n-ta:bcc-a2  
_tdb: _tdb:TaN-98Fri-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[TaN-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaN-98Fri-LB.tdb): BCC_A2, type code %B, sha256 `1ccb77038a7bdc04…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : TA : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)00582-9](https://doi.org/10.1016/S0925-8388%2898%2900582-9) K. Frisk, J. Alloys Compd., 278, 216-26(1998).  
_assessment that models this phase_

## FCC_A1 (N–Ta)

- Id: `phase:n-ta:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1966.92–2281.07 K, x(N) 0.41782–0.44066
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ta:fcc-a1)

Names (2): _corpus: _corpus:phase:n-ta:fcc-a1  
_tdb: _tdb:TaN-98Fri-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[TaN-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaN-98Fri-LB.tdb): FCC_A1, type code %A, sha256 `1ccb77038a7bdc04…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : TA : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)00582-9](https://doi.org/10.1016/S0925-8388%2898%2900582-9) K. Frisk, J. Alloys Compd., 278, 216-26(1998).  
_assessment that models this phase_

## HCP_A3 (N–Ta)

- Id: `phase:n-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2993.7 K, x(N) 0.2347–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ta:hcp-a3)

Names (2): _corpus: _corpus:phase:n-ta:hcp-a3  
_tdb: _tdb:TaN-98Fri-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[TaN-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaN-98Fri-LB.tdb): HCP_A3, type code %A, sha256 `1ccb77038a7bdc04…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : TA : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)00582-9](https://doi.org/10.1016/S0925-8388%2898%2900582-9) K. Frisk, J. Alloys Compd., 278, 216-26(1998).  
_assessment that models this phase_

## LIQUID (N–Ta)

- Id: `phase:n-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2591.13–4000 K, x(N) 0–0.2384
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ta:liquid)

Names (2): _corpus: _corpus:phase:n-ta:liquid  
_tdb: _tdb:TaN-98Fri-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[TaN-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaN-98Fri-LB.tdb): LIQUID, type code %, sha256 `1ccb77038a7bdc04…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : N TA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)00582-9](https://doi.org/10.1016/S0925-8388%2898%2900582-9) K. Frisk, J. Alloys Compd., 278, 216-26(1998).  
_assessment that models this phase_

## N2GAS (N–Ta)

- Id: `phase:n-ta:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ta:n2gas)

Names (2): _corpus: _corpus:phase:n-ta:n2gas  
_tdb: _tdb:TaN-98Fri-LB.tdb:N2GAS  


### TDB models of N2GAS (1): PHASE and CONSTITUENT statements as written

[TaN-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaN-98Fri-LB.tdb): N2GAS, type code %, sha256 `1ccb77038a7bdc04…`

~~~~text
49: PHASE N2GAS % 1 1 !
50: CONST N2GAS : N2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)00582-9](https://doi.org/10.1016/S0925-8388%2898%2900582-9) K. Frisk, J. Alloys Compd., 278, 216-26(1998).  
_assessment that models this phase_

## TAN_EPS (N–Ta)

- Id: `phase:n-ta:tan-eps`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:EPS; no_structure_token
- Candidate (dft_mp): P-62m (189) — on-hull MP TaN at x(TA)=0.5000
- Candidate (dft_oqmd): P-62m (189) — on-hull OQMD N1 Ta1 at x(TA)=0.5000
- Candidate (sgte_mmc2): TaN-eps · hP6 · P-62m (189) — Hallstedt 2025 mmc2 row for TAN_EPS: TaN-epsilon (LT)
- Candidate (tdb_comment): TaN · hP6 · P-62m — TaN-98Fri-LB.tdb: 'Prototype TaN (hP6, P-62m)'
- Stoichiometry: N 0.5000, Ta 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2079.56 K, x(N) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-ta:tan-eps)

Names (2): _corpus: _corpus:phase:n-ta:tan-eps  
_tdb: _tdb:TaN-98Fri-LB.tdb:TAN_EPS  


### TDB models of TAN_EPS (1): PHASE and CONSTITUENT statements as written

[TaN-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaN-98Fri-LB.tdb): TAN_EPS, type code %, sha256 `1ccb77038a7bdc04…`

~~~~text
46: PHASE TAN_EPS % 2 1 1 !
47: CONST TAN_EPS : TA : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)00582-9](https://doi.org/10.1016/S0925-8388%2898%2900582-9) K. Frisk, J. Alloys Compd., 278, 216-26(1998).  
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
