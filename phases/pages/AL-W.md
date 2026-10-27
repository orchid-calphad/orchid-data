# Al–W phases

> Al–W system: 10 phases (tier A 4, tier B 2, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-W.html · Markdown: https://data.orchid-project.org/phases/pages/AL-W.md

10 phases (tier A 4, tier B 2, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-W) · [full JSON](https://data.orchid-project.org/phases/systems/AL-W.json) · [Al–W system page](https://data.orchid-project.org/systems/AL-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–W system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL12W](#phase-al-w-al12w); _phase:al-w:al12w_ | Al12W · cI26 · Im-3 (204) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–970.23 K, x(W) 0.07692–0.07692 | 11 | 2 |
| [AL2W_C40](#phase-al-w-al2w-c40); _phase:al-w:al2w-c40_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1199.74–1939.31 K, x(W) 0.33333–0.33333 | 10 | 2 |
| [AL4W](#phase-al-w-al4w); _phase:al-w:al4w_ | Al4W · mC30 · Cm (8) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1620.87 K, x(W) 0.2–0.2 | 10 | 2 |
| [AL5W](#phase-al-w-al5w); _phase:al-w:al5w_ | Al5W · hP12 · P6_322 (182) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–1149.59 K, x(W) 0.16667–0.16667 | 10 | 2 |
| [AL77W23](#phase-al-w-al77w23); _phase:al-w:al77w23_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1571.03–1648.23 K, x(W) 0.23–0.23 | 4 | 1 |
| [AL7W3](#phase-al-w-al7w3); _phase:al-w:al7w3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1580.05–1706.83 K, x(W) 0.3–0.3 | 4 | 1 |
| [BCC_A2](#phase-al-w-bcc-a2); _phase:al-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0.83995–1 | 8 | 2 |
| [FCC_A1](#phase-al-w-fcc-a1); _phase:al-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–933.6 K, x(W) 0–0.0003 | 4 | 2 |
| [HCP_A3](#phase-al-w-hcp-a3); _phase:al-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-al-w-liquid); _phase:al-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 918.48–4000 K, x(W) 0–1 | 22 | 2 |

## AL12W (Al–W)

- Id: `phase:al-w:al12w`; status `assigned`
- Structure: Al12W · cI26 · Im-3 (204); type `st:al12w-ci26`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.9231, W 0.0769
- Stability: stable in 2 of 2 calculated diagram(s): 300–970.23 K, x(W) 0.07692–0.07692
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:al12w)

Names (7): _corpus: _corpus:phase:al-w:al12w  
_mp: _mp:mp-aaaaaqpv  
_oqmd: _oqmd:oqmd-10607  
_paper: _paper:10.1016/j.calphad.2017.09.007:Al12W, paper:sha256-85fd53a1a176b694:Al12W  
_tdb: _tdb:AlW-17Wan.tdb:AL12W, tdb:AlW-98Sau-LB.tdb:AL12W  


### TDB models of AL12W (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): AL12W, type code %, sha256 `9d538d0d3abf4347…`

~~~~text
41: PHASE AL12W % 2 12 1 !
42: CONST AL12W : AL : W : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): AL12W, type code %, sha256 `f53367dbb2e51e09…`

~~~~text
44: PHASE AL12W % 2 12 1 !
45: CONST AL12W : AL : W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_

## AL2W_C40 (Al–W)

- Id: `phase:al-w:al2w-c40`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.6667, W 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 1199.74–1939.31 K, x(W) 0.33333–0.33333
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:al2w-c40)

Names (5): _corpus: _corpus:phase:al-w:al2w-c40  
_paper: _paper:10.1016/j.calphad.2017.09.007:Al2W, paper:sha256-85fd53a1a176b694:Al2W  
_tdb: _tdb:AlW-17Wan.tdb:AL2W_C40, tdb:AlW-98Sau-LB.tdb:AL2W_C40  


### TDB models of AL2W_C40 (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): AL2W_C40, type code %, sha256 `9d538d0d3abf4347…`

~~~~text
56: PHASE AL2W_C40 % 2 2 1 !
57: CONST AL2W_C40 : AL : W : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): AL2W_C40, type code %, sha256 `f53367dbb2e51e09…`

~~~~text
69: PHASE AL2W_C40 % 2 2 1 !
70: CONST AL2W_C40 : AL : W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_

## AL4W (Al–W)

- Id: `phase:al-w:al4w`; status `assigned`
- Structure: Al4W · mC30 · Cm (8); type `st:al4w-mc30`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.8000, W 0.2000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1620.87 K, x(W) 0.2–0.2
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:al4w)

Names (5): _corpus: _corpus:phase:al-w:al4w  
_paper: _paper:10.1016/j.calphad.2017.09.007:Al4W, paper:sha256-85fd53a1a176b694:Al4W  
_tdb: _tdb:AlW-17Wan.tdb:AL4W, tdb:AlW-98Sau-LB.tdb:AL4W  


### TDB models of AL4W (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): AL4W, type code %, sha256 `9d538d0d3abf4347…`

~~~~text
51: PHASE AL4W % 2 4 1 !
52: CONST AL4W : AL : W : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): AL4W, type code %, sha256 `f53367dbb2e51e09…`

~~~~text
54: PHASE AL4W % 2 4 1 !
55: CONST AL4W : AL : W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_

## AL5W (Al–W)

- Id: `phase:al-w:al5w`; status `assigned`
- Structure: Al5W · hP12 · P6_322 (182); type `st:al5w-hp12`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.8333, W 0.1667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1149.59 K, x(W) 0.16667–0.16667
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:al5w)

Names (7): _corpus: _corpus:phase:al-w:al5w  
_mp: _mp:mp-aaaabswv  
_oqmd: _oqmd:oqmd-10606  
_paper: _paper:10.1016/j.calphad.2017.09.007:Al5W, paper:sha256-85fd53a1a176b694:Al5W  
_tdb: _tdb:AlW-17Wan.tdb:AL5W, tdb:AlW-98Sau-LB.tdb:AL5W  


### TDB models of AL5W (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): AL5W, type code %, sha256 `9d538d0d3abf4347…`

~~~~text
46: PHASE AL5W % 2 5 1 !
47: CONST AL5W : AL : W : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): AL5W, type code %, sha256 `f53367dbb2e51e09…`

~~~~text
49: PHASE AL5W % 2 5 1 !
50: CONST AL5W : AL : W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_

## AL77W23 (Al–W)

- Id: `phase:al-w:al77w23`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Al77W23) — Hallstedt 2025 mmc2 row for AL77W23: Al77W23
- Stoichiometry: Al 0.7700, W 0.2300
- Stability: stable in 1 of 1 calculated diagram(s): 1571.03–1648.23 K, x(W) 0.23–0.23
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:al77w23)

