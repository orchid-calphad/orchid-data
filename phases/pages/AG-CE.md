# Ag–Ce phases

> Ag–Ce system: 8 phases (tier A 3, tier C 1, liquid 1, needs_review 3); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-CE.html · Markdown: https://data.orchid-project.org/phases/pages/AG-CE.md

8 phases (tier A 3, tier C 1, liquid 1, needs_review 3); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-CE) · [full JSON](https://data.orchid-project.org/phases/systems/AG-CE.json) · [Ag–Ce system page](https://data.orchid-project.org/systems/AG-CE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-CE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ce system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2CE](#phase-ag-ce-ag2ce); _phase:ag-ce:ag2ce_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1121.34 K, x(Ce) 0.33333–0.33333 | 8 | 1 |
| [AG4CE](#phase-ag-ce-ag4ce); _phase:ag-ce:ag4ce_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1088.97 K, x(Ce) 0.2–0.2 | 8 | 1 |
| [AG51CE14](#phase-ag-ce-ag51ce14); _phase:ag-ce:ag51ce14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1306.47 K, x(Ce) 0.21538–0.21538 | 12 | 1 |
| [AGCE](#phase-ag-ce-agce); _phase:ag-ce:agce_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1123.3 K, x(Ce) 0.5–0.5 | 11 | 1 |
| [BCC_A2](#phase-ag-ce-bcc-a2); _phase:ag-ce:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 891.81–2499.5 K, x(Ce) 0.95478–1 | 3 | 1 |
| [FCC_A1](#phase-ag-ce-fcc-a1); _phase:ag-ce:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1259.48 K, x(Ce) 0–1 | 10 | 1 |
| [HCP_A3](#phase-ag-ce-hcp-a3); _phase:ag-ce:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-ce-liquid); _phase:ag-ce:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 788.95–2500 K, x(Ce) 0–1 | 30 | 1 |

## AG2CE (Ag–Ce)

- Id: `phase:ag-ce:ag2ce`; status `needs_review`
- No structure assigned. Why: dft_space_group_74_matches_2_structure_types; no_structure_token
- Candidate (dft_mp): Imma (74) — on-hull MP CeAg2 at x(CE)=0.3333
- Candidate (dft_oqmd): Imma (74) — on-hull OQMD Ag2 Ce1 at x(CE)=0.3333
- Candidate (dft_space_group_and_stoichiometry): CeCu2 · oI12 · Imma (74) — space group 74 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): Hg2K · oI12 · Imma (74) — space group 74 and stoichiometry match
- Candidate (sgte_mmc2): Hg2K · oI12 · Imma (74) — Hallstedt 2025 mmc2 row for AG2CE: Ag2Ce-alpha
- Candidate (tdb_comment): Hg2K · oI12 · Imma — AgCe-02Yin-LB.tdb: 'Prototype Hg2K (oI12, Imma), alpha'
- Stoichiometry: Ag 0.6667, Ce 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1121.34 K, x(Ce) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:ag2ce)

Names (3): _corpus: _corpus:phase:ag-ce:ag2ce  
_paper: _paper:10.1016/s0925-8388(01)01757-1:Ag2Ce  
_tdb: _tdb:AgCe-02Yin-LB.tdb:AG2CE  


### TDB models of AG2CE (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): AG2CE, type code %, sha256 `f1251075646ab97a…`

~~~~text
52: PHASE AG2CE % 2 2 1 !
53: CONST AG2CE : AG : CE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90239-4](https://doi.org/10.1016/0022-5088%2883%2990239-4) Isolde Stapf, Hermann Jehn, The Ag-Ce phase diagram I: Ag-Ag3Ce partial phase diagram, Journal of the Less Common Metals 92, 167-175 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90093-4](https://doi.org/10.1016/0022-5088%2875%2990093-4) S. Delfino, R. Ferro, R. Capelli, A. Borsese, Phase equilibria in the silver-cerium system, Journal of the Less Common Metals 41, 59-64 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90028-4](https://doi.org/10.1016/0022-5088%2880%2990028-4) Th. Heumann, A. Préval, The equilibrium diagram of the system Ag-50at.%Ce, Journal of the Less Common Metals 76, 263-270 (1980).  
_cited as the source of values for this phase_

## AG4CE (Ag–Ce)

- Id: `phase:ag-ce:ag4ce`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): P-1 (2) — on-hull OQMD Ag4 Ce1 at x(CE)=0.2000
- Candidate (literature_printed): (Ag4Ce) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ag4Ce) — Hallstedt 2025 mmc2 row for AG4CE: Ag4Ce
- Stoichiometry: Ag 0.8000, Ce 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1088.97 K, x(Ce) 0.2–0.2
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:ag4ce)

Names (3): _corpus: _corpus:phase:ag-ce:ag4ce  
_paper: _paper:10.1016/s0925-8388(01)01757-1:Ag4Ce  
_tdb: _tdb:AgCe-02Yin-LB.tdb:AG4CE  


### TDB models of AG4CE (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): AG4CE, type code %, sha256 `f1251075646ab97a…`

~~~~text
41: PHASE AG4CE % 2 4 1 !
42: CONST AG4CE : AG : CE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90239-4](https://doi.org/10.1016/0022-5088%2883%2990239-4) Isolde Stapf, Hermann Jehn, The Ag-Ce phase diagram I: Ag-Ag3Ce partial phase diagram, Journal of the Less Common Metals 92, 167-175 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90093-4](https://doi.org/10.1016/0022-5088%2875%2990093-4) S. Delfino, R. Ferro, R. Capelli, A. Borsese, Phase equilibria in the silver-cerium system, Journal of the Less Common Metals 41, 59-64 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90028-4](https://doi.org/10.1016/0022-5088%2880%2990028-4) Th. Heumann, A. Préval, The equilibrium diagram of the system Ag-50at.%Ce, Journal of the Less Common Metals 76, 263-270 (1980).  
_cited as the source of values for this phase_

## AG51CE14 (Ag–Ce)

- Id: `phase:ag-ce:ag51ce14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.7846, Ce 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–1306.47 K, x(Ce) 0.21538–0.21538
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:ag51ce14)

Names (3): _corpus: _corpus:phase:ag-ce:ag51ce14  
_paper: _paper:10.1016/s0925-8388(01)01757-1:Ag51Ce14  
_tdb: _tdb:AgCe-02Yin-LB.tdb:AG51CE14  


### TDB models of AG51CE14 (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): AG51CE14, type code %, sha256 `f1251075646ab97a…`

~~~~text
46: PHASE AG51CE14 % 2 51 14 !
47: CONST AG51CE14 : AG : CE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90239-4](https://doi.org/10.1016/0022-5088%2883%2990239-4) Isolde Stapf, Hermann Jehn, The Ag-Ce phase diagram I: Ag-Ag3Ce partial phase diagram, Journal of the Less Common Metals 92, 167-175 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90093-4](https://doi.org/10.1016/0022-5088%2875%2990093-4) S. Delfino, R. Ferro, R. Capelli, A. Borsese, Phase equilibria in the silver-cerium system, Journal of the Less Common Metals 41, 59-64 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90028-4](https://doi.org/10.1016/0022-5088%2880%2990028-4) Th. Heumann, A. Préval, The equilibrium diagram of the system Ag-50at.%Ce, Journal of the Less Common Metals 76, 263-270 (1980).  
_cited as the source of values for this phase_

## AGCE (Ag–Ce)

- Id: `phase:ag-ce:agce`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Ag1 Ce1 at x(CE)=0.5000
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for AGCE: AgCe-alpha
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — AgCe-02Yin-LB.tdb: 'Prototype CsCl (cP2, Pm-3m), alpha'
- Stoichiometry: Ag 0.5000, Ce 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1123.3 K, x(Ce) 0.5–0.5
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:agce)

Names (3): _corpus: _corpus:phase:ag-ce:agce  
_paper: _paper:10.1016/s0925-8388(01)01757-1:AgCe  
_tdb: _tdb:AgCe-02Yin-LB.tdb:AGCE  


### TDB models of AGCE (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): AGCE, type code %, sha256 `f1251075646ab97a…`

~~~~text
58: PHASE AGCE % 2 1 1 !
59: CONST AGCE : AG : CE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90239-4](https://doi.org/10.1016/0022-5088%2883%2990239-4) Isolde Stapf, Hermann Jehn, The Ag-Ce phase diagram I: Ag-Ag3Ce partial phase diagram, Journal of the Less Common Metals 92, 167-175 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90093-4](https://doi.org/10.1016/0022-5088%2875%2990093-4) S. Delfino, R. Ferro, R. Capelli, A. Borsese, Phase equilibria in the silver-cerium system, Journal of the Less Common Metals 41, 59-64 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90028-4](https://doi.org/10.1016/0022-5088%2880%2990028-4) Th. Heumann, A. Préval, The equilibrium diagram of the system Ag-50at.%Ce, Journal of the Less Common Metals 76, 263-270 (1980).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Ce)

- Id: `phase:ag-ce:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 891.81–2499.5 K, x(Ce) 0.95478–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-ce:bcc-a2  
_paper: _paper:10.1016/s0925-8388(01)01757-1:δ-Ce  
_tdb: _tdb:AgCe-02Yin-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): BCC_A2, type code %B, sha256 `f1251075646ab97a…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG CE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90239-4](https://doi.org/10.1016/0022-5088%2883%2990239-4) Isolde Stapf, Hermann Jehn, The Ag-Ce phase diagram I: Ag-Ag3Ce partial phase diagram, Journal of the Less Common Metals 92, 167-175 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90093-4](https://doi.org/10.1016/0022-5088%2875%2990093-4) S. Delfino, R. Ferro, R. Capelli, A. Borsese, Phase equilibria in the silver-cerium system, Journal of the Less Common Metals 41, 59-64 (1975).  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Ce)

- Id: `phase:ag-ce:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1259.48 K, x(Ce) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-ce:fcc-a1  
_paper: _paper:10.1016/s0925-8388(01)01757-1:Ag, paper:10.1016/s0925-8388(01)01757-1:γ-Ce  
_tdb: _tdb:AgCe-02Yin-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): FCC_A1, type code %A, sha256 `f1251075646ab97a…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% CE% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90239-4](https://doi.org/10.1016/0022-5088%2883%2990239-4) Isolde Stapf, Hermann Jehn, The Ag-Ce phase diagram I: Ag-Ag3Ce partial phase diagram, Journal of the Less Common Metals 92, 167-175 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90093-4](https://doi.org/10.1016/0022-5088%2875%2990093-4) S. Delfino, R. Ferro, R. Capelli, A. Borsese, Phase equilibria in the silver-cerium system, Journal of the Less Common Metals 41, 59-64 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90028-4](https://doi.org/10.1016/0022-5088%2880%2990028-4) Th. Heumann, A. Préval, The equilibrium diagram of the system Ag-50at.%Ce, Journal of the Less Common Metals 76, 263-270 (1980).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Ce)

- Id: `phase:ag-ce:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-ce:hcp-a3  
_tdb: _tdb:AgCe-02Yin-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): HCP_A3, type code %A, sha256 `f1251075646ab97a…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG CE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase_

## LIQUID (Ag–Ce)

- Id: `phase:ag-ce:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 788.95–2500 K, x(Ce) 0–1
- Literature: 30 values (30 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ce:liquid)

