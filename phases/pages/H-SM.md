# H–Sm phases

> H–Sm system: 9 phases (tier A 4, tier C 1, liquid 1, gas 2, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-SM.html · Markdown: https://data.orchid-project.org/phases/pages/H-SM.md

9 phases (tier A 4, tier C 1, liquid 1, gas 2, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-SM) · [full JSON](https://data.orchid-project.org/phases/systems/H-SM.json) · [H–Sm system page](https://data.orchid-project.org/systems/H-SM.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-SM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Sm system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-sm-bcc-a2); _phase:h-sm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1181.24–1388.54 K, x(H) 0–0.30379 | 2 | 1 |
| [FCC_A1](#phase-h-sm-fcc-a1); _phase:h-sm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-h-sm-gas); _phase:h-sm:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300.77–2500 K, x(H) 0–1 | 1 | 1 |
| [H2GAS](#phase-h-sm-h2gas); _phase:h-sm:h2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–1025.77 K, x(H) 1–1 | 2 | 1 |
| [HCP_A3](#phase-h-sm-hcp-a3); _phase:h-sm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 788.63–1275.5 K, x(H) 0–0.24289 | 3 | 1 |
| [LIQUID](#phase-h-sm-liquid); _phase:h-sm:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1345–2066.83 K, x(H) 0–0.34012 | 2 | 1 |
| [RHOMB_C19](#phase-h-sm-rhomb-c19); _phase:h-sm:rhomb-c19_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1006.98 K, x(H) 0–0.08519 | 2 | 1 |
| [SMH2_C1](#phase-h-sm-smh2-c1); _phase:h-sm:smh2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1493.46 K, x(H) 0.62188–0.71672 | 7 | 1 |
| [SMH3](#phase-h-sm-smh3); _phase:h-sm:smh3_ | HoH3 · hP24 · P-3c1 (165) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–580.77 K, x(H) 0.73094–0.74986 | 2 | 1 |

## BCC_A2 (H–Sm)

- Id: `phase:h-sm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1181.24–1388.54 K, x(H) 0–0.30379
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:bcc-a2)

Names (3): _corpus: _corpus:phase:h-sm:bcc-a2  
_paper: _paper:10.1016/s0925-8388(01)01990-9:(γ-Sm)  
_tdb: _tdb:SmH-02Zin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): BCC_A2, type code %B, sha256 `3daabda9c80bc264…`

~~~~text
44: PHASE BCC_A2 %B 2 1 1 !
45: CONST BCC_A2 : SM : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (H–Sm)

- Id: `phase:h-sm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:fcc-a1)

Names (2): _corpus: _corpus:phase:h-sm:fcc-a1  
_tdb: _tdb:SmH-02Zin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): FCC_A1, type code %A, sha256 `3daabda9c80bc264…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : SM : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase_

## GAS (H–Sm)

- Id: `phase:h-sm:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.77–2500 K, x(H) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:gas)

Names (3): _corpus: _corpus:phase:h-sm:gas  
_paper: _paper:10.1016/s0925-8388(01)01990-9:H2  
_tdb: _tdb:SmH-02Zin.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): GAS, type code %, sha256 `3daabda9c80bc264…`

~~~~text
68: PHASE GAS:G % 1 1 !
69: CONST GAS:G : H H2 SM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_

## H2GAS (H–Sm)

- Id: `phase:h-sm:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1025.77 K, x(H) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:h2gas)

Names (3): _corpus: _corpus:phase:h-sm:h2gas  
_paper: _paper:10.1016/s0925-8388(01)01990-9:H2  
_tdb: _tdb:SmH-02Zin.tdb:H2GAS  


### TDB models of H2GAS (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): H2GAS, type code %, sha256 `3daabda9c80bc264…`

~~~~text
71: PHASE H2GAS % 1 1 !
72: CONST H2GAS : H2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90025-3](https://doi.org/10.1016/0022-5088%2874%2990025-3) M.H. Mintz, Z. Hadari, M. Bixon, Phase transformations in some rare earth-hydrogen systems, Journal of the Less Common Metals 37, 331-335 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90006-0](https://doi.org/10.1016/0022-5088%2876%2990006-0) M.H. Mintz, D. Hiershler, Z. Hadari, Systematic study of the h.c.p. ⇌ f.c.c. transitions in the heavier LnH2-LnH3 systems, Journal of the Less Common Metals 48, 241-249 (1976).  
_cited as the source of values for this phase_

## HCP_A3 (H–Sm)

- Id: `phase:h-sm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 788.63–1275.5 K, x(H) 0–0.24289
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:hcp-a3)

Names (3): _corpus: _corpus:phase:h-sm:hcp-a3  
_paper: _paper:10.1016/s0925-8388(01)01990-9:(β-Sm)  
_tdb: _tdb:SmH-02Zin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): HCP_A3, type code %A, sha256 `3daabda9c80bc264…`

~~~~text
50: PHASE HCP_A3 %A 2 1 1 !
51: CONST HCP_A3 : SM : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_

## LIQUID (H–Sm)

- Id: `phase:h-sm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1345–2066.83 K, x(H) 0–0.34012
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:liquid)

Names (3): _corpus: _corpus:phase:h-sm:liquid  
_paper: _paper:10.1016/s0925-8388(01)01990-9:L  
_tdb: _tdb:SmH-02Zin.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): LIQUID, type code %, sha256 `3daabda9c80bc264…`

~~~~text
33: PHASE LIQUID:L % 2 1 1 !
34: CONST LIQUID:L : SM : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_

## RHOMB_C19 (H–Sm)

- Id: `phase:h-sm:rhomb-c19`; status `needs_review`
- No structure assigned. Why: site_ratios_contradict_C19:SmH-02Zin.tdb
- Candidate (name_token): CdCl2 · C19 · hR3 · R-3m (166) — Strukturbericht/word 'C19' in the TDB name
- Candidate (tdb_comment): alpha-Sm · hR3 · R-3m — SmH-02Zin.tdb: 'Prototype alpha-Sm (hR3, R-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1006.98 K, x(H) 0–0.08519
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:rhomb-c19)

Names (3): _corpus: _corpus:phase:h-sm:rhomb-c19  
_paper: _paper:10.1016/s0925-8388(01)01990-9:(α-Sm)  
_tdb: _tdb:SmH-02Zin.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): RHOMB_C19, type code %, sha256 `3daabda9c80bc264…`

~~~~text
55: PHASE RHOMB_C19 % 2 1 1 !
56: CONST RHOMB_C19 : SM : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_

## SMH2_C1 (H–Sm)

- Id: `phase:h-sm:smh2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1493.46 K, x(H) 0.62188–0.71672
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:smh2-c1)

Names (4): _corpus: _corpus:phase:h-sm:smh2-c1  
_paper: _paper:10.1016/s0925-8388(01)01990-9:SmH2-x, paper:10.1016/s0925-8388(01)01990-9:SmH2±x  
_tdb: _tdb:SmH-02Zin.tdb:SMH2_C1  


### TDB models of SMH2_C1 (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): SMH2_C1, type code %, sha256 `3daabda9c80bc264…`

~~~~text
60: PHASE SMH2_C1 % 3 1 2 1 !
61: CONST SMH2_C1 : SM : H VA : H VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90025-3](https://doi.org/10.1016/0022-5088%2874%2990025-3) M.H. Mintz, Z. Hadari, M. Bixon, Phase transformations in some rare earth-hydrogen systems, Journal of the Less Common Metals 37, 331-335 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90006-0](https://doi.org/10.1016/0022-5088%2876%2990006-0) M.H. Mintz, D. Hiershler, Z. Hadari, Systematic study of the h.c.p. ⇌ f.c.c. transitions in the heavier LnH2-LnH3 systems, Journal of the Less Common Metals 48, 241-249 (1976).  
_cited as the source of values for this phase_

## SMH3 (H–Sm)

- Id: `phase:h-sm:smh3`; status `assigned`
- Structure: HoH3 · hP24 · P-3c1 (165); type `st:hoh3-hp24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–580.77 K, x(H) 0.73094–0.74986
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-sm:smh3)

Names (3): _corpus: _corpus:phase:h-sm:smh3  
_paper: _paper:10.1016/s0925-8388(01)01990-9:SmH3-y  
_tdb: _tdb:SmH-02Zin.tdb:SMH3  


### TDB models of SMH3 (1): PHASE and CONSTITUENT statements as written

[SmH-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/SmH-02Zin.tdb): SMH3, type code %, sha256 `3daabda9c80bc264…`

~~~~text
65: PHASE SMH3 % 3 1 2 1 !
66: CONST SMH3 : SM : H : H VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01990-9](https://doi.org/10.1016/S0925-8388%2801%2901990-9) M. Zinkevich, N. Mattern, A. Handstein, O. Gutfleisch, J. Alloys Compd., 339, 118-139(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90025-3](https://doi.org/10.1016/0022-5088%2874%2990025-3) M.H. Mintz, Z. Hadari, M. Bixon, Phase transformations in some rare earth-hydrogen systems, Journal of the Less Common Metals 37, 331-335 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90006-0](https://doi.org/10.1016/0022-5088%2876%2990006-0) M.H. Mintz, D. Hiershler, Z. Hadari, Systematic study of the h.c.p. ⇌ f.c.c. transitions in the heavier LnH2-LnH3 systems, Journal of the Less Common Metals 48, 241-249 (1976).  
_cited as the source of values for this phase_

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
