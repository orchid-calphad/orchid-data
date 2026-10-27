# Ge–Ru phases

> Ge–Ru system: 8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-RU.html · Markdown: https://data.orchid-project.org/phases/pages/GE-RU.md

8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-RU) · [full JSON](https://data.orchid-project.org/phases/systems/GE-RU.json) · [Ge–Ru system page](https://data.orchid-project.org/systems/GE-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Ru system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-ru-a4-diamond); _phase:ge-ru:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Ru) 0–0 | 2 | 1 |
| [BCC_A2](#phase-ge-ru-bcc-a2); _phase:ge-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ge-ru-fcc-a1); _phase:ge-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GE3RU2_ALPHA](#phase-ge-ru-ge3ru2-alpha); _phase:ge-ru:ge3ru2-alpha_ | Ge3Ru2 · oP40 · Pbcn (60) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–859.97 K, x(Ru) 0.4–0.4 | 2 | 1 |
| [GE3RU2_BETA](#phase-ge-ru-ge3ru2-beta); _phase:ge-ru:ge3ru2-beta_ | Ru2Sn3 · tP20 · P-4c2 (116) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 859.97–1822.35 K, x(Ru) 0.4–0.4 | 0 | 1 |
| [GERU](#phase-ge-ru-geru); _phase:ge-ru:geru_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1768.35 K, x(Ru) 0.5–0.5 | 7 | 1 |
| [HCP_A3](#phase-ge-ru-hcp-a3); _phase:ge-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.78 K, x(Ru) 0.99852–1 | 3 | 1 |
| [LIQUID](#phase-ge-ru-liquid); _phase:ge-ru:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1202.39–4000 K, x(Ru) 0–1 | 20 | 1 |

## DIAMOND_A4 (Ge–Ru)

- Id: `phase:ge-ru:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Ru) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:a4-diamond)

Names (4): _corpus: _corpus:phase:ge-ru:a4-diamond, corpus:phase:ge-ru:diamond-a4  
_paper: _paper:10.1016/j.jallcom.2009.01.079:Diamond (Ge)  
_tdb: _tdb:GeRu-09Lon.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): DIAMOND_A4, type code %, sha256 `f71e50a0da5d0d63…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02665783](https://doi.org/10.1007/bf02665783) L. Perring, P. Feschotte, J. C. Gachon, The germanium-ruthenium system, JPE 17, 101-106 (1996).  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Ru)

- Id: `phase:ge-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-ru:bcc-a2  
_tdb: _tdb:GeRu-09Lon.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): BCC_A2, type code %B, sha256 `f71e50a0da5d0d63…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : GE RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase_

## FCC_A1 (Ge–Ru)

- Id: `phase:ge-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-ru:fcc-a1  
_tdb: _tdb:GeRu-09Lon.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): FCC_A1, type code %A, sha256 `f71e50a0da5d0d63…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : GE RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase_

## GE3RU2_ALPHA (Ge–Ru)

- Id: `phase:ge-ru:ge3ru2-alpha`; status `assigned`
- Structure: Ge3Ru2 · oP40 · Pbcn (60); type `st:ge3ru2-op40`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.6000, Ru 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–859.97 K, x(Ru) 0.4–0.4
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:ge3ru2-alpha)

Names (3): _corpus: _corpus:phase:ge-ru:ge3ru2-alpha  
_paper: _paper:10.1016/j.jallcom.2009.01.079:αRu2Ge3  
_tdb: _tdb:GeRu-09Lon.tdb:GE3RU2_ALPHA  


### TDB models of GE3RU2_ALPHA (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): GE3RU2_ALPHA, type code %, sha256 `f71e50a0da5d0d63…`

~~~~text
49: PHASE GE3RU2_ALPHA % 2 3 2 !
50: CONST GE3RU2_ALPHA : GE : RU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1997.7508](https://doi.org/10.1006/jssc.1997.7508) J.J. Kuntz, L. Perring, P. Feschotte, J.C. Gachon, Heat Capacity and Heat Content Measurements on Binary Compounds in the Ru–Si, Ru–Ge, and Ru–Sn Systems, Journal of Solid State Chemistry 133, 439-444 (1997).  
_cited as the source of values for this phase_

## GE3RU2_BETA (Ge–Ru)

- Id: `phase:ge-ru:ge3ru2-beta`; status `assigned`
- Structure: Ru2Sn3 · tP20 · P-4c2 (116); type `st:ru2sn3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.6000, Ru 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 859.97–1822.35 K, x(Ru) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:ge3ru2-beta)

Names (2): _corpus: _corpus:phase:ge-ru:ge3ru2-beta  
_tdb: _tdb:GeRu-09Lon.tdb:GE3RU2_BETA  


### TDB models of GE3RU2_BETA (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): GE3RU2_BETA, type code %, sha256 `f71e50a0da5d0d63…`

~~~~text
54: PHASE GE3RU2_BETA % 2 3 2 !
55: CONST GE3RU2_BETA : GE : RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase_

## GERU (Ge–Ru)

- Id: `phase:ge-ru:geru`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): CsCl · cP2 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for GERU: GeRu (high T, see also FeSi)
- Candidate (sgte_mmc2): FeSi · B20 · cP8 · P2_13 (198) — Hallstedt 2025 mmc2 row for GERU: GeRu (low T, see also CsCl)
- Candidate (tdb_comment): FeSi · cP8 · P2_13 — GeRu-09Lon.tdb: 'Prototype FeSi (cP8, P2_13), low T'
- Stoichiometry: Ge 0.5000, Ru 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1768.35 K, x(Ru) 0.5–0.5
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:geru)

Names (3): _corpus: _corpus:phase:ge-ru:geru  
_paper: _paper:10.1016/j.jallcom.2009.01.079:RuGe  
_tdb: _tdb:GeRu-09Lon.tdb:GERU  


### TDB models of GERU (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): GERU, type code %, sha256 `f71e50a0da5d0d63…`

~~~~text
60: PHASE GERU % 2 1 1 !
61: CONST GERU : GE : RU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02665783](https://doi.org/10.1007/bf02665783) L. Perring, P. Feschotte, J. C. Gachon, The germanium-ruthenium system, JPE 17, 101-106 (1996).  
_cited as the source of values for this phase_
- [doi:10.1361/105497198770341932](https://doi.org/10.1361/105497198770341932) J. Charles, L. Perring, J. C. Gachon, Optimization of the binary Ge-Ru system, JPE 19, 449-454 (1998).  
_cited as the source of values for this phase_

## HCP_A3 (Ge–Ru)

- Id: `phase:ge-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.78 K, x(Ru) 0.99852–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:hcp-a3)

Names (3): _corpus: _corpus:phase:ge-ru:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.01.079:Hcp (Ru)  
_tdb: _tdb:GeRu-09Lon.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): HCP_A3, type code %A, sha256 `f71e50a0da5d0d63…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : GE RU% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02665783](https://doi.org/10.1007/bf02665783) L. Perring, P. Feschotte, J. C. Gachon, The germanium-ruthenium system, JPE 17, 101-106 (1996).  
_cited as the source of values for this phase_
- [doi:10.1361/105497198770341932](https://doi.org/10.1361/105497198770341932) J. Charles, L. Perring, J. C. Gachon, Optimization of the binary Ge-Ru system, JPE 19, 449-454 (1998).  
_cited as the source of values for this phase_

## LIQUID (Ge–Ru)

- Id: `phase:ge-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1202.39–4000 K, x(Ru) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ru:liquid)

Names (4): _corpus: _corpus:phase:ge-ru:liquid  
_paper: _paper:10.1016/j.jallcom.2009.01.079:L, paper:10.1016/j.jallcom.2009.01.079:liquid  
_tdb: _tdb:GeRu-09Lon.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeRu-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb): LIQUID, type code %, sha256 `f71e50a0da5d0d63…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GE RU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02665783](https://doi.org/10.1007/bf02665783) L. Perring, P. Feschotte, J. C. Gachon, The germanium-ruthenium system, JPE 17, 101-106 (1996).  
_cited as the source of values for this phase_
- [doi:10.1361/105497198770341932](https://doi.org/10.1361/105497198770341932) J. Charles, L. Perring, J. C. Gachon, Optimization of the binary Ge-Ru system, JPE 19, 449-454 (1998).  
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
