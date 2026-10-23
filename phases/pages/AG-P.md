# Ag–P phases

> Ag–P system: 8 phases (tier A 3, tier B 1, tier C 1, liquid 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-P.html · Markdown: https://data.orchid-project.org/phases/pages/AG-P.md

8 phases (tier A 3, tier B 1, tier C 1, liquid 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-P) · [full JSON](https://data.orchid-project.org/phases/systems/AG-P.json) · [Ag–P system page](https://data.orchid-project.org/systems/AG-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–P system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG3P11](#phase-ag-p-ag3p11); _phase:ag-p:ag3p11_ | Ag3P11 · mC28 · Cm (8) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–829.93 K, x(P) 0.78571–0.78571 | 7 | 1 |
| [AGP2](#phase-ag-p-agp2); _phase:ag-p:agp2_ | CuP2 · mP12 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–910.63 K, x(P) 0.66667–0.66667 | 6 | 1 |
| [BCC_A2](#phase-ag-p-bcc-a2); _phase:ag-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ag-p-fcc-a1); _phase:ag-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1244.02 K, x(P) 0–5e-05 | 2 | 1 |
| [HCP_A3](#phase-ag-p-hcp-a3); _phase:ag-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-p-liquid); _phase:ag-p:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 826.49–2500 K, x(P) 0–1 | 3 | 1 |
| [RED_P](#phase-ag-p-p-red); _phase:ag-p:p-red_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–852.09 K, x(P) 1–1 | 0 | 1 |
| [WHITE_P](#phase-ag-p-p-white); _phase:ag-p:p-white_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## AG3P11 (Ag–P)

- Id: `phase:ag-p:ag3p11`; status `assigned`
- Structure: Ag3P11 · mC28 · Cm (8); type `st:ag3p11-mc28`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ag 0.2143, P 0.7857
- Stability: stable in 1 of 1 calculated diagram(s): 300–829.93 K, x(P) 0.78571–0.78571
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:ag3p11)

Names (5): _corpus: _corpus:phase:ag-p:ag3p11  
_mp: _mp:mp-aaaabpeb  
_oqmd: _oqmd:oqmd-5040  
_paper: _paper:10.1007/bf02881270:Ag3P11  
_tdb: _tdb:AgP-88Kar.tdb:AG3P11  


### TDB models of AG3P11 (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): AG3P11, type code %, sha256 `c7e56e409a01660f…`

~~~~text
61: PHASE AG3P11 % 2 3 11 !
62: CONST AG3P11 : AG : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase; reports values for this phase_

## AGP2 (Ag–P)

- Id: `phase:ag-p:agp2`; status `assigned`
- Structure: CuP2 · mP12 · P2_1/c (14); type `st:cup2-mp12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.3333, P 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–910.63 K, x(P) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:agp2)

Names (3): _corpus: _corpus:phase:ag-p:agp2  
_paper: _paper:10.1007/bf02881270:AgP2  
_tdb: _tdb:AgP-88Kar.tdb:AGP2  


### TDB models of AGP2 (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): AGP2, type code %, sha256 `c7e56e409a01660f…`

~~~~text
56: PHASE AGP2 % 2 1 2 !
57: CONST AGP2 : AG : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Ag–P)

- Id: `phase:ag-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-p:bcc-a2  
_tdb: _tdb:AgP-88Kar.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): BCC_A2, type code %B, sha256 `c7e56e409a01660f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AG P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase_

## FCC_A1 (Ag–P)

- Id: `phase:ag-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1244.02 K, x(P) 0–5e-05
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-p:fcc-a1  
_paper: _paper:10.1007/bf02881270:(Ag)  
_tdb: _tdb:AgP-88Kar.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): FCC_A1, type code %A, sha256 `c7e56e409a01660f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AG% P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ag–P)

- Id: `phase:ag-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-p:hcp-a3  
_tdb: _tdb:AgP-88Kar.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): HCP_A3, type code %A, sha256 `c7e56e409a01660f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase_

## LIQUID (Ag–P)

- Id: `phase:ag-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 826.49–2500 K, x(P) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:liquid)

Names (4): _corpus: _corpus:phase:ag-p:liquid  
_paper: _paper:10.1007/bf02881270:L1, paper:10.1007/bf02881270:L2  
_tdb: _tdb:AgP-88Kar.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): LIQUID, type code %, sha256 `c7e56e409a01660f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AG P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase; reports values for this phase_

## RED_P (Ag–P)

- Id: `phase:ag-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stability: stable in 1 of 1 calculated diagram(s): 300–852.09 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:p-red)

Names (3): _corpus: _corpus:phase:ag-p:p-red, corpus:phase:ag-p:red-p  
_tdb: _tdb:AgP-88Kar.tdb:RED_P  


### TDB models of RED_P (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): RED_P, type code %, sha256 `c7e56e409a01660f…`

~~~~text
51: PHASE RED_P % 1 1 !
52: CONST RED_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase_

## WHITE_P (Ag–P)

- Id: `phase:ag-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-p:p-white)

Names (2): _corpus: _corpus:phase:ag-p:p-white  
_tdb: _tdb:AgP-88Kar.tdb:WHITE_P  


### TDB models of WHITE_P (1): PHASE and CONSTITUENT statements as written

[AgP-88Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb): WHITE_P, type code %, sha256 `c7e56e409a01660f…`

~~~~text
46: PHASE WHITE_P % 1 1 !
47: CONST WHITE_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
