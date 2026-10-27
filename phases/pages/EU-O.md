# Eu–O phases

> Eu–O system: 8 phases (tier A 1, tier C 5, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-O.html · Markdown: https://data.orchid-project.org/phases/pages/EU-O.md

8 phases (tier A 1, tier C 5, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-O) · [full JSON](https://data.orchid-project.org/phases/systems/EU-O.json) · [Eu–O system page](https://data.orchid-project.org/systems/EU-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–O system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [B_R2O3](#phase-eu-o-b-r2o3); _phase:eu-o:b-r2o3_ | B-Sm2O3 · mC30 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-eu-o-bcc-a2); _phase:eu-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1095 K, x(O) 0–0 | 0 | 1 |
| [A_R2O3_D52](#phase-eu-o-d52-a-r2o3); _phase:eu-o:d52-a-r2o3_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C_R2O3_D53](#phase-eu-o-d53-c-r2o3); _phase:eu-o:d53-c-r2o3_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–895 K, x(O) 0.6–0.6 | 0 | 1 |
| [H_R2O3](#phase-eu-o-h-r2o3); _phase:eu-o:h-r2o3_ | H-La2O3 · hP10 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 2420–2500 K, x(O) 0.6–0.6 | 0 | 1 |
| [ION](#phase-eu-o-ion); _phase:eu-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1094–2500 K, x(O) 0–0.57018 | 0 | 1 |
| [O2GAS](#phase-eu-o-o2gas); _phase:eu-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 1–1 | 0 | 1 |
| [X_R2O3](#phase-eu-o-r2o3-x); _phase:eu-o:r2o3-x_ | Nd2O3 · cI26 · Im-3m (229) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |

## B_R2O3 (Eu–O)

- Id: `phase:eu-o:b-r2o3`; status `assigned`
- Structure: B-Sm2O3 · mC30 · C2/m (12); type `st:b-sm2o3-mc30`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:B,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:b-r2o3)

Names (2): _corpus: _corpus:phase:eu-o:b-r2o3  
_tdb: _tdb:EuO-07Zin.tdb:B_R2O3  


### TDB models of B_R2O3 (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): B_R2O3, type code %, sha256 `98ca41c17d4bfe5a…`

~~~~text
47: PHASE B_R2O3:I % 2 2 3 !
48: CONST B_R2O3:I : EU+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## BCC_A2 (Eu–O)

- Id: `phase:eu-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1095 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:bcc-a2)

Names (2): _corpus: _corpus:phase:eu-o:bcc-a2  
_tdb: _tdb:EuO-07Zin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): BCC_A2, type code %B, sha256 `98ca41c17d4bfe5a…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : EU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## A_R2O3_D52 (Eu–O)

- Id: `phase:eu-o:d52-a-r2o3`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:A,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:d52-a-r2o3)

Names (2): _corpus: _corpus:phase:eu-o:d52-a-r2o3  
_tdb: _tdb:EuO-07Zin.tdb:A_R2O3_D52  


### TDB models of A_R2O3_D52 (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): A_R2O3_D52, type code %, sha256 `98ca41c17d4bfe5a…`

~~~~text
42: PHASE A_R2O3_D52:I % 2 2 3 !
43: CONST A_R2O3_D52:I : EU+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## C_R2O3_D53 (Eu–O)

- Id: `phase:eu-o:d53-c-r2o3`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:C,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–895 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:d53-c-r2o3)

Names (2): _corpus: _corpus:phase:eu-o:d53-c-r2o3  
_tdb: _tdb:EuO-07Zin.tdb:C_R2O3_D53  


### TDB models of C_R2O3_D53 (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): C_R2O3_D53, type code %, sha256 `98ca41c17d4bfe5a…`

~~~~text
52: PHASE C_R2O3_D53:I % 2 2 3 !
53: CONST C_R2O3_D53:I : EU+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## H_R2O3 (Eu–O)

- Id: `phase:eu-o:h-r2o3`; status `assigned`
- Structure: H-La2O3 · hP10 · P6_3/mmc (194); type `st:h-la2o3-hp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:H,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 2420–2500 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:h-r2o3)

Names (2): _corpus: _corpus:phase:eu-o:h-r2o3  
_tdb: _tdb:EuO-07Zin.tdb:H_R2O3  


### TDB models of H_R2O3 (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): H_R2O3, type code %, sha256 `98ca41c17d4bfe5a…`

~~~~text
57: PHASE H_R2O3:I % 2 2 3 !
58: CONST H_R2O3:I : EU+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## ION (Eu–O)

- Id: `phase:eu-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1094–2500 K, x(O) 0–0.57018
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:ion)

Names (2): _corpus: _corpus:phase:eu-o:ion  
_tdb: _tdb:EuO-07Zin.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): ION, type code %, sha256 `98ca41c17d4bfe5a…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : EU+3 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## O2GAS (Eu–O)

- Id: `phase:eu-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:o2gas)

Names (2): _corpus: _corpus:phase:eu-o:o2gas  
_tdb: _tdb:EuO-07Zin.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): O2GAS, type code %, sha256 `98ca41c17d4bfe5a…`

~~~~text
65: PHASE O2GAS % 1 1 !
66: CONST O2GAS : O2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## X_R2O3 (Eu–O)

- Id: `phase:eu-o:r2o3-x`; status `assigned`
- Structure: Nd2O3 · cI26 · Im-3m (229); type `st:nd2o3-ci26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:R2O3,X, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-o:r2o3-x)

Names (2): _corpus: _corpus:phase:eu-o:r2o3-x  
_tdb: _tdb:EuO-07Zin.tdb:X_R2O3  


### TDB models of X_R2O3 (1): PHASE and CONSTITUENT statements as written

[EuO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb): X_R2O3, type code %, sha256 `98ca41c17d4bfe5a…`

~~~~text
62: PHASE X_R2O3:I % 2 2 3 !
63: CONST X_R2O3:I : EU+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
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
