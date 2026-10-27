# O–Yb phases

> O–Yb system: 7 phases (tier A 3, tier C 2, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-YB.html · Markdown: https://data.orchid-project.org/phases/pages/O-YB.md

7 phases (tier A 3, tier C 2, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-YB) · [full JSON](https://data.orchid-project.org/phases/systems/O-YB.json) · [O–Yb system page](https://data.orchid-project.org/systems/O-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Yb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-yb-bcc-a2); _phase:o-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C_R2O3_D53](#phase-o-yb-d53-c-r2o3); _phase:o-yb:d53-c-r2o3_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0.6–0.6 | 0 | 1 |
| [FCC_A1](#phase-o-yb-fcc-a1); _phase:o-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1015 K, x(O) 0–0 | 0 | 1 |
| [H_R2O3](#phase-o-yb-h-r2o3); _phase:o-yb:h-r2o3_ | H-La2O3 · hP10 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-o-yb-hcp-a3); _phase:o-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-o-yb-ion); _phase:o-yb:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1856.25–2500 K, x(O) 0.25434–0.55679 | 0 | 1 |
| [O2GAS](#phase-o-yb-o2gas); _phase:o-yb:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 1–1 | 0 | 1 |

## BCC_A2 (O–Yb)

- Id: `phase:o-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Yb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-yb:bcc-a2)

Names (2): _corpus: _corpus:phase:o-yb:bcc-a2  
_tdb: _tdb:YbO-07Zin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[YbO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/YbO-07Zin.tdb): BCC_A2, type code %B, sha256 `fcda387e2b204586…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : YB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## C_R2O3_D53 (O–Yb)

- Id: `phase:o-yb:d53-c-r2o3`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:C,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-yb:d53-c-r2o3)

Names (2): _corpus: _corpus:phase:o-yb:d53-c-r2o3  
_tdb: _tdb:YbO-07Zin.tdb:C_R2O3_D53  


### TDB models of C_R2O3_D53 (1): PHASE and CONSTITUENT statements as written

[YbO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/YbO-07Zin.tdb): C_R2O3_D53, type code %, sha256 `fcda387e2b204586…`

~~~~text
52: PHASE C_R2O3_D53:I % 2 2 3 !
53: CONST C_R2O3_D53:I : YB+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## FCC_A1 (O–Yb)

- Id: `phase:o-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Yb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1015 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-yb:fcc-a1)

Names (2): _corpus: _corpus:phase:o-yb:fcc-a1  
_tdb: _tdb:YbO-07Zin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[YbO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/YbO-07Zin.tdb): FCC_A1, type code %A, sha256 `fcda387e2b204586…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : YB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## H_R2O3 (O–Yb)

- Id: `phase:o-yb:h-r2o3`; status `assigned`
- Structure: H-La2O3 · hP10 · P6_3/mmc (194); type `st:h-la2o3-hp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:H,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-yb:h-r2o3)

Names (2): _corpus: _corpus:phase:o-yb:h-r2o3  
_tdb: _tdb:YbO-07Zin.tdb:H_R2O3  


### TDB models of H_R2O3 (1): PHASE and CONSTITUENT statements as written

[YbO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/YbO-07Zin.tdb): H_R2O3, type code %, sha256 `fcda387e2b204586…`

~~~~text
57: PHASE H_R2O3:I % 2 2 3 !
58: CONST H_R2O3:I : YB+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## HCP_A3 (O–Yb)

- Id: `phase:o-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Yb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-yb:hcp-a3)

Names (2): _corpus: _corpus:phase:o-yb:hcp-a3  
_tdb: _tdb:YbO-07Zin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[YbO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/YbO-07Zin.tdb): HCP_A3, type code %A, sha256 `fcda387e2b204586…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : YB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## ION (O–Yb)

- Id: `phase:o-yb:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1856.25–2500 K, x(O) 0.25434–0.55679
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-yb:ion)

Names (2): _corpus: _corpus:phase:o-yb:ion  
_tdb: _tdb:YbO-07Zin.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[YbO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/YbO-07Zin.tdb): ION, type code %, sha256 `fcda387e2b204586…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : YB+3 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## O2GAS (O–Yb)

- Id: `phase:o-yb:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-yb:o2gas)

Names (2): _corpus: _corpus:phase:o-yb:o2gas  
_tdb: _tdb:YbO-07Zin.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[YbO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/YbO-07Zin.tdb): O2GAS, type code %, sha256 `fcda387e2b204586…`

~~~~text
60: PHASE O2GAS % 1 1 !
61: CONST O2GAS : O2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
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
