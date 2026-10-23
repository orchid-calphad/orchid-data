# Au–B phases

> Au–B system: 5 phases (tier A 3, liquid 1, needs_review 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-B.html · Markdown: https://data.orchid-project.org/phases/pages/AU-B.md

5 phases (tier A 3, liquid 1, needs_review 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-B) · [full JSON](https://data.orchid-project.org/phases/systems/AU-B.json) · [Au–B system page](https://data.orchid-project.org/systems/AU-B.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-B.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–B system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-au-b-b-beta-rhombo); _phase:au-b:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–3999.28 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-au-b-bcc-a2); _phase:au-b:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-au-b-fcc-a1); _phase:au-b:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1346.31 K, x(B) 0–0 | 0 | 1 |
| [HCP_A3](#phase-au-b-hcp-a3); _phase:au-b:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-au-b-liquid); _phase:au-b:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1328.81–4000 K, x(B) 0–1 | 0 | 1 |

## BETA_RHOMBO_B (Au–B)

- Id: `phase:au-b:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AuB-98Che-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.28 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-b:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:au-b:b-beta-rhombo  
_tdb: _tdb:AuB-98Che-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[AuB-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuB-98Che-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `556ef1191028605f…`

~~~~text
42: PHASE BETA_RHOMBO_B % 1 1 !
43: CONST BETA_RHOMBO_B : B : !
~~~~

## BCC_A2 (Au–B)

- Id: `phase:au-b:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-b:bcc-a2)

Names (2): _corpus: _corpus:phase:au-b:bcc-a2  
_tdb: _tdb:AuB-98Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuB-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuB-98Che-LB.tdb): BCC_A2, type code %B, sha256 `556ef1191028605f…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AU : VA : !
~~~~

## FCC_A1 (Au–B)

- Id: `phase:au-b:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1346.31 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-b:fcc-a1)

Names (2): _corpus: _corpus:phase:au-b:fcc-a1  
_tdb: _tdb:AuB-98Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuB-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuB-98Che-LB.tdb): FCC_A1, type code %A, sha256 `556ef1191028605f…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AU : VA : !
~~~~

## HCP_A3 (Au–B)

- Id: `phase:au-b:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-b:hcp-a3)

Names (2): _corpus: _corpus:phase:au-b:hcp-a3  
_tdb: _tdb:AuB-98Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuB-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuB-98Che-LB.tdb): HCP_A3, type code %A, sha256 `556ef1191028605f…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AU : VA : !
~~~~

## LIQUID (Au–B)

- Id: `phase:au-b:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1328.81–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-b:liquid)

Names (2): _corpus: _corpus:phase:au-b:liquid  
_tdb: _tdb:AuB-98Che-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuB-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuB-98Che-LB.tdb): LIQUID, type code %, sha256 `556ef1191028605f…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AU B : !
~~~~

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
