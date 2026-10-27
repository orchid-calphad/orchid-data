# Ag–Tb phases

> Ag–Tb system: 7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-TB.html · Markdown: https://data.orchid-project.org/phases/pages/AG-TB.md

7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-TB) · [full JSON](https://data.orchid-project.org/phases/systems/AG-TB.json) · [Ag–Tb system page](https://data.orchid-project.org/systems/AG-TB.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-TB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Tb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2TB_C11B](#phase-ag-tb-ag2tb-c11b); _phase:ag-tb:ag2tb-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1186.41 K, x(Tb) 0.33333–0.33333 | 9 | 1 |
| [AG51TB14](#phase-ag-tb-ag51tb14); _phase:ag-tb:ag51tb14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1253.25 K, x(Tb) 0.21538–0.22709 | 11 | 1 |
| [AGTB_B2](#phase-ag-tb-agtb-b2); _phase:ag-tb:agtb-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1418.09 K, x(Tb) 0.5–0.5 | 9 | 1 |
| [BCC_A2](#phase-ag-tb-bcc-a2); _phase:ag-tb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1562.02–2499.52 K, x(Tb) 0.99996–1 | 0 | 1 |
| [FCC_A1](#phase-ag-tb-fcc-a1); _phase:ag-tb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1277.48 K, x(Tb) 0–0.01625 | 4 | 1 |
| [HCP_A3](#phase-ag-tb-hcp-a3); _phase:ag-tb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1562.02 K, x(Tb) 0.9999–1 | 3 | 1 |
| [LIQUID](#phase-ag-tb-liquid); _phase:ag-tb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1072.48–2500 K, x(Tb) 0–1 | 22 | 1 |

## AG2TB_C11B (Ag–Tb)

- Id: `phase:ag-tb:ag2tb-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.6667, Tb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1186.41 K, x(Tb) 0.33333–0.33333
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-tb:ag2tb-c11b)

Names (3): _corpus: _corpus:phase:ag-tb:ag2tb-c11b  
_paper: _paper:10.1016/j.jallcom.2009.04.037:Ag2Tb  
_tdb: _tdb:AgTb-09Wan.tdb:AG2TB_C11B  


### TDB models of AG2TB_C11B (1): PHASE and CONSTITUENT statements as written

[AgTb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb): AG2TB_C11B, type code %, sha256 `306744ad1d04e395…`

~~~~text
51: PHASE AG2TB_C11B % 2 2 1 !
52: CONST AG2TB_C11B : AG : TB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_

## AG51TB14 (Ag–Tb)

- Id: `phase:ag-tb:ag51tb14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1253.25 K, x(Tb) 0.21538–0.22709
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-tb:ag51tb14)

Names (3): _corpus: _corpus:phase:ag-tb:ag51tb14  
_paper: _paper:10.1016/j.jallcom.2009.04.037:Ag51Tb14  
_tdb: _tdb:AgTb-09Wan.tdb:AG51TB14  


### TDB models of AG51TB14 (1): PHASE and CONSTITUENT statements as written

[AgTb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb): AG51TB14, type code %, sha256 `306744ad1d04e395…`

~~~~text
46: PHASE AG51TB14 % 2 51 14 !
47: CONST AG51TB14 : AG% TB : TB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_

## AGTB_B2 (Ag–Tb)

- Id: `phase:ag-tb:agtb-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.5000, Tb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1418.09 K, x(Tb) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-tb:agtb-b2)

Names (3): _corpus: _corpus:phase:ag-tb:agtb-b2  
_paper: _paper:10.1016/j.jallcom.2009.04.037:AgTb  
_tdb: _tdb:AgTb-09Wan.tdb:AGTB_B2  


### TDB models of AGTB_B2 (1): PHASE and CONSTITUENT statements as written

[AgTb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb): AGTB_B2, type code %A, sha256 `306744ad1d04e395…`

~~~~text
56: PHASE AGTB_B2 %A 2 1 1 !
57: CONST AGTB_B2 : AG : TB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Tb)

- Id: `phase:ag-tb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1562.02–2499.52 K, x(Tb) 0.99996–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-tb:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-tb:bcc-a2  
_tdb: _tdb:AgTb-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgTb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb): BCC_A2, type code %B, sha256 `306744ad1d04e395…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AG TB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase_

## FCC_A1 (Ag–Tb)

- Id: `phase:ag-tb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1277.48 K, x(Tb) 0–0.01625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-tb:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-tb:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.04.037:(Ag)  
_tdb: _tdb:AgTb-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgTb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb): FCC_A1, type code %A, sha256 `306744ad1d04e395…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AG% TB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Tb)

- Id: `phase:ag-tb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1562.02 K, x(Tb) 0.9999–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-tb:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-tb:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.04.037:αTb  
_tdb: _tdb:AgTb-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgTb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb): HCP_A3, type code %A, sha256 `306744ad1d04e395…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AG TB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_

## LIQUID (Ag–Tb)

- Id: `phase:ag-tb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1072.48–2500 K, x(Tb) 0–1
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-tb:liquid)

Names (3): _corpus: _corpus:phase:ag-tb:liquid  
_paper: _paper:10.1016/j.jallcom.2009.04.037:L  
_tdb: _tdb:AgTb-09Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgTb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb): LIQUID, type code %, sha256 `306744ad1d04e395…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AG TB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
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
