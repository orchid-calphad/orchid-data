# Ag–Cu phases

> Ag–Cu system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-CU.html · Markdown: https://data.orchid-project.org/phases/pages/AG-CU.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-CU) · [full JSON](https://data.orchid-project.org/phases/systems/AG-CU.json) · [Ag–Cu system page](https://data.orchid-project.org/systems/AG-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Cu system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-cu-bcc-a2); _phase:ag-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [FCC_A1](#phase-ag-cu-fcc-a1); _phase:ag-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2499.02 K, x(Cu) 0–1 | 5 | 6 |
| [HCP_A3](#phase-ag-cu-hcp-a3); _phase:ag-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-ag-cu-liquid); _phase:ag-cu:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1052.28–2500 K, x(Cu) 0–1 | 5 | 6 |

## BCC_A2 (Ag–Cu)

- Id: `phase:ag-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cu:bcc-a2)

Names (7): _corpus: _corpus:phase:ag-cu:bcc-a2  
_tdb: _tdb:AgCu-00Moo.tdb:BCC_A2, tdb:AgCu-04Wit-LB.tdb:BCC_A2, tdb:AgCu-06He.tdb:BCC_A2, tdb:AgCu-86Hay.tdb:BCC_A2, tdb:AgCu-88Joe.tdb:BCC_A2, tdb:AgCu-98Luk.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[AgCu-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-00Moo.tdb): BCC_A2, type code %B, sha256 `1e55749c73122903…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AG CU : VA : !
~~~~

[AgCu-04Wit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-04Wit-LB.tdb): BCC_A2, type code %B, sha256 `d0b7c5fc74190270…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG CU : VA : !
~~~~

[AgCu-06He.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-06He.tdb): BCC_A2, type code %B, sha256 `454efb43f047fe25…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG CU : VA : !
~~~~

[AgCu-86Hay.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-86Hay.tdb): BCC_A2, type code %B, sha256 `2dde865753d877b6…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG CU : VA : !
~~~~

[AgCu-88Joe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-88Joe.tdb): BCC_A2, type code %B, sha256 `efd48daf5625109e…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AG CU : VA : !
~~~~

[AgCu-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-98Luk.tdb): BCC_A2, type code %B, sha256 `b1f37711e5a07cb6…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG CU : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.09.001](https://doi.org/10.1016/j.calphad.2006.09.001) X.C. He, H. Wang, H.S. Liu, Z.P. Jin, Thermodynamic description of the Cu–Ag–Zr system, Calphad 30, 367-374 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
_assessment that models this phase_

## FCC_A1 (Ag–Cu)

- Id: `phase:ag-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2499.02 K, x(Cu) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cu:fcc-a1)

Names (8): _corpus: _corpus:phase:ag-cu:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2004.04.126:(Cu)  
_tdb: _tdb:AgCu-00Moo.tdb:FCC_A1, tdb:AgCu-04Wit-LB.tdb:FCC_A1, tdb:AgCu-06He.tdb:FCC_A1, tdb:AgCu-86Hay.tdb:FCC_A1, tdb:AgCu-88Joe.tdb:FCC_A1, tdb:AgCu-98Luk.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[AgCu-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-00Moo.tdb): FCC_A1, type code %A, sha256 `1e55749c73122903…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AG% CU% : VA : !
~~~~

[AgCu-04Wit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-04Wit-LB.tdb): FCC_A1, type code %A, sha256 `d0b7c5fc74190270…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% CU% : VA : !
~~~~

[AgCu-06He.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-06He.tdb): FCC_A1, type code %A, sha256 `454efb43f047fe25…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% CU% : VA : !
~~~~

[AgCu-86Hay.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-86Hay.tdb): FCC_A1, type code %A, sha256 `2dde865753d877b6…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% CU% : VA : !
~~~~

