# Rh–Ti phases

> Rh–Ti system: 8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RH-TI.html · Markdown: https://data.orchid-project.org/phases/pages/RH-TI.md

8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RH-TI) · [full JSON](https://data.orchid-project.org/phases/systems/RH-TI.json) · [Rh–Ti system page](https://data.orchid-project.org/systems/RH-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/RH-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Rh–Ti system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [A2_BCC](#phase-rh-ti-bcc-a2); _phase:rh-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 535.24–1840 K, x(Ti) 0.75–1 | 0 | 2 |
| [B2_BCC](#phase-rh-ti-bcc-b2); _phase:rh-ti:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2221.79 K, x(Ti) 0.37495–1 | 0 | 1 |
| [A1_FCC](#phase-rh-ti-fcc-a1); _phase:rh-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [L12_FCC](#phase-rh-ti-fcc-l12); _phase:rh-ti:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2237 K, x(Ti) 0–0.28094 | 0 | 1 |
| [HCP_A3](#phase-rh-ti-hcp-a3); _phase:rh-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 0.99758–1 | 0 | 1 |
| [LIQUID](#phase-rh-ti-liquid); _phase:rh-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1555.98–4000 K, x(Ti) 0–1 | 0 | 1 |
| [RH5TI3](#phase-rh-ti-rh5ti3); _phase:rh-ti:rh5ti3_ | Ge3Rh5 · oP16 · Pbam (55) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2115.61 K, x(Ti) 0.375–0.375 | 0 | 1 |
| [RHTI2](#phase-rh-ti-rhti2); _phase:rh-ti:rhti2_ | CuZr2 · tI6 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1085 K, x(Ti) 0.66667–0.66667 | 0 | 1 |

## A2_BCC (Rh–Ti)

- Id: `phase:rh-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 535.24–1840 K, x(Ti) 0.75–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:bcc-a2)

Names (3): _corpus: _corpus:phase:rh-ti:bcc-a2  
_tdb: _tdb:RhTi-22Hu.tdb:A2_BCC, tdb:RhTi-22Hu.tdb:BCC_A2  


### TDB models of A2_BCC (2): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): A2_BCC, type code %B, sha256 `9a0f1ecc0389a4aa…`

~~~~text
49: PHASE A2_BCC %B 2 1 3 !
50: CONST A2_BCC : RH TI% : VA : !
~~~~

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): BCC_A2, type code %B, sha256 `9a0f1ecc0389a4aa…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : RH TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
_assessment that models this phase_

## B2_BCC (Rh–Ti)

- Id: `phase:rh-ti:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: RhTi-22Hu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in RhTi-22Hu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2221.79 K, x(Ti) 0.37495–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:bcc-b2)

Names (2): _corpus: _corpus:phase:rh-ti:bcc-b2  
_tdb: _tdb:RhTi-22Hu.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): B2_BCC, type code %BO, sha256 `9a0f1ecc0389a4aa…`

~~~~text
54: PHASE B2_BCC %BO 3 0.5 0.5 3 !
55: CONST B2_BCC : RH% TI : RH TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
_assessment that models this phase_

## A1_FCC (Rh–Ti)

- Id: `phase:rh-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:rh-ti:fcc-a1  
_tdb: _tdb:RhTi-22Hu.tdb:A1_FCC, tdb:RhTi-22Hu.tdb:FCC_A1  


### TDB models of A1_FCC (2): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): A1_FCC, type code %A, sha256 `9a0f1ecc0389a4aa…`

~~~~text
34: PHASE A1_FCC %A 2 1 1 !
35: CONST A1_FCC : RH% TI : VA : !
~~~~

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): FCC_A1, type code %A, sha256 `9a0f1ecc0389a4aa…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : RH% TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
_assessment that models this phase_

## L12_FCC (Rh–Ti)

- Id: `phase:rh-ti:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: RhTi-22Hu.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in RhTi-22Hu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2237 K, x(Ti) 0–0.28094
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:fcc-l12)

Names (2): _corpus: _corpus:phase:rh-ti:fcc-l12  
_tdb: _tdb:RhTi-22Hu.tdb:L12_FCC  


### TDB models of L12_FCC (1): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): L12_FCC, type code %AY, sha256 `9a0f1ecc0389a4aa…`

~~~~text
39: PHASE L12_FCC %AY 3 0.75 0.25 1 !
40: CONST L12_FCC : RH% TI : RH TI% : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
_assessment that models this phase_

## HCP_A3 (Rh–Ti)

- Id: `phase:rh-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 0.99758–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:hcp-a3)

Names (2): _corpus: _corpus:phase:rh-ti:hcp-a3  
_tdb: _tdb:RhTi-22Hu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): HCP_A3, type code %A, sha256 `9a0f1ecc0389a4aa…`

~~~~text
59: PHASE HCP_A3 %A 2 1 0.5 !
60: CONST HCP_A3 : RH TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
_assessment that models this phase_

## LIQUID (Rh–Ti)

- Id: `phase:rh-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1555.98–4000 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:liquid)

Names (2): _corpus: _corpus:phase:rh-ti:liquid  
_tdb: _tdb:RhTi-22Hu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): LIQUID, type code %, sha256 `9a0f1ecc0389a4aa…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : RH TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
_assessment that models this phase_

## RH5TI3 (Rh–Ti)

- Id: `phase:rh-ti:rh5ti3`; status `assigned`
- Structure: Ge3Rh5 · oP16 · Pbam (55); type `st:ge3rh5-op16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Rh 0.6250, Ti 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–2115.61 K, x(Ti) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:rh5ti3)

Names (4): _corpus: _corpus:phase:rh-ti:rh5ti3  
_mp: _mp:mp-aaaaaztt  
_oqmd: _oqmd:oqmd-18075  
_tdb: _tdb:RhTi-22Hu.tdb:RH5TI3  


### TDB models of RH5TI3 (1): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): RH5TI3, type code %, sha256 `9a0f1ecc0389a4aa…`

~~~~text
64: PHASE RH5TI3 % 2 5 3 !
65: CONST RH5TI3 : RH : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
_assessment that models this phase_

## RHTI2 (Rh–Ti)

- Id: `phase:rh-ti:rhti2`; status `assigned`
- Structure: CuZr2 · tI6 · I4/mmm (139); type `st:cuzr2-ti6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_139_matches_5_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Rh 0.3333, Ti 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1085 K, x(Ti) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:rh-ti:rhti2)

Names (2): _corpus: _corpus:phase:rh-ti:rhti2  
_tdb: _tdb:RhTi-22Hu.tdb:RHTI2  


### TDB models of RHTI2 (1): PHASE and CONSTITUENT statements as written

[RhTi-22Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/RhTi-22Hu.tdb): RHTI2, type code %, sha256 `9a0f1ecc0389a4aa…`

~~~~text
69: PHASE RHTI2 % 2 1 2 !
70: CONST RHTI2 : RH : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102386](https://doi.org/10.1016/j.calphad.2021.102386) X. Hu, L. Chen, C. Zhan, K. Xu, M. Lou, K. Chang, Calphad, 76, 102386(2022).  
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
