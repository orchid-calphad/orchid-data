# Co–Sc phases

> Co–Sc system: 8 phases (tier A 5, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-SC.html · Markdown: https://data.orchid-project.org/phases/pages/CO-SC.md

8 phases (tier A 5, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-SC) · [full JSON](https://data.orchid-project.org/phases/systems/CO-SC.json) · [Co–Sc system page](https://data.orchid-project.org/systems/CO-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Sc system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-sc-bcc-a2); _phase:co-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1601.82–2499.32 K, x(Sc) 0.99862–1 | 2 | 1 |
| [CO2SC_C15](#phase-co-sc-co2sc-c15); _phase:co-sc:co2sc-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1792.32 K, x(Sc) 0.30741–0.36353 | 6 | 1 |
| [COSC_B2](#phase-co-sc-cosc-b2); _phase:co-sc:cosc-b2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1322.24 K, x(Sc) 0.48–0.48 | 4 | 1 |
| [COSC2_C16](#phase-co-sc-cosc2-c16); _phase:co-sc:cosc2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1113.73 K, x(Sc) 0.66667–0.66667 | 6 | 1 |
| [COSC3](#phase-co-sc-cosc3); _phase:co-sc:cosc3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1092.49 K, x(Sc) 0.77–0.77 | 4 | 1 |
| [FCC_A1](#phase-co-sc-fcc-a1); _phase:co-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 694.47–1770.85 K, x(Sc) 0–0.00915 | 4 | 1 |
| [HCP_A3](#phase-co-sc-hcp-a3); _phase:co-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1812.96 K, x(Sc) 0–1 | 2 | 1 |
| [LIQUID](#phase-co-sc-liquid); _phase:co-sc:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1024.14–2500 K, x(Sc) 0–1 | 18 | 1 |

## BCC_A2 (Co–Sc)

- Id: `phase:co-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1601.82–2499.32 K, x(Sc) 0.99862–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:bcc-a2)

Names (3): _corpus: _corpus:phase:co-sc:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2007.11.069:βSc  
_tdb: _tdb:CoSc-08Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): BCC_A2, type code %B, sha256 `b016d43f8f1436b7…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CO SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

## CO2SC_C15 (Co–Sc)

- Id: `phase:co-sc:co2sc-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoSc-08Liu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1792.32 K, x(Sc) 0.30741–0.36353
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:co2sc-c15)

Names (3): _corpus: _corpus:phase:co-sc:co2sc-c15  
_paper: _paper:10.1016/j.jallcom.2007.11.069:Co2Sc  
_tdb: _tdb:CoSc-08Liu.tdb:CO2SC_C15  


### TDB models of CO2SC_C15 (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): CO2SC_C15, type code %, sha256 `b016d43f8f1436b7…`

~~~~text
47: PHASE CO2SC_C15 % 2 2 1 !
48: CONST CO2SC_C15 : CO% SC : CO SC% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

## COSC_B2 (Co–Sc)

- Id: `phase:co-sc:cosc-b2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_B2; stoichiometry_contradicts_B2:CoSc-08Liu.tdb
- Candidate (literature_printed): CsCl · cP2 — printed with a label mapped to this phase
- Candidate (name_token): CsCl · B2 · cP2 · Pm-3m (221) — Strukturbericht/word 'B2' in the TDB name
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for COSC_B2: CoSc
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — CoSc-08Liu.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Stoichiometry: Co 0.5200, Sc 0.4800
- Stability: stable in 1 of 1 calculated diagram(s): 300–1322.24 K, x(Sc) 0.48–0.48
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:cosc-b2)

Names (3): _corpus: _corpus:phase:co-sc:cosc-b2  
_paper: _paper:10.1016/j.jallcom.2007.11.069:CoSc  
_tdb: _tdb:CoSc-08Liu.tdb:COSC_B2  


### TDB models of COSC_B2 (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): COSC_B2, type code %, sha256 `b016d43f8f1436b7…`

~~~~text
52: PHASE COSC_B2 % 2 0.52 0.48 !
53: CONST COSC_B2 : CO : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

## COSC2_C16 (Co–Sc)

- Id: `phase:co-sc:cosc2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.3333, Sc 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1113.73 K, x(Sc) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:cosc2-c16)

Names (3): _corpus: _corpus:phase:co-sc:cosc2-c16  
_paper: _paper:10.1016/j.jallcom.2007.11.069:CoSc2  
_tdb: _tdb:CoSc-08Liu.tdb:COSC2_C16  


### TDB models of COSC2_C16 (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): COSC2_C16, type code %, sha256 `b016d43f8f1436b7…`

~~~~text
57: PHASE COSC2_C16 % 2 1 2 !
58: CONST COSC2_C16 : CO : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

## COSC3 (Co–Sc)

- Id: `phase:co-sc:cosc3`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (literature_printed): CoSc3 · oP32 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): CoSc3 · oP32 · Pnma (62) — Hallstedt 2025 mmc2 row for COSC3: CoSc3
- Candidate (tdb_comment): CoSc3 · oP32 · Pnma — CoSc-08Liu.tdb: 'Prototype CoSc3 (oP32, Pnma)'
- Stoichiometry: Co 0.2300, Sc 0.7700
- Stability: stable in 1 of 1 calculated diagram(s): 300–1092.49 K, x(Sc) 0.77–0.77
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:cosc3)

Names (3): _corpus: _corpus:phase:co-sc:cosc3  
_paper: _paper:10.1016/j.jallcom.2007.11.069:CoSc3  
_tdb: _tdb:CoSc-08Liu.tdb:COSC3  


### TDB models of COSC3 (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): COSC3, type code %, sha256 `b016d43f8f1436b7…`

~~~~text
62: PHASE COSC3 % 2 0.23 0.77 !
63: CONST COSC3 : CO : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Co–Sc)

- Id: `phase:co-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 694.47–1770.85 K, x(Sc) 0–0.00915
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:fcc-a1)

Names (3): _corpus: _corpus:phase:co-sc:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.11.069:αCo  
_tdb: _tdb:CoSc-08Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): FCC_A1, type code %A, sha256 `b016d43f8f1436b7…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CO% SC : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Co–Sc)

- Id: `phase:co-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1812.96 K, x(Sc) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:hcp-a3)

Names (3): _corpus: _corpus:phase:co-sc:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2007.11.069:αSc  
_tdb: _tdb:CoSc-08Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): HCP_A3, type code %A, sha256 `b016d43f8f1436b7…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CO% SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Co–Sc)

- Id: `phase:co-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1024.14–2500 K, x(Sc) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-sc:liquid)

Names (3): _corpus: _corpus:phase:co-sc:liquid  
_paper: _paper:10.1016/j.jallcom.2007.11.069:L  
_tdb: _tdb:CoSc-08Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoSc-08Liu.tdb): LIQUID, type code %, sha256 `b016d43f8f1436b7…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CO SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_

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
