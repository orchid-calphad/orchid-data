# Bi–Cs phases

> Bi–Cs system: 9 phases (tier A 6, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-CS.html · Markdown: https://data.orchid-project.org/phases/pages/BI-CS.md

9 phases (tier A 6, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-CS) · [full JSON](https://data.orchid-project.org/phases/systems/BI-CS.json) · [Bi–Cs system page](https://data.orchid-project.org/systems/BI-CS.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-CS.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Cs system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-cs-a7-rhombohedral); _phase:bi-cs:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Cs) 0–0 | 4 | 1 |
| [BCC_A2](#phase-bi-cs-bcc-a2); _phase:bi-cs:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–301.5 K, x(Cs) 1–1 | 2 | 1 |
| [BI2CS_C15](#phase-bi-cs-bi2cs-c15); _phase:bi-cs:bi2cs-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–854.13 K, x(Cs) 0.33333–0.33333 | 11 | 1 |
| [BI2CS3](#phase-bi-cs-bi2cs3); _phase:bi-cs:bi2cs3_ | Eu3Ga2 · mC20 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–760 K, x(Cs) 0.6–0.6 | 8 | 1 |
| [BI4CS5](#phase-bi-cs-bi4cs5); _phase:bi-cs:bi4cs5_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–679.55 K, x(Cs) 0.55556–0.55556 | 5 | 1 |
| [BICS3_D03](#phase-bi-cs-bics3-d03); _phase:bi-cs:bics3-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–934.18 K, x(Cs) 0.75–0.75 | 10 | 1 |
| [FCC_A1](#phase-bi-cs-fcc-a1); _phase:bi-cs:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-cs-hcp-a3); _phase:bi-cs:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-bi-cs-liquid); _phase:bi-cs:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 301.5–2500 K, x(Cs) 0–1 | 24 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Cs)

- Id: `phase:bi-cs:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Cs) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-cs:a7-rhombohedral, corpus:phase:bi-cs:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2014.11.002:(Bi)  
_tdb: _tdb:BiCs-15Dja.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `f0497ab1e5628a60…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645965](https://doi.org/10.1007/bf02645965) J. Sangster, A. Pelton, The Bi–Cs (bismuth–cesium) system, J. Phase Equilib. 12 (1991) 443–446.  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Cs)

- Id: `phase:bi-cs:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–301.5 K, x(Cs) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:bcc-a2)

Names (3): _corpus: _corpus:phase:bi-cs:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.11.002:(Cs)  
_tdb: _tdb:BiCs-15Dja.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): BCC_A2, type code %B, sha256 `f0497ab1e5628a60…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : BI CS% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645965](https://doi.org/10.1007/bf02645965) J. Sangster, A. Pelton, The Bi–Cs (bismuth–cesium) system, J. Phase Equilib. 12 (1991) 443–446.  
_cited as the source of values for this phase_

## BI2CS_C15 (Bi–Cs)

- Id: `phase:bi-cs:bi2cs-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabigx and oqmd-647553, space group 227
- Stoichiometry: Bi 0.6667, Cs 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–854.13 K, x(Cs) 0.33333–0.33333
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:bi2cs-c15)

Names (5): _corpus: _corpus:phase:bi-cs:bi2cs-c15  
_mp: _mp:mp-aaaabigx  
_oqmd: _oqmd:oqmd-647553  
_paper: _paper:10.1016/j.calphad.2014.11.002:Bi2Cs  
_tdb: _tdb:BiCs-15Dja.tdb:BI2CS_C15  


### TDB models of BI2CS_C15 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): BI2CS_C15, type code %, sha256 `f0497ab1e5628a60…`

~~~~text
52: PHASE BI2CS_C15 % 2 2 1 !
53: CONST BI2CS_C15 : BI : CS : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645965](https://doi.org/10.1007/bf02645965) J. Sangster, A. Pelton, The Bi–Cs (bismuth–cesium) system, J. Phase Equilib. 12 (1991) 443–446.  
_cited as the source of values for this phase_

## BI2CS3 (Bi–Cs)

- Id: `phase:bi-cs:bi2cs3`; status `assigned`
- Structure: Eu3Ga2 · mC20 · C2/c (15); type `st:eu3ga2-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4000, Cs 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–760 K, x(Cs) 0.6–0.6
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:bi2cs3)

Names (3): _corpus: _corpus:phase:bi-cs:bi2cs3  
_paper: _paper:10.1016/j.calphad.2014.11.002:Bi2Cs3  
_tdb: _tdb:BiCs-15Dja.tdb:BI2CS3  


### TDB models of BI2CS3 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): BI2CS3, type code %, sha256 `f0497ab1e5628a60…`

~~~~text
62: PHASE BI2CS3 % 2 2 3 !
63: CONST BI2CS3 : BI : CS : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645965](https://doi.org/10.1007/bf02645965) J. Sangster, A. Pelton, The Bi–Cs (bismuth–cesium) system, J. Phase Equilib. 12 (1991) 443–446.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_

## BI4CS5 (Bi–Cs)

- Id: `phase:bi-cs:bi4cs5`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_mp; no_structure_token
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Bi4 Cs5 at x(CS)=0.5556
- Candidate (literature_printed): Rb5As4 · mC20 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Rb5As4 · mC20 · C2/m (12) — Hallstedt 2025 mmc2 row for BI4CS5: Bi24Cs5
- Candidate (tdb_comment): Rb5As4 · mC20 · C2/m — BiCs-15Dja.tdb: 'Prototype Rb5As4 (mC20, C2/m)'
- Stoichiometry: Bi 0.4444, Cs 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–679.55 K, x(Cs) 0.55556–0.55556
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:bi4cs5)

Names (3): _corpus: _corpus:phase:bi-cs:bi4cs5  
_paper: _paper:10.1016/j.calphad.2014.11.002:Bi4Cs5  
_tdb: _tdb:BiCs-15Dja.tdb:BI4CS5  


### TDB models of BI4CS5 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): BI4CS5, type code %, sha256 `f0497ab1e5628a60…`

~~~~text
57: PHASE BI4CS5 % 2 4 5 !
58: CONST BI4CS5 : BI : CS : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645965](https://doi.org/10.1007/bf02645965) J. Sangster, A. Pelton, The Bi–Cs (bismuth–cesium) system, J. Phase Equilib. 12 (1991) 443–446.  
_cited as the source of values for this phase_

## BICS3_D03 (Bi–Cs)

- Id: `phase:bi-cs:bics3-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.2500, Cs 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–934.18 K, x(Cs) 0.75–0.75
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:bics3-d03)

Names (3): _corpus: _corpus:phase:bi-cs:bics3-d03  
_paper: _paper:10.1016/j.calphad.2014.11.002:BiCs3  
_tdb: _tdb:BiCs-15Dja.tdb:BICS3_D03  


### TDB models of BICS3_D03 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): BICS3_D03, type code %, sha256 `f0497ab1e5628a60…`

~~~~text
67: PHASE BICS3_D03 % 2 1 3 !
68: CONST BICS3_D03 : BI : CS : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645965](https://doi.org/10.1007/bf02645965) J. Sangster, A. Pelton, The Bi–Cs (bismuth–cesium) system, J. Phase Equilib. 12 (1991) 443–446.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Cs)

- Id: `phase:bi-cs:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-cs:fcc-a1  
_tdb: _tdb:BiCs-15Dja.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): FCC_A1, type code %A, sha256 `f0497ab1e5628a60…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : BI CS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase_

## HCP_A3 (Bi–Cs)

- Id: `phase:bi-cs:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-cs:hcp-a3  
_tdb: _tdb:BiCs-15Dja.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): HCP_A3, type code %A, sha256 `f0497ab1e5628a60…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : BI CS : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase_

## LIQUID (Bi–Cs)

- Id: `phase:bi-cs:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.5–2500 K, x(Cs) 0–1
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-cs:liquid)

Names (3): _corpus: _corpus:phase:bi-cs:liquid  
_paper: _paper:10.1016/j.calphad.2014.11.002:L  
_tdb: _tdb:BiCs-15Dja.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiCs-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb): LIQUID, type code %, sha256 `f0497ab1e5628a60…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : BI BICS BICS3 CS : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645965](https://doi.org/10.1007/bf02645965) J. Sangster, A. Pelton, The Bi–Cs (bismuth–cesium) system, J. Phase Equilib. 12 (1991) 443–446.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
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
