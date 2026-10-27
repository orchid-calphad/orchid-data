# Dy–O phases

> Dy–O system: 8 phases (tier A 2, tier C 4, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/DY-O.html · Markdown: https://data.orchid-project.org/phases/pages/DY-O.md

8 phases (tier A 2, tier C 4, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=DY-O) · [full JSON](https://data.orchid-project.org/phases/systems/DY-O.json) · [Dy–O system page](https://data.orchid-project.org/systems/DY-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/DY-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Dy–O system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [B_R2O3](#phase-dy-o-b-r2o3); _phase:dy-o:b-r2o3_ | B-Sm2O3 · mC30 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-dy-o-bcc-a2); _phase:dy-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C_R2O3_D53](#phase-dy-o-d53-c-r2o3); _phase:dy-o:d53-c-r2o3_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–995 K, x(O) 0.6–0.6 | 0 | 1 |
| [H_R2O3](#phase-dy-o-h-r2o3); _phase:dy-o:h-r2o3_ | H-La2O3 · hP10 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 2465–2500 K, x(O) 0.6–0.6 | 0 | 1 |
| [HCP_A3](#phase-dy-o-hcp-a3); _phase:dy-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–545 K, x(O) 0–0 | 0 | 1 |
| [ION](#phase-dy-o-ion); _phase:dy-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2471–2500 K, x(O) 0.56084–0.56659 | 0 | 1 |
| [O2GAS](#phase-dy-o-o2gas); _phase:dy-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 1–1 | 0 | 1 |
| [X_R2O3](#phase-dy-o-r2o3-x); _phase:dy-o:r2o3-x_ | Nd2O3 · cI26 · Im-3m (229) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |

## B_R2O3 (Dy–O)

- Id: `phase:dy-o:b-r2o3`; status `assigned`
- Structure: B-Sm2O3 · mC30 · C2/m (12); type `st:b-sm2o3-mc30`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:B,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:b-r2o3)

Names (2): _corpus: _corpus:phase:dy-o:b-r2o3  
_tdb: _tdb:DyO-23Nak.tdb:B_R2O3  


### TDB models of B_R2O3 (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): B_R2O3, type code %, sha256 `c88748be13043bab…`

~~~~text
48: PHASE B_R2O3:I % 2 2 3 !
49: CONST B_R2O3:I : DY+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_

## BCC_A2 (Dy–O)

- Id: `phase:dy-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:bcc-a2)

Names (2): _corpus: _corpus:phase:dy-o:bcc-a2  
_tdb: _tdb:DyO-23Nak.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): BCC_A2, type code %B, sha256 `c88748be13043bab…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_

## C_R2O3_D53 (Dy–O)

- Id: `phase:dy-o:d53-c-r2o3`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:C,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–995 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:d53-c-r2o3)

Names (2): _corpus: _corpus:phase:dy-o:d53-c-r2o3  
_tdb: _tdb:DyO-23Nak.tdb:C_R2O3_D53  


### TDB models of C_R2O3_D53 (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): C_R2O3_D53, type code %, sha256 `c88748be13043bab…`

~~~~text
53: PHASE C_R2O3_D53:I % 2 2 3 !
54: CONST C_R2O3_D53:I : DY+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_

## H_R2O3 (Dy–O)

- Id: `phase:dy-o:h-r2o3`; status `assigned`
- Structure: H-La2O3 · hP10 · P6_3/mmc (194); type `st:h-la2o3-hp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:H,R2O3, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 2465–2500 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:h-r2o3)

Names (2): _corpus: _corpus:phase:dy-o:h-r2o3  
_tdb: _tdb:DyO-23Nak.tdb:H_R2O3  


### TDB models of H_R2O3 (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): H_R2O3, type code %, sha256 `c88748be13043bab…`

~~~~text
58: PHASE H_R2O3:I % 2 2 3 !
59: CONST H_R2O3:I : DY+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_

## HCP_A3 (Dy–O)

- Id: `phase:dy-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–545 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:hcp-a3)

Names (2): _corpus: _corpus:phase:dy-o:hcp-a3  
_tdb: _tdb:DyO-23Nak.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): HCP_A3, type code %A, sha256 `c88748be13043bab…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_

## ION (Dy–O)

- Id: `phase:dy-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2471–2500 K, x(O) 0.56084–0.56659
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:ion)

Names (2): _corpus: _corpus:phase:dy-o:ion  
_tdb: _tdb:DyO-23Nak.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): ION, type code %, sha256 `c88748be13043bab…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : DY+3 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_

## O2GAS (Dy–O)

- Id: `phase:dy-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:o2gas)

Names (2): _corpus: _corpus:phase:dy-o:o2gas  
_tdb: _tdb:DyO-23Nak.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): O2GAS, type code %, sha256 `c88748be13043bab…`

~~~~text
66: PHASE O2GAS % 1 1 !
67: CONST O2GAS : O2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
_assessment that models this phase_

## X_R2O3 (Dy–O)

- Id: `phase:dy-o:r2o3-x`; status `assigned`
- Structure: Nd2O3 · cI26 · Im-3m (229); type `st:nd2o3-ci26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:R2O3,X, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-o:r2o3-x)

Names (2): _corpus: _corpus:phase:dy-o:r2o3-x  
_tdb: _tdb:DyO-23Nak.tdb:X_R2O3  


### TDB models of X_R2O3 (1): PHASE and CONSTITUENT statements as written

[DyO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb): X_R2O3, type code %, sha256 `c88748be13043bab…`

~~~~text
63: PHASE X_R2O3:I % 2 2 3 !
64: CONST X_R2O3:I : DY+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023).  
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
