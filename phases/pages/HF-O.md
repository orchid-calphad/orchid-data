# Hf–O phases

> Hf–O system: 9 phases (tier A 4, tier C 2, liquid 1, gas 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-O.html · Markdown: https://data.orchid-project.org/phases/pages/HF-O.md

9 phases (tier A 4, tier C 2, liquid 1, gas 2); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-O) · [full JSON](https://data.orchid-project.org/phases/systems/HF-O.json) · [Hf–O system page](https://data.orchid-project.org/systems/HF-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–O system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-o-bcc-a2); _phase:hf-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2015.2–2582.59 K, x(O) 0–0.04924 | 0 | 2 |
| [FCC_A1](#phase-hf-o-fcc-a1); _phase:hf-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-hf-o-gas); _phase:hf-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(O) 0.99886–1 | 0 | 2 |
| [HCP_A3](#phase-hf-o-hcp-a3); _phase:hf-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2771.46 K, x(O) 0–0.2134 | 0 | 2 |
| [HFO2_C1](#phase-hf-o-hfo2-c1); _phase:hf-o:hfo2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2793–3222.7 K, x(O) 0.64795–0.66667 | 0 | 2 |
| [HFO2_MONO](#phase-hf-o-hfo2-mono); _phase:hf-o:hfo2-mono_ | ZrO2-m · C43 · mP12 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2100 K, x(O) 0.66667–0.66667 | 0 | 2 |
| [HFO2_TETR](#phase-hf-o-hfo2-tetr); _phase:hf-o:hfo2-tetr_ | HgI2 · tP6 · P4_2/nmc (137) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 2 calculated diagram(s): 2100–2793 K, x(O) 0.66667–0.66667 | 0 | 2 |
| [ION](#phase-hf-o-ion); _phase:hf-o:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2506–4000 K, x(O) 0–0.66667 | 0 | 2 |
| [O2GAS](#phase-hf-o-o2gas); _phase:hf-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1 | 0 | 2 |

## BCC_A2 (Hf–O)

- Id: `phase:hf-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2015.2–2582.59 K, x(O) 0–0.04924
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:bcc-a2)

Names (3): _corpus: _corpus:phase:hf-o:bcc-a2  
_tdb: _tdb:HfO-06Shi.tdb:BCC_A2, tdb:HfO-06Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): BCC_A2, type code %B, sha256 `c524a8de35394af9…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : HF : O VA% : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): BCC_A2, type code %B, sha256 `54d88108dcb3dde7…`

~~~~text
47: PHASE BCC_A2 %B 2 1 1 !
48: CONST BCC_A2 : HF : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## FCC_A1 (Hf–O)

- Id: `phase:hf-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:fcc-a1)

Names (3): _corpus: _corpus:phase:hf-o:fcc-a1  
_tdb: _tdb:HfO-06Shi.tdb:FCC_A1, tdb:HfO-06Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): FCC_A1, type code %A, sha256 `c524a8de35394af9…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : HF : O VA% : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): FCC_A1, type code %A, sha256 `54d88108dcb3dde7…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : HF : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## GAS (Hf–O)

- Id: `phase:hf-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(O) 0.99886–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:gas)

Names (3): _corpus: _corpus:phase:hf-o:gas  
_tdb: _tdb:HfO-06Shi.tdb:GAS, tdb:HfO-06Wan.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): GAS, type code %, sha256 `c524a8de35394af9…`

~~~~text
69: PHASE GAS:G % 1 1 !
70: CONST GAS:G : HF O O2 O3 HFO HFO2 : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): GAS, type code %, sha256 `54d88108dcb3dde7…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : HF O O2 O3 HFO HFO2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## HCP_A3 (Hf–O)

- Id: `phase:hf-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2771.46 K, x(O) 0–0.2134
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:hcp-a3)

Names (3): _corpus: _corpus:phase:hf-o:hcp-a3  
_tdb: _tdb:HfO-06Shi.tdb:HCP_A3, tdb:HfO-06Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): HCP_A3, type code %, sha256 `c524a8de35394af9…`

~~~~text
48: PHASE HCP_A3 % 2 1 0.5 !
49: CONST HCP_A3 : HF : O VA% : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): HCP_A3, type code %, sha256 `54d88108dcb3dde7…`

