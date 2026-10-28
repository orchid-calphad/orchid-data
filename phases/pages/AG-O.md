# Ag–O phases

> Ag–O system: 8 phases (tier A 3, tier C 1, liquid 2, gas 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-O.html · Markdown: https://data.orchid-project.org/phases/pages/AG-O.md

8 phases (tier A 3, tier C 1, liquid 2, gas 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-O) · [full JSON](https://data.orchid-project.org/phases/systems/AG-O.json) · [Ag–O system page](https://data.orchid-project.org/systems/AG-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–O system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-o-bcc-a2); _phase:ag-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CUPRITE_C3](#phase-ag-o-c3-cuprite); _phase:ag-o:c3-cuprite_ | Cu2O · C3 · cP6 · Pn-3m (224) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0.33333–0.33333 | 8 | 1 |
| [FCC_A1](#phase-ag-o-fcc-a1); _phase:ag-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1235.08 K, x(O) 0–0.00057 | 0 | 1 |
| [GAS](#phase-ag-o-gas); _phase:ag-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2432.39 K, x(O) 0–1 | 0 | 1 |
| [HCP_A3](#phase-ag-o-hcp-a3); _phase:ag-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-ag-o-ion); _phase:ag-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1211.42–2432.39 K, x(O) 0–0.02078 | 0 | 1 |
| [LIQUID](#phase-ag-o-liquid); _phase:ag-o:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 1 | 1 |
| [O2GAS](#phase-ag-o-o2gas); _phase:ag-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 466.46–1036.46 K, x(O) 1–1 | 0 | 1 |

## BCC_A2 (Ag–O)

- Id: `phase:ag-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-o:bcc-a2  
_tdb: _tdb:AgO-97Ass-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): BCC_A2, type code %B, sha256 `9f608fb28b4b4e31…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : AG : VA% O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase_

## CUPRITE_C3 (Ag–O)

- Id: `phase:ag-o:c3-cuprite`; status `assigned`
- Structure: Cu2O · C3 · cP6 · Pn-3m (224); type `st:c3-cu2o-cp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:CUPRITE); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:c3-cuprite)

Names (4): _corpus: _corpus:phase:ag-o:c3-cuprite, corpus:phase:ag-o:cuprite-c3  
_paper: _paper:10.1111/j.1151-2916.1997.tb03232.x:Ag2O  
_tdb: _tdb:AgO-97Ass-LB.tdb:CUPRITE_C3  


### TDB models of CUPRITE_C3 (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): CUPRITE_C3, type code %, sha256 `9f608fb28b4b4e31…`

~~~~text
59: PHASE CUPRITE_C3:I % 2 2 1 !
60: CONST CUPRITE_C3:I : AG+1 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ag–O)

- Id: `phase:ag-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1235.08 K, x(O) 0–0.00057
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:fcc-a1)

Names (2): _corpus: _corpus:phase:ag-o:fcc-a1  
_tdb: _tdb:AgO-97Ass-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): FCC_A1, type code %A, sha256 `9f608fb28b4b4e31…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : AG : VA% O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase_

## GAS (Ag–O)

- Id: `phase:ag-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2432.39 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:gas)

Names (2): _corpus: _corpus:phase:ag-o:gas  
_tdb: _tdb:AgO-97Ass-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): GAS, type code %, sha256 `9f608fb28b4b4e31…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : AG AG2 AGO O O2 O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase_

## HCP_A3 (Ag–O)

- Id: `phase:ag-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-o:hcp-a3  
_tdb: _tdb:AgO-97Ass-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): HCP_A3, type code %A, sha256 `9f608fb28b4b4e31…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : AG : VA% O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase_

## ION (Ag–O)

- Id: `phase:ag-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1211.42–2432.39 K, x(O) 0–0.02078
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:ion)

Names (2): _corpus: _corpus:phase:ag-o:ion  
_tdb: _tdb:AgO-97Ass-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): ION, type code %, sha256 `9f608fb28b4b4e31…`

~~~~text
39: PHASE ION:Y % 2 1 1 !
40: CONST ION:Y : AG+1 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase_

## LIQUID (Ag–O)

- Id: `phase:ag-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:liquid)

Names (3): _corpus: _corpus:phase:ag-o:liquid  
_paper: _paper:10.1111/j.1151-2916.1997.tb03232.x:L  
_tdb: _tdb:AgO-97Ass-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): LIQUID, type code %, sha256 `9f608fb28b4b4e31…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : AG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase; reports values for this phase_

## O2GAS (Ag–O)

- Id: `phase:ag-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 466.46–1036.46 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-o:o2gas)

Names (2): _corpus: _corpus:phase:ag-o:o2gas  
_tdb: _tdb:AgO-97Ass-LB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[AgO-97Ass-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb): O2GAS, type code %, sha256 `9f608fb28b4b4e31…`

~~~~text
62: PHASE O2GAS % 1 1 !
63: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
