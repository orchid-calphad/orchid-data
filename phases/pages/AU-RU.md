# Au–Ru phases

> Au–Ru system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-RU.html · Markdown: https://data.orchid-project.org/phases/pages/AU-RU.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-RU) · [full JSON](https://data.orchid-project.org/phases/systems/AU-RU.json) · [Au–Ru system page](https://data.orchid-project.org/systems/AU-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Ru system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-au-ru-bcc-a2); _phase:au-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-au-ru-fcc-a1); _phase:au-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1339.45 K, x(Ru) 0–0.00816 | 0 | 2 |
| [HCP_A3](#phase-au-ru-hcp-a3); _phase:au-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.91 K, x(Ru) 0.99995–1 | 0 | 2 |
| [LIQUID](#phase-au-ru-liquid); _phase:au-ru:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1337.33–4000 K, x(Ru) 0–1 | 19 | 2 |

## BCC_A2 (Au–Ru)

- Id: `phase:au-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ru:bcc-a2)

Names (3): _corpus: _corpus:phase:au-ru:bcc-a2  
_tdb: _tdb:AuRu-84Oka.tdb:BCC_A2, tdb:AuRu-98Spe-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AuRu-84Oka.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-84Oka.tdb): BCC_A2, type code %B, sha256 `431b1a82358b61e6…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AU RU : VA : !
~~~~

[AuRu-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-98Spe-LB.tdb): BCC_A2, type code %B, sha256 `21a44838d8ab9cba…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AU RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02872961](https://doi.org/10.1007/BF02872961) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diag., 5, 388-90(1984).  
_assessment that models this phase_

## FCC_A1 (Au–Ru)

- Id: `phase:au-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1339.45 K, x(Ru) 0–0.00816
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ru:fcc-a1)

Names (3): _corpus: _corpus:phase:au-ru:fcc-a1  
_tdb: _tdb:AuRu-84Oka.tdb:FCC_A1, tdb:AuRu-98Spe-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AuRu-84Oka.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-84Oka.tdb): FCC_A1, type code %A, sha256 `431b1a82358b61e6…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AU% RU : VA : !
~~~~

[AuRu-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-98Spe-LB.tdb): FCC_A1, type code %A, sha256 `21a44838d8ab9cba…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AU% RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02872961](https://doi.org/10.1007/BF02872961) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diag., 5, 388-90(1984).  
_assessment that models this phase_

## HCP_A3 (Au–Ru)

- Id: `phase:au-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.91 K, x(Ru) 0.99995–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ru:hcp-a3)

Names (3): _corpus: _corpus:phase:au-ru:hcp-a3  
_tdb: _tdb:AuRu-84Oka.tdb:HCP_A3, tdb:AuRu-98Spe-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AuRu-84Oka.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-84Oka.tdb): HCP_A3, type code %A, sha256 `431b1a82358b61e6…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AU RU% : VA : !
~~~~

[AuRu-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-98Spe-LB.tdb): HCP_A3, type code %A, sha256 `21a44838d8ab9cba…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AU RU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02872961](https://doi.org/10.1007/BF02872961) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diag., 5, 388-90(1984).  
_assessment that models this phase_

## LIQUID (Au–Ru)

- Id: `phase:au-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1337.33–4000 K, x(Ru) 0–1
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ru:liquid)

Names (5): _corpus: _corpus:phase:au-ru:liquid  
_paper: _paper:10.1007/bf02872961:L, paper:10.1007/bf02872961:L2  
_tdb: _tdb:AuRu-84Oka.tdb:LIQUID, tdb:AuRu-98Spe-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AuRu-84Oka.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-84Oka.tdb): LIQUID, type code %, sha256 `431b1a82358b61e6…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AU RU : !
~~~~

[AuRu-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuRu-98Spe-LB.tdb): LIQUID, type code %, sha256 `21a44838d8ab9cba…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AU RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02872961](https://doi.org/10.1007/BF02872961) H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diag., 5, 388-90(1984).  
_assessment that models this phase; reports values for this phase_

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
