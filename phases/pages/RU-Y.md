# Ru–Y phases

> Ru–Y system: 9 phases (tier A 5, tier C 3, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RU-Y.html · Markdown: https://data.orchid-project.org/phases/pages/RU-Y.md

9 phases (tier A 5, tier C 3, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RU-Y) · [full JSON](https://data.orchid-project.org/phases/systems/RU-Y.json) · [Ru–Y system page](https://data.orchid-project.org/systems/RU-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/RU-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ru–Y system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ru-y-bcc-a2); _phase:ru-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1751–3999.75 K, x(Y) 0.99996–1 | 2 | 1 |
| [FCC_A1](#phase-ru-y-fcc-a1); _phase:ru-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ru-y-hcp-a3); _phase:ru-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2635.93 K, x(Y) 0–1 | 8 | 1 |
| [LIQUID](#phase-ru-y-liquid); _phase:ru-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1357.86–4000 K, x(Y) 0–1 | 26 | 1 |
| [RU25Y44](#phase-ru-y-ru25y44); _phase:ru-y:ru25y44_ | Ru25Y44 · oP276 · Pnna (52) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1546.93 K, x(Y) 0.63768–0.63768 | 8 | 1 |
| [RU2Y_C14](#phase-ru-y-ru2y-c14); _phase:ru-y:ru2y-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2248.43 K, x(Y) 0.33333–0.33333 | 12 | 1 |
| [RU2Y3](#phase-ru-y-ru2y3); _phase:ru-y:ru2y3_ | Er3Ru2 · hP10 · P6_3/m (176) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 310.97–1568.17 K, x(Y) 0.6–0.6 | 8 | 1 |
| [RU2Y5](#phase-ru-y-ru2y5); _phase:ru-y:ru2y5_ | Mn5C2 · mC28 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1573.39 K, x(Y) 0.71429–0.71429 | 12 | 1 |
| [RUY3_D011](#phase-ru-y-ruy3-d011); _phase:ru-y:ruy3-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 315.35–1509.78 K, x(Y) 0.75–0.75 | 8 | 1 |

## BCC_A2 (Ru–Y)

- Id: `phase:ru-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1751–3999.75 K, x(Y) 0.99996–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:bcc-a2)

Names (3): _corpus: _corpus:phase:ru-y:bcc-a2  
_paper: _paper:10.1007/s10973-010-1076-2:βY  
_tdb: _tdb:RuY-11Ait.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): BCC_A2, type code %B, sha256 `67a1011da0969b03…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : RU Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ru–Y)

- Id: `phase:ru-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:fcc-a1)

Names (2): _corpus: _corpus:phase:ru-y:fcc-a1  
_tdb: _tdb:RuY-11Ait.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): FCC_A1, type code %A, sha256 `67a1011da0969b03…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : RU Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase_

## HCP_A3 (Ru–Y)

- Id: `phase:ru-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2635.93 K, x(Y) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:hcp-a3)

Names (4): _corpus: _corpus:phase:ru-y:hcp-a3  
_paper: _paper:10.1007/s10973-010-1076-2:Ru, paper:10.1007/s10973-010-1076-2:αY  
_tdb: _tdb:RuY-11Ait.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): HCP_A3, type code %A, sha256 `67a1011da0969b03…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : RU% Y% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.7795](https://doi.org/10.1006/jssc.1998.7795) Selhaoui N, Charles J, Kleppa OJ, Bouirden L, Gachon JC. The Ruthenuim-Yttrium system: an experimental calorimetric study with a phase diagram optimization. J Solid State Chem. 1998; 138:302–6.  
_cited as the source of values for this phase_

## LIQUID (Ru–Y)

- Id: `phase:ru-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1357.86–4000 K, x(Y) 0–1
- Literature: 26 values (26 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:liquid)

Names (3): _corpus: _corpus:phase:ru-y:liquid  
_paper: _paper:10.1007/s10973-010-1076-2:Liq  
_tdb: _tdb:RuY-11Ait.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): LIQUID, type code %, sha256 `67a1011da0969b03…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : RU Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.7795](https://doi.org/10.1006/jssc.1998.7795) Selhaoui N, Charles J, Kleppa OJ, Bouirden L, Gachon JC. The Ruthenuim-Yttrium system: an experimental calorimetric study with a phase diagram optimization. J Solid State Chem. 1998; 138:302–6.  
_cited as the source of values for this phase_

## RU25Y44 (Ru–Y)

- Id: `phase:ru-y:ru25y44`; status `assigned`
- Structure: Ru25Y44 · oP276 · Pnna (52); type `st:ru25y44-op276`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.3623, Y 0.6377
- Stability: stable in 1 of 1 calculated diagram(s): 300–1546.93 K, x(Y) 0.63768–0.63768
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:ru25y44)

Names (3): _corpus: _corpus:phase:ru-y:ru25y44  
_paper: _paper:10.1007/s10973-010-1076-2:Ru25Y44  
_tdb: _tdb:RuY-11Ait.tdb:RU25Y44  


### TDB models of RU25Y44 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): RU25Y44, type code %, sha256 `67a1011da0969b03…`

~~~~text
58: PHASE RU25Y44 % 2 25 44 !
59: CONST RU25Y44 : RU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.7795](https://doi.org/10.1006/jssc.1998.7795) Selhaoui N, Charles J, Kleppa OJ, Bouirden L, Gachon JC. The Ruthenuim-Yttrium system: an experimental calorimetric study with a phase diagram optimization. J Solid State Chem. 1998; 138:302–6.  
_cited as the source of values for this phase_

## RU2Y_C14 (Ru–Y)

- Id: `phase:ru-y:ru2y-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgini and oqmd-19316, space group 194
- Stoichiometry: Ru 0.6667, Y 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2248.43 K, x(Y) 0.33333–0.33333
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:ru2y-c14)

Names (5): _corpus: _corpus:phase:ru-y:ru2y-c14  
_mp: _mp:mp-aaabgini  
_oqmd: _oqmd:oqmd-19316  
_paper: _paper:10.1007/s10973-010-1076-2:Ru2Y  
_tdb: _tdb:RuY-11Ait.tdb:RU2Y_C14  


### TDB models of RU2Y_C14 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): RU2Y_C14, type code %, sha256 `67a1011da0969b03…`

~~~~text
48: PHASE RU2Y_C14 % 2 2 1 !
49: CONST RU2Y_C14 : RU : Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.7795](https://doi.org/10.1006/jssc.1998.7795) Selhaoui N, Charles J, Kleppa OJ, Bouirden L, Gachon JC. The Ruthenuim-Yttrium system: an experimental calorimetric study with a phase diagram optimization. J Solid State Chem. 1998; 138:302–6.  
_cited as the source of values for this phase_
- [doi:10.1051/jcp/1993900435](https://doi.org/10.1051/jcp/1993900435) N Selhaoui, OJ Kleppa, Standard enthalpies of formation of yttrium alloys, Y-Me (Me = Ru, Rh, Pd, Os, Ir, Pt), by high-temperature calorimetry, J. Chim. Phys. 90, 435-443 (1993).  
_cited as the source of values for this phase_

## RU2Y3 (Ru–Y)

- Id: `phase:ru-y:ru2y3`; status `assigned`
- Structure: Er3Ru2 · hP10 · P6_3/m (176); type `st:er3ru2-hp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.4000, Y 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 310.97–1568.17 K, x(Y) 0.6–0.6
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:ru2y3)

Names (3): _corpus: _corpus:phase:ru-y:ru2y3  
_paper: _paper:10.1007/s10973-010-1076-2:Ru2Y3  
_tdb: _tdb:RuY-11Ait.tdb:RU2Y3  


### TDB models of RU2Y3 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): RU2Y3, type code %, sha256 `67a1011da0969b03…`

~~~~text
53: PHASE RU2Y3 % 2 2 3 !
54: CONST RU2Y3 : RU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.7795](https://doi.org/10.1006/jssc.1998.7795) Selhaoui N, Charles J, Kleppa OJ, Bouirden L, Gachon JC. The Ruthenuim-Yttrium system: an experimental calorimetric study with a phase diagram optimization. J Solid State Chem. 1998; 138:302–6.  
_cited as the source of values for this phase_

## RU2Y5 (Ru–Y)

- Id: `phase:ru-y:ru2y5`; status `assigned`
- Structure: Mn5C2 · mC28 · C2/c (15); type `st:mn5c2-mc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_15_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.2857, Y 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–1573.39 K, x(Y) 0.71429–0.71429
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:ru2y5)

Names (3): _corpus: _corpus:phase:ru-y:ru2y5  
_paper: _paper:10.1007/s10973-010-1076-2:Ru2Y5  
_tdb: _tdb:RuY-11Ait.tdb:RU2Y5  


### TDB models of RU2Y5 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): RU2Y5, type code %, sha256 `67a1011da0969b03…`

~~~~text
63: PHASE RU2Y5 % 2 2 5 !
64: CONST RU2Y5 : RU : Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.7795](https://doi.org/10.1006/jssc.1998.7795) Selhaoui N, Charles J, Kleppa OJ, Bouirden L, Gachon JC. The Ruthenuim-Yttrium system: an experimental calorimetric study with a phase diagram optimization. J Solid State Chem. 1998; 138:302–6.  
_cited as the source of values for this phase_
- [doi:10.1051/jcp/1993900435](https://doi.org/10.1051/jcp/1993900435) N Selhaoui, OJ Kleppa, Standard enthalpies of formation of yttrium alloys, Y-Me (Me = Ru, Rh, Pd, Os, Ir, Pt), by high-temperature calorimetry, J. Chim. Phys. 90, 435-443 (1993).  
_cited as the source of values for this phase_

## RUY3_D011 (Ru–Y)

- Id: `phase:ru-y:ruy3-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacqsrd and oqmd-1437321, space group 62
- Stoichiometry: Ru 0.2500, Y 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 315.35–1509.78 K, x(Y) 0.75–0.75
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-y:ruy3-d011)

Names (5): _corpus: _corpus:phase:ru-y:ruy3-d011  
_mp: _mp:mp-aaacqsrd  
_oqmd: _oqmd:oqmd-1437321  
_paper: _paper:10.1007/s10973-010-1076-2:RuY3  
_tdb: _tdb:RuY-11Ait.tdb:RUY3_D011  


### TDB models of RUY3_D011 (1): PHASE and CONSTITUENT statements as written

[RuY-11Ait.tdb](https://orchid-project.org/data/databases/sgte-binary/RuY-11Ait.tdb): RUY3_D011, type code %, sha256 `67a1011da0969b03…`

~~~~text
68: PHASE RUY3_D011 % 2 1 3 !
69: CONST RUY3_D011 : RU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-010-1076-2](https://doi.org/10.1007/s10973-010-1076-2) M. Ait Amar, M. Idbenali, N. Selhaoui, K. Mahdouk, A. Aharoune, L. Bouirden, Thermodynamic description of the Ru–Y binary system, J Therm Anal Calorim 103, 141-145 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1006/jssc.1998.7795](https://doi.org/10.1006/jssc.1998.7795) Selhaoui N, Charles J, Kleppa OJ, Bouirden L, Gachon JC. The Ruthenuim-Yttrium system: an experimental calorimetric study with a phase diagram optimization. J Solid State Chem. 1998; 138:302–6.  
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
