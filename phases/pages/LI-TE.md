# Li–Te phases

> Li–Te system: 7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LI-TE.html · Markdown: https://data.orchid-project.org/phases/pages/LI-TE.md

7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LI-TE) · [full JSON](https://data.orchid-project.org/phases/systems/LI-TE.json) · [Li–Te system page](https://data.orchid-project.org/systems/LI-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/LI-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Li–Te system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-li-te-a8-hexagonal); _phase:li-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 4 | 1 |
| [BCC_A2](#phase-li-te-bcc-a2); _phase:li-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.85 K, x(Te) 0–0 | 2 | 1 |
| [FCC_A1](#phase-li-te-fcc-a1); _phase:li-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-li-te-hcp-a3); _phase:li-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LI2TE_C1](#phase-li-te-li2te-c1); _phase:li-te:li2te-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1528.07 K, x(Te) 0.33333–0.33333 | 10 | 1 |
| [LIQUID](#phase-li-te-liquid); _phase:li-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 453.6–2500 K, x(Te) 0–1 | 12 | 1 |
| [LITE3](#phase-li-te-lite3); _phase:li-te:lite3_ | LiTe3 · hP48 · P-3c1 (165) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 575.2–732.82 K, x(Te) 0.75–0.75 | 10 | 1 |

## HEXAGONAL_A8 (Li–Te)

- Id: `phase:li-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:li-te:a8-hexagonal, corpus:phase:li-te:hexagonal-a8  
_paper: _paper:10.1007/s11669-022-00950-z:(Te)  
_tdb: _tdb:LiTe-22Yu.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[LiTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb): HEXAGONAL_A8, type code %, sha256 `036b3481f222317d…`

~~~~text
48: PHASE HEXAGONAL_A8 % 1 1 !
49: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667559](https://doi.org/10.1007/bf02667559) J. Songster, A. D. Pelton, The li-te (lithium-tellurium) system, JPE 13, 300-303 (1992).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2403448](https://doi.org/10.1149/1.2403448) P. T. Cunningham, S. A. Johnson, E. J. Cairns, Phase Equilibria in Lithium-Chalcogen Systems, J. Electrochem. Soc. 120, 328 (1973).  
_cited as the source of values for this phase_

## BCC_A2 (Li–Te)

- Id: `phase:li-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.85 K, x(Te) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-te:bcc-a2)

Names (3): _corpus: _corpus:phase:li-te:bcc-a2  
_paper: _paper:10.1007/s11669-022-00950-z:(Li)  
_tdb: _tdb:LiTe-22Yu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LiTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb): BCC_A2, type code %B, sha256 `036b3481f222317d…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2403448](https://doi.org/10.1149/1.2403448) P. T. Cunningham, S. A. Johnson, E. J. Cairns, Phase Equilibria in Lithium-Chalcogen Systems, J. Electrochem. Soc. 120, 328 (1973).  
_cited as the source of values for this phase_

## FCC_A1 (Li–Te)

- Id: `phase:li-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-te:fcc-a1)

Names (2): _corpus: _corpus:phase:li-te:fcc-a1  
_tdb: _tdb:LiTe-22Yu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LiTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb): FCC_A1, type code %A, sha256 `036b3481f222317d…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : LI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase_

## HCP_A3 (Li–Te)

- Id: `phase:li-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-te:hcp-a3)

Names (2): _corpus: _corpus:phase:li-te:hcp-a3  
_tdb: _tdb:LiTe-22Yu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LiTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb): HCP_A3, type code %A, sha256 `036b3481f222317d…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : LI : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase_

## LI2TE_C1 (Li–Te)

- Id: `phase:li-te:li2te-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadti and oqmd-11316, space group 225
- Stoichiometry: Li 0.6667, Te 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1528.07 K, x(Te) 0.33333–0.33333
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-te:li2te-c1)

Names (5): _corpus: _corpus:phase:li-te:li2te-c1  
_mp: _mp:mp-aaaaadti  
_oqmd: _oqmd:oqmd-11316  
_paper: _paper:10.1007/s11669-022-00950-z:Li2Te  
_tdb: _tdb:LiTe-22Yu.tdb:LI2TE_C1  


### TDB models of LI2TE_C1 (1): PHASE and CONSTITUENT statements as written

[LiTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb): LI2TE_C1, type code %, sha256 `036b3481f222317d…`

~~~~text
53: PHASE LI2TE_C1 % 2 2 1 !
54: CONST LI2TE_C1 : LI : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2403448](https://doi.org/10.1149/1.2403448) P. T. Cunningham, S. A. Johnson, E. J. Cairns, Phase Equilibria in Lithium-Chalcogen Systems, J. Electrochem. Soc. 120, 328 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667559](https://doi.org/10.1007/bf02667559) J. Songster, A. D. Pelton, The li-te (lithium-tellurium) system, JPE 13, 300-303 (1992).  
_cited as the source of values for this phase_

## LIQUID (Li–Te)

- Id: `phase:li-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 453.6–2500 K, x(Te) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-te:liquid)

Names (4): _corpus: _corpus:phase:li-te:liquid  
_paper: _paper:10.1007/s11669-022-00950-z:L, paper:10.1007/s11669-022-00950-z:L1  
_tdb: _tdb:LiTe-22Yu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LiTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb): LIQUID, type code %, sha256 `036b3481f222317d…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : LI LI2TE TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2403448](https://doi.org/10.1149/1.2403448) P. T. Cunningham, S. A. Johnson, E. J. Cairns, Phase Equilibria in Lithium-Chalcogen Systems, J. Electrochem. Soc. 120, 328 (1973).  
_cited as the source of values for this phase_

## LITE3 (Li–Te)

- Id: `phase:li-te:lite3`; status `assigned`
- Structure: LiTe3 · hP48 · P-3c1 (165); type `st:lite3-hp48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Li 0.2500, Te 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 575.2–732.82 K, x(Te) 0.75–0.75
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-te:lite3)

Names (3): _corpus: _corpus:phase:li-te:lite3  
_paper: _paper:10.1007/s11669-022-00950-z:LiTe3  
_tdb: _tdb:LiTe-22Yu.tdb:LITE3  


### TDB models of LITE3 (1): PHASE and CONSTITUENT statements as written

[LiTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb): LITE3, type code %, sha256 `036b3481f222317d…`

~~~~text
58: PHASE LITE3 % 2 1 3 !
59: CONST LITE3 : LI : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2403448](https://doi.org/10.1149/1.2403448) P. T. Cunningham, S. A. Johnson, E. J. Cairns, Phase Equilibria in Lithium-Chalcogen Systems, J. Electrochem. Soc. 120, 328 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667559](https://doi.org/10.1007/bf02667559) J. Songster, A. D. Pelton, The li-te (lithium-tellurium) system, JPE 13, 300-303 (1992).  
_cited as the source of values for this phase_

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
