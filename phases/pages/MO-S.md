# Mo–S phases

> Mo–S system: 10 phases (tier A 5, tier C 1, liquid 1, gas 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-S.html · Markdown: https://data.orchid-project.org/phases/pages/MO-S.md

10 phases (tier A 5, tier C 1, liquid 1, gas 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-S) · [full JSON](https://data.orchid-project.org/phases/systems/MO-S.json) · [Mo–S system page](https://data.orchid-project.org/systems/MO-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–S system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-mo-s-a16-orthorhombic); _phase:mo-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(S) 1–1 | 0 | 1 |
| [BCC_A2](#phase-mo-s-bcc-a2); _phase:mo-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2896.99 K, x(S) 0–0.02647 | 22 | 1 |
| [FCC_A1](#phase-mo-s-fcc-a1); _phase:mo-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-mo-s-gas); _phase:mo-s:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 690.29–4000 K, x(S) 0.94459–1 | 11 | 1 |
| [HCP_A3](#phase-mo-s-hcp-a3); _phase:mo-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-mo-s-liquid); _phase:mo-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.34–4000 K, x(S) 0–1 | 40 | 1 |
| [MO2S3_HT](#phase-mo-s-mo2s3-ht); _phase:mo-s:mo2s3-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1833–2026.77 K, x(S) 0.6–0.6 | 29 | 1 |
| [MO2S3_LT](#phase-mo-s-mo2s3-lt); _phase:mo-s:mo2s3-lt_ | Mo2S3 · mP10 · P2_1/m (11) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 882.97–1833 K, x(S) 0.6–0.6 | 11 | 1 |
| [MOS2_C7](#phase-mo-s-mos2-c7); _phase:mo-s:mos2-c7_ | MoS2 (2H) · C7 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1992.94 K, x(S) 0.65541–0.7152 | 28 | 1 |
| [MONOCLINIC_S](#phase-mo-s-s-monoclinic); _phase:mo-s:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## ORTHORHOMBIC_A16 (Mo–S)

- Id: `phase:mo-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:mo-s:a16-orthorhombic  
_tdb: _tdb:MoS-18Cui.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): ORTHORHOMBIC_A16, type code %, sha256 `f40ff1fdf8952ae3…`

~~~~text
55: PHASE ORTHORHOMBIC_A16 % 1 1 !
56: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase_

## BCC_A2 (Mo–S)

- Id: `phase:mo-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2896.99 K, x(S) 0–0.02647
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:bcc-a2)

Names (3): _corpus: _corpus:phase:mo-s:bcc-a2  
_paper: _paper:10.1016/j.tca.2017.12.011:bcc_A2  
_tdb: _tdb:MoS-18Cui.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): BCC_A2, type code %B, sha256 `f40ff1fdf8952ae3…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : MO% S : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bfb0047028](https://doi.org/10.1007/bfb0047028) Günter H. Moh, High-temperature metal sulfide chemistry, Topics in Current Chemistry, 107-151 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(83)90262-4](https://doi.org/10.1016/0036-9748%2883%2990262-4) William B. Johnson, William S. Hong, Dennis W. Readey, A molybdenum sulfur binary phase diagram, Scripta Metallurgica 17, 919-922 (1983).  
_cited as the source of values for this phase_
- [doi:10.1021/acs.nanolett.6b02443](https://doi.org/10.1021/acs.nanolett.6b02443) Shun-Li Shang, Greta Lindwall, Yi Wang, Joan M. Redwing, Tim Anderson, Zi-Kui Liu, Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides: Thermodynamic Insight into MoS\<sub>2\</sub>, Nano Lett. 16, 5742-5750 (2016).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.01.175](https://doi.org/10.1016/j.jallcom.2007.01.175) I.G. Vasilyeva, R.E. Nikolaev, High-temperature solid–vapor and liquid–vapor transitions in binary and ternary chalcogenides La2S3, MoS2, Mo2S3 and LiInSe2, Journal of Alloys and Compounds 452, 89-93 (2008).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1010115620439](https://doi.org/10.1023/a:1010115620439) Ya. I. Gibner, I. G. Vasilyeva, Rapid Heating in High-Temperature Thermomicroscopic Analysis, Journal of Thermal Analysis and Calorimetry 53, 151-160 (1998).  
_cited as the source of values for this phase_

## FCC_A1 (Mo–S)

- Id: `phase:mo-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Mo 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:fcc-a1)

Names (2): _corpus: _corpus:phase:mo-s:fcc-a1  
_tdb: _tdb:MoS-18Cui.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): FCC_A1, type code %A, sha256 `f40ff1fdf8952ae3…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase_

## GAS (Mo–S)

- Id: `phase:mo-s:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 690.29–4000 K, x(S) 0.94459–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:gas)

Names (4): _corpus: _corpus:phase:mo-s:gas  
_paper: _paper:10.1016/j.tca.2017.12.011:S2 (g), paper:10.1016/j.tca.2017.12.011:gas  
_tdb: _tdb:MoS-18Cui.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): GAS, type code %, sha256 `f40ff1fdf8952ae3…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : MO MO2 MOS MOS2 S S2 S3 S4 S5 S6 S7 S8 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/acs.nanolett.6b02443](https://doi.org/10.1021/acs.nanolett.6b02443) Shun-Li Shang, Greta Lindwall, Yi Wang, Joan M. Redwing, Tim Anderson, Zi-Kui Liu, Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides: Thermodynamic Insight into MoS\<sub>2\</sub>, Nano Lett. 16, 5742-5750 (2016).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.01.175](https://doi.org/10.1016/j.jallcom.2007.01.175) I.G. Vasilyeva, R.E. Nikolaev, High-temperature solid–vapor and liquid–vapor transitions in binary and ternary chalcogenides La2S3, MoS2, Mo2S3 and LiInSe2, Journal of Alloys and Compounds 452, 89-93 (2008).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1010115620439](https://doi.org/10.1023/a:1010115620439) Ya. I. Gibner, I. G. Vasilyeva, Rapid Heating in High-Temperature Thermomicroscopic Analysis, Journal of Thermal Analysis and Calorimetry 53, 151-160 (1998).  
_cited as the source of values for this phase_

## HCP_A3 (Mo–S)

- Id: `phase:mo-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mo 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:hcp-a3)

Names (2): _corpus: _corpus:phase:mo-s:hcp-a3  
_tdb: _tdb:MoS-18Cui.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): HCP_A3, type code %A, sha256 `f40ff1fdf8952ae3…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase_

## LIQUID (Mo–S)

- Id: `phase:mo-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.34–4000 K, x(S) 0–1
- Literature: 40 values (40 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:liquid)

Names (4): _corpus: _corpus:phase:mo-s:liquid  
_paper: _paper:10.1016/j.tca.2017.12.011:L, paper:10.1016/j.tca.2017.12.011:Liquid  
_tdb: _tdb:MoS-18Cui.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): LIQUID, type code %, sha256 `f40ff1fdf8952ae3…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : MO S : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/acs.nanolett.6b02443](https://doi.org/10.1021/acs.nanolett.6b02443) Shun-Li Shang, Greta Lindwall, Yi Wang, Joan M. Redwing, Tim Anderson, Zi-Kui Liu, Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides: Thermodynamic Insight into MoS\<sub>2\</sub>, Nano Lett. 16, 5742-5750 (2016).  
_cited as the source of values for this phase_
- [doi:10.1007/bfb0047028](https://doi.org/10.1007/bfb0047028) Günter H. Moh, High-temperature metal sulfide chemistry, Topics in Current Chemistry, 107-151 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.01.175](https://doi.org/10.1016/j.jallcom.2007.01.175) I.G. Vasilyeva, R.E. Nikolaev, High-temperature solid–vapor and liquid–vapor transitions in binary and ternary chalcogenides La2S3, MoS2, Mo2S3 and LiInSe2, Journal of Alloys and Compounds 452, 89-93 (2008).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(83)90262-4](https://doi.org/10.1016/0036-9748%2883%2990262-4) William B. Johnson, William S. Hong, Dennis W. Readey, A molybdenum sulfur binary phase diagram, Scripta Metallurgica 17, 919-922 (1983).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1010115620439](https://doi.org/10.1023/a:1010115620439) Ya. I. Gibner, I. G. Vasilyeva, Rapid Heating in High-Temperature Thermomicroscopic Analysis, Journal of Thermal Analysis and Calorimetry 53, 151-160 (1998).  
_cited as the source of values for this phase_

## MO2S3_HT (Mo–S)

- Id: `phase:mo-s:mo2s3-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Mo2S3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Mo2S3) — Hallstedt 2025 mmc2 row for MO2S3_HT: Mo2S3 (high T)
- Stoichiometry: Mo 0.4000, S 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 1833–2026.77 K, x(S) 0.6–0.6
- Literature: 29 values (29 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:mo2s3-ht)