~~~~text
52: PHASE HCP_A3 % 2 1 0.5 !
53: CONST HCP_A3 : HF : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## HFO2_C1 (Hf–O)

- Id: `phase:hf-o:hfo2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2793–3222.7 K, x(O) 0.64795–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:hfo2-c1)

Names (3): _corpus: _corpus:phase:hf-o:hfo2-c1  
_tdb: _tdb:HfO-06Shi.tdb:HFO2_C1, tdb:HfO-06Wan.tdb:HFO2_C1  


### TDB models of HFO2_C1 (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): HFO2_C1, type code %, sha256 `c524a8de35394af9…`

~~~~text
63: PHASE HFO2_C1 % 1 1 !
64: CONST HFO2_C1 : HFO2 : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): HFO2_C1, type code %, sha256 `54d88108dcb3dde7…`

~~~~text
67: PHASE HFO2_C1:I % 2 1 2 !
68: CONST HFO2_C1:I : HF+2 HF+4% : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## HFO2_MONO (Hf–O)

- Id: `phase:hf-o:hfo2-mono`; status `assigned`
- Structure: ZrO2-m · C43 · mP12 · P2_1/c (14); type `st:c43-zro2-m-mp12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MONO, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–2100 K, x(O) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:hfo2-mono)

Names (3): _corpus: _corpus:phase:hf-o:hfo2-mono  
_tdb: _tdb:HfO-06Shi.tdb:HFO2_MONO, tdb:HfO-06Wan.tdb:HFO2_MONO  


### TDB models of HFO2_MONO (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): HFO2_MONO, type code %, sha256 `c524a8de35394af9…`

~~~~text
53: PHASE HFO2_MONO % 1 1 !
54: CONST HFO2_MONO : HFO2 : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): HFO2_MONO, type code %, sha256 `54d88108dcb3dde7…`

~~~~text
57: PHASE HFO2_MONO:I % 2 1 2 !
58: CONST HFO2_MONO:I : HF+4 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## HFO2_TETR (Hf–O)

- Id: `phase:hf-o:hfo2-tetr`; status `assigned`
- Structure: HgI2 · tP6 · P4_2/nmc (137); type `st:hgi2-tp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:TETR, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 2 calculated diagram(s): 2100–2793 K, x(O) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:hfo2-tetr)

Names (3): _corpus: _corpus:phase:hf-o:hfo2-tetr  
_tdb: _tdb:HfO-06Shi.tdb:HFO2_TETR, tdb:HfO-06Wan.tdb:HFO2_TETR  


### TDB models of HFO2_TETR (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): HFO2_TETR, type code %, sha256 `c524a8de35394af9…`

~~~~text
58: PHASE HFO2_TETR % 1 1 !
59: CONST HFO2_TETR : HFO2 : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): HFO2_TETR, type code %, sha256 `54d88108dcb3dde7…`

~~~~text
62: PHASE HFO2_TETR:I % 2 1 2 !
63: CONST HFO2_TETR:I : HF+4 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## ION (Hf–O)

- Id: `phase:hf-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2506–4000 K, x(O) 0–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:ion)

Names (3): _corpus: _corpus:phase:hf-o:ion  
_tdb: _tdb:HfO-06Shi.tdb:ION, tdb:HfO-06Wan.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): ION, type code %, sha256 `c524a8de35394af9…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : HF+4 : O-2 VA : !
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): ION, type code %, sha256 `54d88108dcb3dde7…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : HF+4 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
_assessment that models this phase_

## O2GAS (Hf–O)

- Id: `phase:hf-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-o:o2gas)

Names (3): _corpus: _corpus:phase:hf-o:o2gas  
_tdb: _tdb:HfO-06Shi.tdb:O2GAS, tdb:HfO-06Wan.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[HfO-06Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb): O2GAS, type code %, sha256 `c524a8de35394af9…`

~~~~text
66: PHASE O2GAS % 1 1 !
67: CONST O2GAS : O2 :!
~~~~

[HfO-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb): O2GAS, type code %, sha256 `54d88108dcb3dde7…`

~~~~text
70: PHASE O2GAS % 1 1 !
71: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006).  
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
