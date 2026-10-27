# B–Cd phases

> B–Cd system: 6 phases (tier A 3, liquid 1, needs_review 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-CD.html · Markdown: https://data.orchid-project.org/phases/pages/B-CD.md

6 phases (tier A 3, liquid 1, needs_review 2); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-CD) · [full JSON](https://data.orchid-project.org/phases/systems/B-CD.json) · [B–Cd system page](https://data.orchid-project.org/systems/B-CD.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-CD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Cd system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-cd-b-alpha-rhombo); _phase:b-cd:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-cd-b-beta-rhombo); _phase:b-cd:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2351 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-cd-bcc-a2); _phase:b-cd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-b-cd-fcc-a1); _phase:b-cd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-cd-hcp-a3); _phase:b-cd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–594.17 K, x(B) 0–0 | 0 | 1 |
| [LIQUID](#phase-b-cd-liquid); _phase:b-cd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 594.17–4000 K, x(B) 0–1 | 0 | 1 |

## ALPHA_RHOMBO_B (B–Cd)

- Id: `phase:b-cd:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — CdB-13Zha.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cd:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-cd:b-alpha-rhombo  
_tdb: _tdb:CdB-13Zha.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[CdB-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdB-13Zha.tdb): ALPHA_RHOMBO_B, type code %, sha256 `117484c482c2e747…`

~~~~text
41: PHASE ALPHA_RHOMBO_B % 1 1 !
42: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Cd)

- Id: `phase:b-cd:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CdB-13Zha.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2351 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cd:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-cd:b-beta-rhombo  
_tdb: _tdb:CdB-13Zha.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[CdB-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdB-13Zha.tdb): BETA_RHOMBO_B, type code %, sha256 `117484c482c2e747…`

~~~~text
46: PHASE BETA_RHOMBO_B % 1 1 !
47: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## BCC_A2 (B–Cd)

- Id: `phase:b-cd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cd:bcc-a2)

Names (2): _corpus: _corpus:phase:b-cd:bcc-a2  
_tdb: _tdb:CdB-13Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdB-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdB-13Zha.tdb): BCC_A2, type code %B, sha256 `117484c482c2e747…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## FCC_A1 (B–Cd)

- Id: `phase:b-cd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cd:fcc-a1)

Names (2): _corpus: _corpus:phase:b-cd:fcc-a1  
_tdb: _tdb:CdB-13Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdB-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdB-13Zha.tdb): FCC_A1, type code %A, sha256 `117484c482c2e747…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## HCP_A3 (B–Cd)

- Id: `phase:b-cd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–594.17 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cd:hcp-a3)

Names (2): _corpus: _corpus:phase:b-cd:hcp-a3  
_tdb: _tdb:CdB-13Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdB-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdB-13Zha.tdb): HCP_A3, type code %A, sha256 `117484c482c2e747…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## LIQUID (B–Cd)

- Id: `phase:b-cd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 594.17–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-cd:liquid)

Names (2): _corpus: _corpus:phase:b-cd:liquid  
_tdb: _tdb:CdB-13Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdB-13Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CdB-13Zha.tdb): LIQUID, type code %, sha256 `117484c482c2e747…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : B CD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