Names (4): _corpus: _corpus:phase:mo-s:mo2s3-ht  
_paper: _paper:10.1016/j.tca.2017.12.011:Mo2S3, paper:10.1016/j.tca.2017.12.011:β\_Mo2S3  
_tdb: _tdb:MoS-18Cui.tdb:MO2S3_HT  


### TDB models of MO2S3_HT (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): MO2S3_HT, type code %, sha256 `f40ff1fdf8952ae3…`

~~~~text
70: PHASE MO2S3_HT % 2 2 3 !
71: CONST MO2S3_HT : MO : S : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bfb0047028](https://doi.org/10.1007/bfb0047028) Günter H. Moh, High-temperature metal sulfide chemistry, Topics in Current Chemistry, 107-151 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.01.175](https://doi.org/10.1016/j.jallcom.2007.01.175) I.G. Vasilyeva, R.E. Nikolaev, High-temperature solid–vapor and liquid–vapor transitions in binary and ternary chalcogenides La2S3, MoS2, Mo2S3 and LiInSe2, Journal of Alloys and Compounds 452, 89-93 (2008).  
_cited as the source of values for this phase_
- [doi:10.1021/acs.nanolett.6b02443](https://doi.org/10.1021/acs.nanolett.6b02443) Shun-Li Shang, Greta Lindwall, Yi Wang, Joan M. Redwing, Tim Anderson, Zi-Kui Liu, Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides: Thermodynamic Insight into MoS\<sub>2\</sub>, Nano Lett. 16, 5742-5750 (2016).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(83)90262-4](https://doi.org/10.1016/0036-9748%2883%2990262-4) William B. Johnson, William S. Hong, Dennis W. Readey, A molybdenum sulfur binary phase diagram, Scripta Metallurgica 17, 919-922 (1983).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1010115620439](https://doi.org/10.1023/a:1010115620439) Ya. I. Gibner, I. G. Vasilyeva, Rapid Heating in High-Temperature Thermomicroscopic Analysis, Journal of Thermal Analysis and Calorimetry 53, 151-160 (1998).  
_cited as the source of values for this phase_

## MO2S3_LT (Mo–S)

- Id: `phase:mo-s:mo2s3-lt`; status `assigned`
- Structure: Mo2S3 · mP10 · P2_1/m (11); type `st:mo2s3-mp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mo 0.4000, S 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 882.97–1833 K, x(S) 0.6–0.6
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:mo2s3-lt)

Names (3): _corpus: _corpus:phase:mo-s:mo2s3-lt  
_paper: _paper:10.1016/j.tca.2017.12.011:α\_Mo2S3  
_tdb: _tdb:MoS-18Cui.tdb:MO2S3_LT  


### TDB models of MO2S3_LT (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): MO2S3_LT, type code %, sha256 `f40ff1fdf8952ae3…`

~~~~text
65: PHASE MO2S3_LT % 2 2 3 !
66: CONST MO2S3_LT : MO : S : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bfb0047028](https://doi.org/10.1007/bfb0047028) Günter H. Moh, High-temperature metal sulfide chemistry, Topics in Current Chemistry, 107-151 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(83)90262-4](https://doi.org/10.1016/0036-9748%2883%2990262-4) William B. Johnson, William S. Hong, Dennis W. Readey, A molybdenum sulfur binary phase diagram, Scripta Metallurgica 17, 919-922 (1983).  
_cited as the source of values for this phase_
- [doi:10.1021/acs.nanolett.6b02443](https://doi.org/10.1021/acs.nanolett.6b02443) Shun-Li Shang, Greta Lindwall, Yi Wang, Joan M. Redwing, Tim Anderson, Zi-Kui Liu, Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides: Thermodynamic Insight into MoS\<sub>2\</sub>, Nano Lett. 16, 5742-5750 (2016).  
_cited as the source of values for this phase_

## MOS2_C7 (Mo–S)

- Id: `phase:mo-s:mos2-c7`; status `assigned`
- Structure: MoS2 (2H) · C7 · hP6 · P6_3/mmc (194); type `st:c7-mos2-2h-hp6`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1992.94 K, x(S) 0.65541–0.7152
- Literature: 28 values (28 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:mos2-c7)

Names (4): _corpus: _corpus:phase:mo-s:mos2-c7  
_paper: _paper:10.1016/j.tca.2017.12.011:2H_MoS2, paper:10.1016/j.tca.2017.12.011:MoS2  
_tdb: _tdb:MoS-18Cui.tdb:MOS2_C7  


### TDB models of MOS2_C7 (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): MOS2_C7, type code %, sha256 `f40ff1fdf8952ae3…`

~~~~text
75: PHASE MOS2_C7 % 2 1 2 !
76: CONST MOS2_C7 : MO% S : MO S% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/acs.nanolett.6b02443](https://doi.org/10.1021/acs.nanolett.6b02443) Shun-Li Shang, Greta Lindwall, Yi Wang, Joan M. Redwing, Tim Anderson, Zi-Kui Liu, Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides: Thermodynamic Insight into MoS\<sub>2\</sub>, Nano Lett. 16, 5742-5750 (2016).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(83)90262-4](https://doi.org/10.1016/0036-9748%2883%2990262-4) William B. Johnson, William S. Hong, Dennis W. Readey, A molybdenum sulfur binary phase diagram, Scripta Metallurgica 17, 919-922 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.01.175](https://doi.org/10.1016/j.jallcom.2007.01.175) I.G. Vasilyeva, R.E. Nikolaev, High-temperature solid–vapor and liquid–vapor transitions in binary and ternary chalcogenides La2S3, MoS2, Mo2S3 and LiInSe2, Journal of Alloys and Compounds 452, 89-93 (2008).  
_cited as the source of values for this phase_
- [doi:10.1007/bfb0047028](https://doi.org/10.1007/bfb0047028) Günter H. Moh, High-temperature metal sulfide chemistry, Topics in Current Chemistry, 107-151 (2006).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1010115620439](https://doi.org/10.1023/a:1010115620439) Ya. I. Gibner, I. G. Vasilyeva, Rapid Heating in High-Temperature Thermomicroscopic Analysis, Journal of Thermal Analysis and Calorimetry 53, 151-160 (1998).  
_cited as the source of values for this phase_

## MONOCLINIC_S (Mo–S)

- Id: `phase:mo-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — MoS-18Cui.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-s:s-monoclinic)

Names (2): _corpus: _corpus:phase:mo-s:s-monoclinic  
_tdb: _tdb:MoS-18Cui.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[MoS-18Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoS-18Cui.tdb): MONOCLINIC_S, type code %, sha256 `f40ff1fdf8952ae3…`

~~~~text
60: PHASE MONOCLINIC_S % 1 1 !
61: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2017.12.011](https://doi.org/10.1016/j.tca.2017.12.011) Senlin Cui, Biao Hu, Bin Ouyang, Dongdong Zhao, Thermodynamic assessment of the Mo-S system and its application in thermal decomposition of MoS 2, Thermochimica Acta 660, 44-55 (2018).  
_assessment that models this phase_

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