Names (3): _corpus: _corpus:phase:ag-ce:liquid  
_paper: _paper:10.1016/s0925-8388(01)01757-1:L  
_tdb: _tdb:AgCe-02Yin-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgCe-02Yin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCe-02Yin-LB.tdb): LIQUID, type code %, sha256 `f1251075646ab97a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG CE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)01757-1](https://doi.org/10.1016/S0925-8388%2801%2901757-1) F. Yin, M. Huang, X. Su, P. Zhang, Z. Li, Y. Shi, J. Alloys Compd., 334, 154-58(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90239-4](https://doi.org/10.1016/0022-5088%2883%2990239-4) Isolde Stapf, Hermann Jehn, The Ag-Ce phase diagram I: Ag-Ag3Ce partial phase diagram, Journal of the Less Common Metals 92, 167-175 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90093-4](https://doi.org/10.1016/0022-5088%2875%2990093-4) S. Delfino, R. Ferro, R. Capelli, A. Borsese, Phase equilibria in the silver-cerium system, Journal of the Less Common Metals 41, 59-64 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90028-4](https://doi.org/10.1016/0022-5088%2880%2990028-4) Th. Heumann, A. Préval, The equilibrium diagram of the system Ag-50at.%Ce, Journal of the Less Common Metals 76, 263-270 (1980).  
_cited as the source of values for this phase_

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