[AgCu-88Joe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-88Joe.tdb): FCC_A1, type code %A, sha256 `efd48daf5625109e…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AG% CU% : VA : !
~~~~

[AgCu-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-98Luk.tdb): FCC_A1, type code %A, sha256 `b1f37711e5a07cb6…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% CU% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.09.001](https://doi.org/10.1016/j.calphad.2006.09.001) X.C. He, H. Wang, H.S. Liu, Z.P. Jin, Thermodynamic description of the Cu–Ag–Zr system, Calphad 30, 367-374 (2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
_assessment that models this phase_

## HCP_A3 (Ag–Cu)

- Id: `phase:ag-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cu:hcp-a3)

Names (7): _corpus: _corpus:phase:ag-cu:hcp-a3  
_tdb: _tdb:AgCu-00Moo.tdb:HCP_A3, tdb:AgCu-04Wit-LB.tdb:HCP_A3, tdb:AgCu-06He.tdb:HCP_A3, tdb:AgCu-86Hay.tdb:HCP_A3, tdb:AgCu-88Joe.tdb:HCP_A3, tdb:AgCu-98Luk.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[AgCu-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-00Moo.tdb): HCP_A3, type code %A, sha256 `1e55749c73122903…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AG CU : VA : !
~~~~

[AgCu-04Wit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-04Wit-LB.tdb): HCP_A3, type code %A, sha256 `d0b7c5fc74190270…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG CU : VA : !
~~~~

[AgCu-06He.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-06He.tdb): HCP_A3, type code %A, sha256 `454efb43f047fe25…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG CU : VA : !
~~~~

[AgCu-86Hay.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-86Hay.tdb): HCP_A3, type code %A, sha256 `2dde865753d877b6…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG CU : VA : !
~~~~

[AgCu-88Joe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-88Joe.tdb): HCP_A3, type code %A, sha256 `efd48daf5625109e…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AG CU : VA : !
~~~~

[AgCu-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-98Luk.tdb): HCP_A3, type code %A, sha256 `b1f37711e5a07cb6…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG CU : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.09.001](https://doi.org/10.1016/j.calphad.2006.09.001) X.C. He, H. Wang, H.S. Liu, Z.P. Jin, Thermodynamic description of the Cu–Ag–Zr system, Calphad 30, 367-374 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
_assessment that models this phase_

## LIQUID (Ag–Cu)

- Id: `phase:ag-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1052.28–2500 K, x(Cu) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cu:liquid)

Names (8): _corpus: _corpus:phase:ag-cu:liquid  
_paper: _paper:10.1016/j.jallcom.2004.04.126:L  
_tdb: _tdb:AgCu-00Moo.tdb:LIQUID, tdb:AgCu-04Wit-LB.tdb:LIQUID, tdb:AgCu-06He.tdb:LIQUID, tdb:AgCu-86Hay.tdb:LIQUID, tdb:AgCu-88Joe.tdb:LIQUID, tdb:AgCu-98Luk.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[AgCu-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-00Moo.tdb): LIQUID, type code %, sha256 `1e55749c73122903…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AG CU : !
~~~~

[AgCu-04Wit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-04Wit-LB.tdb): LIQUID, type code %, sha256 `d0b7c5fc74190270…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG CU : !
~~~~

[AgCu-06He.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-06He.tdb): LIQUID, type code %, sha256 `454efb43f047fe25…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG CU : !
~~~~

[AgCu-86Hay.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-86Hay.tdb): LIQUID, type code %, sha256 `2dde865753d877b6…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG CU : !
~~~~

[AgCu-88Joe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-88Joe.tdb): LIQUID, type code %, sha256 `efd48daf5625109e…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AG CU : !
~~~~

[AgCu-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCu-98Luk.tdb): LIQUID, type code %, sha256 `b1f37711e5a07cb6…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG CU : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.09.001](https://doi.org/10.1016/j.calphad.2006.09.001) X.C. He, H. Wang, H.S. Liu, Z.P. Jin, Thermodynamic description of the Cu–Ag–Zr system, Calphad 30, 367-374 (2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
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
