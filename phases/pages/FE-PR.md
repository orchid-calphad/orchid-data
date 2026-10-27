# Fe–Pr phases

> Fe–Pr system: 6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-PR.html · Markdown: https://data.orchid-project.org/phases/pages/FE-PR.md

6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-PR) · [full JSON](https://data.orchid-project.org/phases/systems/FE-PR.json) · [Fe–Pr system page](https://data.orchid-project.org/systems/FE-PR.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-PR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Pr system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-pr-bcc-a2); _phase:fe-pr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.24 K, x(Pr) 0–1 | 0 | 2 |
| [DHCP](#phase-fe-pr-dhcp-a3); _phase:fe-pr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1203 K, x(Pr) 1–1 | 0 | 2 |
| [FCC_A1](#phase-fe-pr-fcc-a1); _phase:fe-pr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1066.26–1808.41 K, x(Pr) 0–0.00032 | 0 | 2 |
| [FE17PR2](#phase-fe-pr-fe17pr2); _phase:fe-pr:fe17pr2_ | Th2Zn17 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1382.98 K, x(Pr) 0.10526–0.10526 | 0 | 2 |
| [HCP_A3](#phase-fe-pr-hcp-a3); _phase:fe-pr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-fe-pr-liquid); _phase:fe-pr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 938.01–2500 K, x(Pr) 0–1 | 0 | 2 |

## BCC_A2 (Fe–Pr)

- Id: `phase:fe-pr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.24 K, x(Pr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pr:bcc-a2)

Names (3): _corpus: _corpus:phase:fe-pr:bcc-a2  
_tdb: _tdb:FePr-16Che.tdb:BCC_A2, tdb:FePr-95Bae-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FePr-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-16Che.tdb): BCC_A2, type code %B, sha256 `12e07b0584954755…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% PR% : VA : !
~~~~

[FePr-95Bae-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-95Bae-LB.tdb): BCC_A2, type code %B, sha256 `7d621fd2fe786c71…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% PR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_

## DHCP (Fe–Pr)

- Id: `phase:fe-pr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pr 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1203 K, x(Pr) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pr:dhcp-a3)

Names (3): _corpus: _corpus:phase:fe-pr:dhcp-a3  
_tdb: _tdb:FePr-16Che.tdb:DHCP, tdb:FePr-95Bae-LB.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[FePr-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-16Che.tdb): DHCP, type code %, sha256 `12e07b0584954755…`

~~~~text
42: PHASE DHCP % 1 1 !
43: CONST DHCP : PR : !
~~~~

[FePr-95Bae-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-95Bae-LB.tdb): DHCP, type code %, sha256 `7d621fd2fe786c71…`

~~~~text
46: PHASE DHCP % 1 1 !
47: CONST DHCP : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_

## FCC_A1 (Fe–Pr)

- Id: `phase:fe-pr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1066.26–1808.41 K, x(Pr) 0–0.00032
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pr:fcc-a1)

Names (3): _corpus: _corpus:phase:fe-pr:fcc-a1  
_tdb: _tdb:FePr-16Che.tdb:FCC_A1, tdb:FePr-95Bae-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FePr-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-16Che.tdb): FCC_A1, type code %A, sha256 `12e07b0584954755…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% PR : VA : !
~~~~

[FePr-95Bae-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-95Bae-LB.tdb): FCC_A1, type code %A, sha256 `7d621fd2fe786c71…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_

## FE17PR2 (Fe–Pr)

- Id: `phase:fe-pr:fe17pr2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.8947, Pr 0.1053
- Stability: stable in 2 of 2 calculated diagram(s): 300–1382.98 K, x(Pr) 0.10526–0.10526
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pr:fe17pr2)

Names (3): _corpus: _corpus:phase:fe-pr:fe17pr2  
_tdb: _tdb:FePr-16Che.tdb:FE17PR2, tdb:FePr-95Bae-LB.tdb:FE17PR2  


### TDB models of FE17PR2 (2): PHASE and CONSTITUENT statements as written

[FePr-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-16Che.tdb): FE17PR2, type code %A, sha256 `12e07b0584954755…`

~~~~text
47: PHASE FE17PR2 %A 2 17 2 !
48: CONST FE17PR2 : FE : PR : !
~~~~

[FePr-95Bae-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-95Bae-LB.tdb): FE17PR2, type code %B, sha256 `7d621fd2fe786c71…`

~~~~text
51: PHASE FE17PR2 %B 2 17 2 !
52: CONST FE17PR2 : FE : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_

## HCP_A3 (Fe–Pr)

- Id: `phase:fe-pr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pr:hcp-a3)

Names (3): _corpus: _corpus:phase:fe-pr:hcp-a3  
_tdb: _tdb:FePr-16Che.tdb:HCP_A3, tdb:FePr-95Bae-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FePr-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-16Che.tdb): HCP_A3, type code %A, sha256 `12e07b0584954755…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE : VA : !
~~~~

[FePr-95Bae-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-95Bae-LB.tdb): HCP_A3, type code %A, sha256 `7d621fd2fe786c71…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
_assessment that models this phase_

## LIQUID (Fe–Pr)

- Id: `phase:fe-pr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 938.01–2500 K, x(Pr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pr:liquid)

Names (3): _corpus: _corpus:phase:fe-pr:liquid  
_tdb: _tdb:FePr-16Che.tdb:LIQUID, tdb:FePr-95Bae-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FePr-16Che.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-16Che.tdb): LIQUID, type code %, sha256 `12e07b0584954755…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE PR : !
~~~~

[FePr-95Bae-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePr-95Bae-LB.tdb): LIQUID, type code %, sha256 `7d621fd2fe786c71…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.10.004](https://doi.org/10.1016/j.calphad.2016.10.004) T.L. Chen, J. Wang, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 55, 270-80(2016).  
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