Names (3): _corpus: _corpus:phase:al-w:al77w23  
_paper: _paper:sha256-85fd53a1a176b694:Al77W23  
_tdb: _tdb:AlW-98Sau-LB.tdb:AL77W23  


### TDB models of AL77W23 (1): PHASE and CONSTITUENT statements as written

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): AL77W23, type code %, sha256 `f53367dbb2e51e09…`

~~~~text
59: PHASE AL77W23 % 2 77 23 !
60: CONST AL77W23 : AL : W : !
~~~~

## AL7W3 (Al–W)

- Id: `phase:al-w:al7w3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Al7W3) — Hallstedt 2025 mmc2 row for AL7W3: Al7W3
- Stoichiometry: Al 0.7000, W 0.3000
- Stability: stable in 1 of 1 calculated diagram(s): 1580.05–1706.83 K, x(W) 0.3–0.3
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:al7w3)

Names (3): _corpus: _corpus:phase:al-w:al7w3  
_paper: _paper:sha256-85fd53a1a176b694:Al7W3  
_tdb: _tdb:AlW-98Sau-LB.tdb:AL7W3  


### TDB models of AL7W3 (1): PHASE and CONSTITUENT statements as written

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): AL7W3, type code %, sha256 `f53367dbb2e51e09…`

~~~~text
64: PHASE AL7W3 % 2 7 3 !
65: CONST AL7W3 : AL : W : !
~~~~

## BCC_A2 (Al–W)

- Id: `phase:al-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0.83995–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:bcc-a2)

Names (5): _corpus: _corpus:phase:al-w:bcc-a2  
_paper: _paper:10.1016/j.calphad.2017.09.007:(W), paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:AlW-17Wan.tdb:BCC_A2, tdb:AlW-98Sau-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): BCC_A2, type code %B, sha256 `9d538d0d3abf4347…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AL W : VA : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): BCC_A2, type code %B, sha256 `f53367dbb2e51e09…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Al–W)

- Id: `phase:al-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–933.6 K, x(W) 0–0.0003
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:fcc-a1)

Names (5): _corpus: _corpus:phase:al-w:fcc-a1  
_paper: _paper:10.1016/j.calphad.2017.09.007:(Al), paper:sha256-85fd53a1a176b694:fcc-A  
_tdb: _tdb:AlW-17Wan.tdb:FCC_A1, tdb:AlW-98Sau-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): FCC_A1, type code %A, sha256 `9d538d0d3abf4347…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AL W : VA : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): FCC_A1, type code %A, sha256 `f53367dbb2e51e09…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Al–W)

- Id: `phase:al-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:hcp-a3)

Names (3): _corpus: _corpus:phase:al-w:hcp-a3  
_tdb: _tdb:AlW-17Wan.tdb:HCP_A3, tdb:AlW-98Sau-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): HCP_A3, type code %A, sha256 `9d538d0d3abf4347…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AL W : VA : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): HCP_A3, type code %A, sha256 `f53367dbb2e51e09…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase_

## LIQUID (Al–W)

- Id: `phase:al-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 918.48–4000 K, x(W) 0–1
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-w:liquid)

Names (5): _corpus: _corpus:phase:al-w:liquid  
_paper: _paper:10.1016/j.calphad.2017.09.007:L, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:AlW-17Wan.tdb:LIQUID, tdb:AlW-98Sau-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AlW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-17Wan.tdb): LIQUID, type code %, sha256 `9d538d0d3abf4347…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AL W : !
~~~~

[AlW-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlW-98Sau-LB.tdb): LIQUID, type code %, sha256 `f53367dbb2e51e09…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
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
