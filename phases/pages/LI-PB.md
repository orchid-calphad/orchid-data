# Li–Pb phases

> Li–Pb system: 10 phases (tier A 5, tier C 4, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LI-PB.html · Markdown: https://data.orchid-project.org/phases/pages/LI-PB.md

10 phases (tier A 5, tier C 4, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LI-PB) · [full JSON](https://data.orchid-project.org/phases/systems/LI-PB.json) · [Li–Pb system page](https://data.orchid-project.org/systems/LI-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/LI-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Li–Pb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-li-pb-bcc-a2); _phase:li-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–456.29 K, x(Pb) 0–0 | 2 | 1 |
| [FCC_A1](#phase-li-pb-fcc-a1); _phase:li-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2175.61 K, x(Pb) 0.96783–1 | 7 | 1 |
| [HCP_A3](#phase-li-pb-hcp-a3); _phase:li-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LI3PB_D03](#phase-li-pb-li3pb-d03); _phase:li-pb:li3pb-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–931.06 K, x(Pb) 0.25–0.25 | 6 | 1 |
| [LI4PB](#phase-li-pb-li4pb); _phase:li-pb:li4pb_ | Li17Pb4 · cF420 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–921.06 K, x(Pb) 0.2–0.2 | 9 | 1 |
| [LI5PB2](#phase-li-pb-li5pb2); _phase:li-pb:li5pb2_ | Li8Pb3 · hR11 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–915.02 K, x(Pb) 0.28571–0.28571 | 9 | 1 |
| [LI7PB2](#phase-li-pb-li7pb2); _phase:li-pb:li7pb2_ | Li7Pb2 · hP9 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–998.56 K, x(Pb) 0.20816–0.22222 | 13 | 1 |
| [LIPB_ALPHA](#phase-li-pb-lipb-alpha); _phase:li-pb:lipb-alpha_ | alpha-LiPb · hR2 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–487.34 K, x(Pb) 0.47841–0.5114 | 6 | 1 |
| [LIPB_B2](#phase-li-pb-lipb-b2); _phase:li-pb:lipb-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 459.01–755.28 K, x(Pb) 0.46061–0.50937 | 15 | 1 |
| [LIQUID](#phase-li-pb-liquid); _phase:li-pb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 449.29–2500 K, x(Pb) 0–1 | 19 | 1 |

## BCC_A2 (Li–Pb)

- Id: `phase:li-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–456.29 K, x(Pb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:bcc-a2)

Names (3): _corpus: _corpus:phase:li-pb:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:bcc  
_tdb: _tdb:LiPb-16Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): BCC_A2, type code %B, sha256 `d85ea4e948ee390a…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : LI% PB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_

## FCC_A1 (Li–Pb)

- Id: `phase:li-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2175.61 K, x(Pb) 0.96783–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:fcc-a1)

Names (3): _corpus: _corpus:phase:li-pb:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:fcc  
_tdb: _tdb:LiPb-16Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): FCC_A1, type code %A, sha256 `d85ea4e948ee390a…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : LI PB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1927-191-1239](https://doi.org/10.1515/ijmr-1927-191-1239) J. Czochralski, E. Rassow, Z. Metallkd 19 (1927) 111e112.  
_cited as the source of values for this phase_

## HCP_A3 (Li–Pb)

- Id: `phase:li-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:hcp-a3)

Names (2): _corpus: _corpus:phase:li-pb:hcp-a3  
_tdb: _tdb:LiPb-16Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): HCP_A3, type code %A, sha256 `d85ea4e948ee390a…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : LI PB : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase_

## LI3PB_D03 (Li–Pb)

- Id: `phase:li-pb:li3pb-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stoichiometry: Li 0.7500, Pb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–931.06 K, x(Pb) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:li3pb-d03)

Names (3): _corpus: _corpus:phase:li-pb:li3pb-d03  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:Li3Pb  
_tdb: _tdb:LiPb-16Zho.tdb:LI3PB_D03  


### TDB models of LI3PB_D03 (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): LI3PB_D03, type code %, sha256 `d85ea4e948ee390a…`

~~~~text
54: PHASE LI3PB_D03 % 2 3 1 !
55: CONST LI3PB_D03 : LI : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_
- [doi:10.1021/j150536a022](https://doi.org/10.1021/j150536a022) Allan Zalkin, William J. Ramsey, Intermetallic Compounds between Lithium and Lead. I. The Structures of Li\<sub>3\</sub>Pb and Li\<sub>7\</sub>Pb\<sub>2\</sub>., J. Phys. Chem. 60, 234-236 (1956).  
_cited as the source of values for this phase_

## LI4PB (Li–Pb)

- Id: `phase:li-pb:li4pb`; status `assigned`
- Structure: Li17Pb4 · cF420 · F-43m (216); type `st:li17pb4-cf420`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Li 0.8000, Pb 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–921.06 K, x(Pb) 0.2–0.2
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:li4pb)

Names (3): _corpus: _corpus:phase:li-pb:li4pb  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:Li4Pb  
_tdb: _tdb:LiPb-16Zho.tdb:LI4PB  


### TDB models of LI4PB (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): LI4PB, type code %, sha256 `d85ea4e948ee390a…`

~~~~text
44: PHASE LI4PB % 2 4 1 !
45: CONST LI4PB : LI : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_
- [doi:10.1021/j150564a013](https://doi.org/10.1021/j150564a013) A. Zalkin, W. J. Ramsey, Intermetallic Compounds between Lithium and Lead. IV. The Crystal Structure of Li\<sub>22\</sub> Pb\<sub>5\</sub>, J. Phys. Chem. 62, 689-693 (1958).  
_cited as the source of values for this phase_

## LI5PB2 (Li–Pb)

- Id: `phase:li-pb:li5pb2`; status `assigned`
- Structure: Li8Pb3 · hR11 · R-3m (166); type `st:li8pb3-hr11`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Li 0.7143, Pb 0.2857
- Stability: stable in 1 of 1 calculated diagram(s): 300–915.02 K, x(Pb) 0.28571–0.28571
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:li5pb2)

Names (3): _corpus: _corpus:phase:li-pb:li5pb2  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:Li5Pb2  
_tdb: _tdb:LiPb-16Zho.tdb:LI5PB2  


### TDB models of LI5PB2 (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): LI5PB2, type code %, sha256 `d85ea4e948ee390a…`

~~~~text
59: PHASE LI5PB2 % 2 5 2 !
60: CONST LI5PB2 : LI : PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_

## LI7PB2 (Li–Pb)

- Id: `phase:li-pb:li7pb2`; status `assigned`
- Structure: Li7Pb2 · hP9 · P-3m1 (164); type `st:li7pb2-hp9`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–998.56 K, x(Pb) 0.20816–0.22222
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:li7pb2)

Names (3): _corpus: _corpus:phase:li-pb:li7pb2  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:Li7Pb2  
_tdb: _tdb:LiPb-16Zho.tdb:LI7PB2  


### TDB models of LI7PB2 (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): LI7PB2, type code %, sha256 `d85ea4e948ee390a…`

~~~~text
49: PHASE LI7PB2 % 2 7 2 !
50: CONST LI7PB2 : LI : LI PB% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_
- [doi:10.1021/j150536a022](https://doi.org/10.1021/j150536a022) Allan Zalkin, William J. Ramsey, Intermetallic Compounds between Lithium and Lead. I. The Structures of Li\<sub>3\</sub>Pb and Li\<sub>7\</sub>Pb\<sub>2\</sub>., J. Phys. Chem. 60, 234-236 (1956).  
_cited as the source of values for this phase_

## LIPB_ALPHA (Li–Pb)

- Id: `phase:li-pb:lipb-alpha`; status `assigned`
- Structure: alpha-LiPb · hR2 · R-3m (166); type `st:alpha-lipb-hr2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–487.34 K, x(Pb) 0.47841–0.5114
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:lipb-alpha)

Names (3): _corpus: _corpus:phase:li-pb:lipb-alpha  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:αLiPb  
_tdb: _tdb:LiPb-16Zho.tdb:LIPB_ALPHA  


### TDB models of LIPB_ALPHA (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): LIPB_ALPHA, type code %, sha256 `d85ea4e948ee390a…`

~~~~text
64: PHASE LIPB_ALPHA % 2 1 1 !
65: CONST LIPB_ALPHA : LI% PB : LI PB% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_
- [doi:10.1021/j150556a034](https://doi.org/10.1021/j150556a034) Allan Zalkin, William J. Ramsey, Intermetallic Compounds between Lithium and Lead. III. The β\<sub>1\</sub>-β Transition in LiPb, J. Phys. Chem. 61, 1413-1415 (1957).  
_cited as the source of values for this phase_

## LIPB_B2 (Li–Pb)

- Id: `phase:li-pb:lipb-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in LiPb-16Zho.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 459.01–755.28 K, x(Pb) 0.46061–0.50937
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:lipb-b2)

Names (3): _corpus: _corpus:phase:li-pb:lipb-b2  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:βLiPb  
_tdb: _tdb:LiPb-16Zho.tdb:LIPB_B2  


### TDB models of LIPB_B2 (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): LIPB_B2, type code %, sha256 `d85ea4e948ee390a…`

~~~~text
69: PHASE LIPB_B2 % 2 1 1 !
70: CONST LIPB_B2 : LI% PB : LI PB% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_
- [doi:10.1021/j150556a034](https://doi.org/10.1021/j150556a034) Allan Zalkin, William J. Ramsey, Intermetallic Compounds between Lithium and Lead. III. The β\<sub>1\</sub>-β Transition in LiPb, J. Phys. Chem. 61, 1413-1415 (1957).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1927-191-1239](https://doi.org/10.1515/ijmr-1927-191-1239) J. Czochralski, E. Rassow, Z. Metallkd 19 (1927) 111e112.  
_cited as the source of values for this phase_

## LIQUID (Li–Pb)

- Id: `phase:li-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 449.29–2500 K, x(Pb) 0–1
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-pb:liquid)

Names (3): _corpus: _corpus:phase:li-pb:liquid  
_paper: _paper:10.1016/j.jnucmat.2016.04.061:liq.  
_tdb: _tdb:LiPb-16Zho.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LiPb-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb): LIQUID, type code %, sha256 `d85ea4e948ee390a…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : LI LI4PB PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.193400038](https://doi.org/10.1002/bbpc.193400038) G. Grube, H. Klaiber, Z. Elektrochem. 40 (1934) 745e754.  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1927-191-1239](https://doi.org/10.1515/ijmr-1927-191-1239) J. Czochralski, E. Rassow, Z. Metallkd 19 (1927) 111e112.  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
