# Re–Ru phases

> Re–Ru system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RE-RU.html · Markdown: https://data.orchid-project.org/phases/pages/RE-RU.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RE-RU) · [full JSON](https://data.orchid-project.org/phases/systems/RE-RU.json) · [Re–Ru system page](https://data.orchid-project.org/systems/RE-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/RE-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Re–Ru system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-re-ru-bcc-a2); _phase:re-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-re-ru-fcc-a1); _phase:re-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-re-ru-hcp-a3); _phase:re-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3864.5 K, x(Ru) 0–1 | 0 | 2 |
| [LIQUID](#phase-re-ru-liquid); _phase:re-ru:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 300.25–4000 K, x(Ru) 0–1 | 0 | 2 |

## BCC_A2 (Re–Ru)

- Id: `phase:re-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ru:bcc-a2)

Names (3): _corpus: _corpus:phase:re-ru:bcc-a2  
_tdb: _tdb:ReRu-21Wan.tdb:BCC_A2, tdb:ReRu-21Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ReRu-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Wan.tdb): BCC_A2, type code %B, sha256 `7af6b3fb3e3a8bf0…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : RE RU : VA : !
~~~~

[ReRu-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Zha.tdb): BCC_A2, type code %B, sha256 `dd1305b43cccede4…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : RE RU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102289](https://doi.org/10.1016/j.calphad.2021.102289) C.P. Wang, H. Ren, H. Liu, L.L. Li, S.Y. Yang, J.J. Han, Y. Lu, Y.H. Guo, Y.X. Huang, X.J. Liu, Calphad, 74, 102289(2021).  
_assessment that models this phase_

## FCC_A1 (Re–Ru)

- Id: `phase:re-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ru:fcc-a1)

Names (3): _corpus: _corpus:phase:re-ru:fcc-a1  
_tdb: _tdb:ReRu-21Wan.tdb:FCC_A1, tdb:ReRu-21Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ReRu-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Wan.tdb): FCC_A1, type code %A, sha256 `7af6b3fb3e3a8bf0…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : RE RU : VA : !
~~~~

[ReRu-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Zha.tdb): FCC_A1, type code %A, sha256 `dd1305b43cccede4…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : RE RU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102289](https://doi.org/10.1016/j.calphad.2021.102289) C.P. Wang, H. Ren, H. Liu, L.L. Li, S.Y. Yang, J.J. Han, Y. Lu, Y.H. Guo, Y.X. Huang, X.J. Liu, Calphad, 74, 102289(2021).  
_assessment that models this phase_

## HCP_A3 (Re–Ru)

- Id: `phase:re-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3864.5 K, x(Ru) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ru:hcp-a3)

Names (3): _corpus: _corpus:phase:re-ru:hcp-a3  
_tdb: _tdb:ReRu-21Wan.tdb:HCP_A3, tdb:ReRu-21Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ReRu-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Wan.tdb): HCP_A3, type code %A, sha256 `7af6b3fb3e3a8bf0…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : RE% RU% : VA : !
~~~~

[ReRu-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Zha.tdb): HCP_A3, type code %A, sha256 `dd1305b43cccede4…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : RE% RU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102289](https://doi.org/10.1016/j.calphad.2021.102289) C.P. Wang, H. Ren, H. Liu, L.L. Li, S.Y. Yang, J.J. Han, Y. Lu, Y.H. Guo, Y.X. Huang, X.J. Liu, Calphad, 74, 102289(2021).  
_assessment that models this phase_

## LIQUID (Re–Ru)

- Id: `phase:re-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.25–4000 K, x(Ru) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ru:liquid)

Names (3): _corpus: _corpus:phase:re-ru:liquid  
_tdb: _tdb:ReRu-21Wan.tdb:LIQUID, tdb:ReRu-21Zha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ReRu-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Wan.tdb): LIQUID, type code %, sha256 `7af6b3fb3e3a8bf0…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : RE RU : !
~~~~

[ReRu-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/ReRu-21Zha.tdb): LIQUID, type code %, sha256 `dd1305b43cccede4…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : RE RU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102289](https://doi.org/10.1016/j.calphad.2021.102289) C.P. Wang, H. Ren, H. Liu, L.L. Li, S.Y. Yang, J.J. Han, Y. Lu, Y.H. Guo, Y.X. Huang, X.J. Liu, Calphad, 74, 102289(2021).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
