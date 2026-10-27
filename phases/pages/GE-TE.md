# Ge–Te phases

> Ge–Te system: 9 phases (tier A 6, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-TE.html · Markdown: https://data.orchid-project.org/phases/pages/GE-TE.md

9 phases (tier A 6, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-TE) · [full JSON](https://data.orchid-project.org/phases/systems/GE-TE.json) · [Ge–Te system page](https://data.orchid-project.org/systems/GE-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Te system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-te-a4-diamond); _phase:ge-te:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Te) 0–0 | 15 | 1 |
| [HEXAGONAL_A8](#phase-ge-te-a8-hexagonal); _phase:ge-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 11 | 1 |
| [BCC_A2](#phase-ge-te-bcc-a2); _phase:ge-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ge-te-fcc-a1); _phase:ge-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GETE_B1](#phase-ge-te-gete-b1); _phase:ge-te:gete-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 678.15–2500 K, x(Te) 0.50033–1 | 41 | 1 |
| [GETE_GAMMA](#phase-ge-te-gete-gamma); _phase:ge-te:gete-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–638.83 K, x(Te) 0.51–0.51 | 8 | 1 |
| [GETE_LOW](#phase-ge-te-gete-low); _phase:ge-te:gete-low_ | alpha-GeTe · hR2 · R3m (160) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–703.15 K, x(Te) 0.5–0.50799 | 39 | 1 |
| [HCP_A3](#phase-ge-te-hcp-a3); _phase:ge-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ge-te-liquid); _phase:ge-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 658.04–2500 K, x(Te) 0–1 | 19 | 1 |

## DIAMOND_A4 (Ge–Te)

- Id: `phase:ge-te:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Te) 0–0
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:a4-diamond)

Names (3): _corpus: _corpus:phase:ge-te:a4-diamond  
_paper: _paper:10.1016/s0364-5916(99)00012-7:Ge  
_tdb: _tdb:GeTe-99Sch-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): DIAMOND_A4, type code %, sha256 `4acca1dfd153da40…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase; reports values for this phase_

## HEXAGONAL_A8 (Ge–Te)

- Id: `phase:ge-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:a8-hexagonal)

Names (3): _corpus: _corpus:phase:ge-te:a8-hexagonal  
_paper: _paper:10.1016/s0364-5916(99)00012-7:Te  
_tdb: _tdb:GeTe-99Sch-LB.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): HEXAGONAL_A8, type code %, sha256 `4acca1dfd153da40…`

~~~~text
55: PHASE HEXAGONAL_A8 % 1 1 !
56: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Ge–Te)

- Id: `phase:ge-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-te:bcc-a2  
_tdb: _tdb:GeTe-99Sch-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): BCC_A2, type code %, sha256 `4acca1dfd153da40…`

~~~~text
38: PHASE BCC_A2 % 2 1 3 !
39: CONST BCC_A2 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase_

## FCC_A1 (Ge–Te)

- Id: `phase:ge-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-te:fcc-a1  
_tdb: _tdb:GeTe-99Sch-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): FCC_A1, type code %, sha256 `4acca1dfd153da40…`

~~~~text
33: PHASE FCC_A1 % 2 1 1 !
34: CONST FCC_A1 : GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase_

## GETE_B1 (Ge–Te)

- Id: `phase:ge-te:gete-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 678.15–2500 K, x(Te) 0.50033–1
- Literature: 41 values (41 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:gete-b1)

Names (4): _corpus: _corpus:phase:ge-te:gete-b1  
_paper: _paper:10.1016/s0364-5916(99)00012-7:β, paper:10.1016/s0364-5916(99)00012-7:β-GeTe  
_tdb: _tdb:GeTe-99Sch-LB.tdb:GETE_B1  


### TDB models of GETE_B1 (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): GETE_B1, type code %, sha256 `4acca1dfd153da40…`

~~~~text
65: PHASE GETE_B1 % 2 1 1 !
66: CONST GETE_B1 : GE% VA : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase; reports values for this phase_

## GETE_GAMMA (Ge–Te)

- Id: `phase:ge-te:gete-gamma`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): GeS · B16 · oP8 · Pnma (62) — Hallstedt 2025 mmc2 row for GETE_GAMMA: gamma-GeTe (low-T)
- Candidate (tdb_comment): GeS · oP8 · Pnma — GeTe-99Sch-LB.tdb: 'Prototype GeS (oP8, Pnma)'
- Stoichiometry: Ge 0.4900, Te 0.5100
- Stability: stable in 1 of 1 calculated diagram(s): 300–638.83 K, x(Te) 0.51–0.51
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:gete-gamma)

Names (4): _corpus: _corpus:phase:ge-te:gete-gamma  
_paper: _paper:10.1016/s0364-5916(99)00012-7:γ, paper:10.1016/s0364-5916(99)00012-7:γ-GeTe  
_tdb: _tdb:GeTe-99Sch-LB.tdb:GETE_GAMMA  


### TDB models of GETE_GAMMA (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): GETE_GAMMA, type code %, sha256 `4acca1dfd153da40…`

~~~~text
70: PHASE GETE_GAMMA % 2 49 51 !
71: CONST GETE_GAMMA : GE : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase; reports values for this phase_

## GETE_LOW (Ge–Te)

- Id: `phase:ge-te:gete-low`; status `assigned`
- Structure: alpha-GeTe · hR2 · R3m (160); type `st:alpha-gete-hr2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:LOW, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–703.15 K, x(Te) 0.5–0.50799
- Literature: 39 values (39 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:gete-low)

Names (4): _corpus: _corpus:phase:ge-te:gete-low  
_paper: _paper:10.1016/s0364-5916(99)00012-7:α, paper:10.1016/s0364-5916(99)00012-7:α-GeTe  
_tdb: _tdb:GeTe-99Sch-LB.tdb:GETE_LOW  


### TDB models of GETE_LOW (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): GETE_LOW, type code %, sha256 `4acca1dfd153da40…`

~~~~text
60: PHASE GETE_LOW % 2 1 1 !
61: CONST GETE_LOW : GE% VA : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ge–Te)

- Id: `phase:ge-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-te:hcp-a3  
_tdb: _tdb:GeTe-99Sch-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): HCP_A3, type code %, sha256 `4acca1dfd153da40…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : GE : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
_assessment that models this phase_

## LIQUID (Ge–Te)

- Id: `phase:ge-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 658.04–2500 K, x(Te) 0–1
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-te:liquid)

Names (3): _corpus: _corpus:phase:ge-te:liquid  
_paper: _paper:10.1016/s0364-5916(99)00012-7:L  
_tdb: _tdb:GeTe-99Sch-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeTe-99Sch-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb): LIQUID, type code %, sha256 `4acca1dfd153da40…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : GE GETE TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999).  
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
