# Ru–W phases

> Ru–W system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RU-W.html · Markdown: https://data.orchid-project.org/phases/pages/RU-W.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RU-W) · [full JSON](https://data.orchid-project.org/phases/systems/RU-W.json) · [Ru–W system page](https://data.orchid-project.org/systems/RU-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/RU-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ru–W system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ru-w-bcc-a2); _phase:ru-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.9 K, x(W) 0.76687–1 | 4 | 1 |
| [SIGMA_D8B](#phase-ru-w-d8b-sigma); _phase:ru-w:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1942.46–2571.97 K, x(W) 0.59242–0.61341 | 6 | 1 |
| [FCC_A1](#phase-ru-w-fcc-a1); _phase:ru-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ru-w-hcp-a3); _phase:ru-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2607 K, x(W) 0–0.46456 | 4 | 1 |
| [LIQUID](#phase-ru-w-liquid); _phase:ru-w:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2479.37–4000 K, x(W) 0–1 | 4 | 1 |

## BCC_A2 (Ru–W)

- Id: `phase:ru-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.9 K, x(W) 0.76687–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-w:bcc-a2)

Names (3): _corpus: _corpus:phase:ru-w:bcc-a2  
_paper: _paper:10.1007/s11669-021-00909-6:bcc(W)  
_tdb: _tdb:RuW-21Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[RuW-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuW-21Zha.tdb): BCC_A2, type code %B, sha256 `2bf92cce922c6885…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : RU W% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase; reports values for this phase_

## SIGMA_D8B (Ru–W)

- Id: `phase:ru-w:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in RuW-21Zha.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1942.46–2571.97 K, x(W) 0.59242–0.61341
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-w:d8b-sigma)

Names (4): _corpus: _corpus:phase:ru-w:d8b-sigma, corpus:phase:ru-w:sigma-d8b  
_paper: _paper:10.1007/s11669-021-00909-6:σ(RuW)  
_tdb: _tdb:RuW-21Zha.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (1): PHASE and CONSTITUENT statements as written

[RuW-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuW-21Zha.tdb): SIGMA_D8B, type code %, sha256 `2bf92cce922c6885…`

~~~~text
42: PHASE SIGMA_D8B % 3 10 4 16 !
43: CONST SIGMA_D8B : RU W : W : RU W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ru–W)

- Id: `phase:ru-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-w:fcc-a1)

Names (2): _corpus: _corpus:phase:ru-w:fcc-a1  
_tdb: _tdb:RuW-21Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[RuW-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuW-21Zha.tdb): FCC_A1, type code %A, sha256 `2bf92cce922c6885…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : RU W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase_

## HCP_A3 (Ru–W)

- Id: `phase:ru-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2607 K, x(W) 0–0.46456
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-w:hcp-a3)

Names (3): _corpus: _corpus:phase:ru-w:hcp-a3  
_paper: _paper:10.1007/s11669-021-00909-6:hcp(Ru)  
_tdb: _tdb:RuW-21Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[RuW-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuW-21Zha.tdb): HCP_A3, type code %A, sha256 `2bf92cce922c6885…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : RU% W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ru–W)

- Id: `phase:ru-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2479.37–4000 K, x(W) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-w:liquid)

Names (3): _corpus: _corpus:phase:ru-w:liquid  
_paper: _paper:10.1007/s11669-021-00909-6:L  
_tdb: _tdb:RuW-21Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[RuW-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuW-21Zha.tdb): LIQUID, type code %, sha256 `2bf92cce922c6885…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : RU W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
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
