# Ag–Dy phases

> Ag–Dy system: 7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-DY.html · Markdown: https://data.orchid-project.org/phases/pages/AG-DY.md

7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-DY) · [full JSON](https://data.orchid-project.org/phases/systems/AG-DY.json) · [Ag–Dy system page](https://data.orchid-project.org/systems/AG-DY.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-DY.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Dy system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2DY_C11B](#phase-ag-dy-ag2dy-c11b); _phase:ag-dy:ag2dy-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1250.27 K, x(Dy) 0.33333–0.33333 | 6 | 1 |
| [AG51DY14](#phase-ag-dy-ag51dy14); _phase:ag-dy:ag51dy14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1256.94 K, x(Dy) 0.21538–0.21538 | 7 | 1 |
| [AGDY_B2](#phase-ag-dy-agdy-b2); _phase:ag-dy:agdy-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1468.63 K, x(Dy) 0.5–0.5 | 6 | 1 |
| [BCC_A2](#phase-ag-dy-bcc-a2); _phase:ag-dy:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1652.86–2500 K, x(Dy) 0.99974–1 | 0 | 1 |
| [FCC_A1](#phase-ag-dy-fcc-a1); _phase:ag-dy:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1236.94 K, x(Dy) 0–0.0129 | 3 | 1 |
| [HCP_A3](#phase-ag-dy-hcp-a3); _phase:ag-dy:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1677.86 K, x(Dy) 1–1 | 2 | 1 |
| [LIQUID](#phase-ag-dy-liquid); _phase:ag-dy:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1076.94–2500 K, x(Dy) 0–1 | 15 | 1 |

## AG2DY_C11B (Ag–Dy)

- Id: `phase:ag-dy:ag2dy-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.6667, Dy 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1250.27 K, x(Dy) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-dy:ag2dy-c11b)

Names (3): _corpus: _corpus:phase:ag-dy:ag2dy-c11b  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Ag2Dy  
_tdb: _tdb:AgDy-10Lon.tdb:AG2DY_C11B  


### TDB models of AG2DY_C11B (1): PHASE and CONSTITUENT statements as written

[AgDy-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb): AG2DY_C11B, type code %, sha256 `368d9cf97a10d0ba…`

~~~~text
53: PHASE AG2DY_C11B % 2 2 1 !
54: CONST AG2DY_C11B : AG : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_

## AG51DY14 (Ag–Dy)

- Id: `phase:ag-dy:ag51dy14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.7846, Dy 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–1256.94 K, x(Dy) 0.21538–0.21538
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-dy:ag51dy14)

Names (3): _corpus: _corpus:phase:ag-dy:ag51dy14  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Ag51Dy14  
_tdb: _tdb:AgDy-10Lon.tdb:AG51DY14  


### TDB models of AG51DY14 (1): PHASE and CONSTITUENT statements as written

[AgDy-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb): AG51DY14, type code %, sha256 `368d9cf97a10d0ba…`

~~~~text
48: PHASE AG51DY14 % 2 51 14 !
49: CONST AG51DY14 : AG : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_

## AGDY_B2 (Ag–Dy)

- Id: `phase:ag-dy:agdy-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadfj and oqmd-10365, space group 221
- Stoichiometry: Ag 0.5000, Dy 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1468.63 K, x(Dy) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-dy:agdy-b2)

Names (5): _corpus: _corpus:phase:ag-dy:agdy-b2  
_mp: _mp:mp-aaaaadfj  
_oqmd: _oqmd:oqmd-10365  
_paper: _paper:10.1016/j.jallcom.2009.09.036:AgDy  
_tdb: _tdb:AgDy-10Lon.tdb:AGDY_B2  


### TDB models of AGDY_B2 (1): PHASE and CONSTITUENT statements as written

[AgDy-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb): AGDY_B2, type code %A, sha256 `368d9cf97a10d0ba…`

~~~~text
58: PHASE AGDY_B2 %A 2 1 1 !
59: CONST AGDY_B2 : AG : DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Ag–Dy)

- Id: `phase:ag-dy:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1652.86–2500 K, x(Dy) 0.99974–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-dy:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-dy:bcc-a2  
_tdb: _tdb:AgDy-10Lon.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgDy-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb): BCC_A2, type code %B, sha256 `368d9cf97a10d0ba…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AG DY% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase_

## FCC_A1 (Ag–Dy)

- Id: `phase:ag-dy:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1236.94 K, x(Dy) 0–0.0129
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-dy:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-dy:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Fcc(Ag)  
_tdb: _tdb:AgDy-10Lon.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgDy-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb): FCC_A1, type code %A, sha256 `368d9cf97a10d0ba…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AG% DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ag–Dy)

- Id: `phase:ag-dy:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1677.86 K, x(Dy) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-dy:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-dy:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.09.036:Hcp(Dy)  
_tdb: _tdb:AgDy-10Lon.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgDy-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb): HCP_A3, type code %A, sha256 `368d9cf97a10d0ba…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AG DY% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ag–Dy)

- Id: `phase:ag-dy:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1076.94–2500 K, x(Dy) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-dy:liquid)

Names (3): _corpus: _corpus:phase:ag-dy:liquid  
_paper: _paper:10.1016/j.jallcom.2009.09.036:L  
_tdb: _tdb:AgDy-10Lon.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgDy-10Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb): LIQUID, type code %, sha256 `368d9cf97a10d0ba…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AG DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010).  
_assessment that models this phase; reports values for this phase_

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
