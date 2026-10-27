# Hf–Ru phases

> Hf–Ru system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-RU.html · Markdown: https://data.orchid-project.org/phases/pages/HF-RU.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-RU) · [full JSON](https://data.orchid-project.org/phases/systems/HF-RU.json) · [Hf–Ru system page](https://data.orchid-project.org/systems/HF-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Ru system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-ru-bcc-a2); _phase:hf-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1583.01–2507.97 K, x(Ru) 0–0.09759 | 0 | 2 |
| [B2_BCC](#phase-hf-ru-bcc-b2); _phase:hf-ru:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2722.49 K, x(Ru) 0–0.52378 | 0 | 1 |
| [FCC_A1](#phase-hf-ru-fcc-a1); _phase:hf-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-hf-ru-hcp-a3); _phase:hf-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3042.95 K, x(Ru) 0–1 | 0 | 1 |
| [LIQUID](#phase-hf-ru-liquid); _phase:hf-ru:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1882.97–4000 K, x(Ru) 0–1 | 0 | 1 |

## BCC_A2 (Hf–Ru)

- Id: `phase:hf-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1583.01–2507.97 K, x(Ru) 0–0.09759
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ru:bcc-a2)

Names (3): _corpus: _corpus:phase:hf-ru:bcc-a2  
_tdb: _tdb:HfRu-21Liu.tdb:A2_BCC, tdb:HfRu-21Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HfRu-21Liu.tdb): A2_BCC, type code %B, sha256 `57aca576778f9191…`

~~~~text
41: PHASE A2_BCC %B 2 1 3 !
42: CONST A2_BCC : HF% RU : VA : !
~~~~

[HfRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HfRu-21Liu.tdb): BCC_A2, type code %B, sha256 `57aca576778f9191…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : HF% RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## B2_BCC (Hf–Ru)

- Id: `phase:hf-ru:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: HfRu-21Liu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in HfRu-21Liu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2722.49 K, x(Ru) 0–0.52378
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ru:bcc-b2)

Names (2): _corpus: _corpus:phase:hf-ru:bcc-b2  
_tdb: _tdb:HfRu-21Liu.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[HfRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HfRu-21Liu.tdb): B2_BCC, type code %BO, sha256 `57aca576778f9191…`

~~~~text
46: PHASE B2_BCC %BO 3 0.5 0.5 3 !
47: CONST B2_BCC : HF% RU : HF RU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## FCC_A1 (Hf–Ru)

- Id: `phase:hf-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ru:fcc-a1)

Names (2): _corpus: _corpus:phase:hf-ru:fcc-a1  
_tdb: _tdb:HfRu-21Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HfRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HfRu-21Liu.tdb): FCC_A1, type code %A, sha256 `57aca576778f9191…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : HF RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## HCP_A3 (Hf–Ru)

- Id: `phase:hf-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3042.95 K, x(Ru) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ru:hcp-a3)

Names (2): _corpus: _corpus:phase:hf-ru:hcp-a3  
_tdb: _tdb:HfRu-21Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HfRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HfRu-21Liu.tdb): HCP_A3, type code %A, sha256 `57aca576778f9191…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : HF% RU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## LIQUID (Hf–Ru)

- Id: `phase:hf-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1882.97–4000 K, x(Ru) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ru:liquid)

Names (2): _corpus: _corpus:phase:hf-ru:liquid  
_tdb: _tdb:HfRu-21Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HfRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HfRu-21Liu.tdb): LIQUID, type code %, sha256 `57aca576778f9191…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : HF RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
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
