# Cu–Ge phases

> Cu–Ge system: 9 phases (tier A 5, liquid 1, needs_review 3); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-GE.html · Markdown: https://data.orchid-project.org/phases/pages/CU-GE.md

9 phases (tier A 5, liquid 1, needs_review 3); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-GE) · [full JSON](https://data.orchid-project.org/phases/systems/CU-GE.json) · [Cu–Ge system page](https://data.orchid-project.org/systems/CU-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Ge system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-cu-ge-a4-diamond); _phase:cu-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1 | 4 | 2 |
| [BCC_A2](#phase-cu-ge-bcc-a2); _phase:cu-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [CU3GE](#phase-cu-ge-cu3ge); _phase:cu-ge:cu3ge_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1017.11 K, x(Ge) 0.25–0.25 | 0 | 1 |
| [CU3GE_D018](#phase-cu-ge-cu3ge-d018); _phase:cu-ge:cu3ge-d018_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 822.46–1022.22 K, x(Ge) 0.235–0.235 | 10 | 1 |
| [CU3GE_D03](#phase-cu-ge-cu3ge-d03); _phase:cu-ge:cu3ge-d03_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 884.79–970.46 K, x(Ge) 0.265–0.265 | 8 | 1 |
| [CU3GE_D0A](#phase-cu-ge-cu3ge-d0a); _phase:cu-ge:cu3ge-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–947.61 K, x(Ge) 0.25–0.25 | 6 | 1 |
| [FCC_A1](#phase-cu-ge-fcc-a1); _phase:cu-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1360.77 K, x(Ge) 0–0.11795 | 2 | 2 |
| [HCP_A3](#phase-cu-ge-hcp-a3); _phase:cu-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1097.53 K, x(Ge) 0.09624–0.1857 | 6 | 2 |
| [LIQUID](#phase-cu-ge-liquid); _phase:cu-ge:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 908.02–2500 K, x(Ge) 0–1 | 10 | 2 |

## DIAMOND_A4 (Cu–Ge)

- Id: `phase:cu-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:a4-diamond)

Names (5): _corpus: _corpus:phase:cu-ge:a4-diamond, corpus:phase:cu-ge:diamond-a4  
_paper: _paper:10.1016/j.jallcom.2010.05.077:(Ge)  
_tdb: _tdb:CuGe-10Wan.tdb:DIAMOND_A4, tdb:CuGe-Rand.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): DIAMOND_A4, type code %, sha256 `af99f4c24e73a88e…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : GE : !
~~~~

[CuGe-Rand.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-Rand.tdb): DIAMOND_A4, type code %, sha256 `39799a146bda7651…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874979](https://doi.org/10.1007/bf02874979) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase diagrams 7 (1986) 28.  
_cited as the source of values for this phase_

## BCC_A2 (Cu–Ge)

- Id: `phase:cu-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-ge:bcc-a2  
_tdb: _tdb:CuGe-10Wan.tdb:BCC_A2, tdb:CuGe-Rand.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): BCC_A2, type code %B, sha256 `af99f4c24e73a88e…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CU GE : VA : !
~~~~

[CuGe-Rand.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-Rand.tdb): BCC_A2, type code %B, sha256 `39799a146bda7651…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CU GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase_

## CU3GE (Cu–Ge)

- Id: `phase:cu-ge:cu3ge`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Pmmn (59) — on-hull MP Cu3Ge at x(GE)=0.2500
- Candidate (dft_oqmd): Pmmn (59) — on-hull OQMD Cu3 Ge1 at x(GE)=0.2500
- Candidate (tdb_comment): BiF3 · cF16 · Fm-3m — CuGe-Rand.tdb: 'Prototype BiF3 (cF16, Fm-3m), theta (high-T), also Cu5Ge2'
- Candidate (tdb_comment): Na3As · hP8 · P6_3/mmc — CuGe-Rand.tdb: 'Prototype Na3As (hP8, P6_3/mmc), epsilon (high-T)'
- Candidate (tdb_comment): beta-Cu3Ti · oP8 · Pmmn — CuGe-Rand.tdb: 'Prototype beta-Cu3Ti (oP8, Pmmn), eta (low-T)'
- Stoichiometry: Cu 0.7500, Ge 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1017.11 K, x(Ge) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:cu3ge)

Names (2): _corpus: _corpus:phase:cu-ge:cu3ge  
_tdb: _tdb:CuGe-Rand.tdb:CU3GE  


### TDB models of CU3GE (1): PHASE and CONSTITUENT statements as written

[CuGe-Rand.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-Rand.tdb): CU3GE, type code %, sha256 `39799a146bda7651…`

~~~~text
51: PHASE CU3GE % 2 3 1 !
52: CONST CU3GE : CU : GE : !
~~~~

## CU3GE_D018 (Cu–Ge)

- Id: `phase:cu-ge:cu3ge-d018`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D0_18; stoichiometry_contradicts_D0_18:CuGe-10Wan.tdb
- Candidate (literature_printed): Na3As · hP8 — printed with a label mapped to this phase
- Candidate (name_token): Na3As · D0_18 · hP8 · P6_3/mmc (194) — Strukturbericht/word 'D018' in the TDB name
- Candidate (sgte_mmc2): Na3As · D0_18 · hP8 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CU3GE_D018: Cu3Ge (epsilon, high-T)
- Candidate (tdb_comment): Na3As · hP8 · P6_3/mmc — CuGe-10Wan.tdb: 'Prototype Na3As (hP8, P6_3/mmc), epsilon (high-T)'
- Stoichiometry: Cu 0.7650, Ge 0.2350
- Stability: stable in 1 of 1 calculated diagram(s): 822.46–1022.22 K, x(Ge) 0.235–0.235
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:cu3ge-d018)

Names (3): _corpus: _corpus:phase:cu-ge:cu3ge-d018  
_paper: _paper:10.1016/j.jallcom.2010.05.077:ε-Cu0.765Ge0.235  
_tdb: _tdb:CuGe-10Wan.tdb:CU3GE_D018  


### TDB models of CU3GE_D018 (1): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): CU3GE_D018, type code %, sha256 `af99f4c24e73a88e…`

~~~~text
45: PHASE CU3GE_D018 % 2 0.765 0.235 !
46: CONST CU3GE_D018 : CU : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874979](https://doi.org/10.1007/bf02874979) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase diagrams 7 (1986) 28.  
_cited as the source of values for this phase_

## CU3GE_D03 (Cu–Ge)

- Id: `phase:cu-ge:cu3ge-d03`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D0_3; stoichiometry_contradicts_D0_3:CuGe-10Wan.tdb
- Candidate (literature_printed): BiF3 · cF16 — printed with a label mapped to this phase
- Candidate (name_token): BiF3 · D0_3 · cF16 · Fm-3m (225) — Strukturbericht/word 'D03' in the TDB name
- Candidate (sgte_mmc2): BiF3 · D0_3 · cF16 · Fm-3m (225) — Hallstedt 2025 mmc2 row for CU3GE_D03: Cu3Ge (theta, high-T, Cu5Ge2)
- Candidate (tdb_comment): BiF3 · cF16 · Fm-3m — CuGe-10Wan.tdb: 'Prototype BiF3 (cF16, Fm-3m), theta (high-T), also Cu5Ge2'
- Stoichiometry: Cu 0.7350, Ge 0.2650
- Stability: stable in 1 of 1 calculated diagram(s): 884.79–970.46 K, x(Ge) 0.265–0.265
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:cu3ge-d03)

Names (3): _corpus: _corpus:phase:cu-ge:cu3ge-d03  
_paper: _paper:10.1016/j.jallcom.2010.05.077:θ-Cu0.735Ge0.265  
_tdb: _tdb:CuGe-10Wan.tdb:CU3GE_D03  


### TDB models of CU3GE_D03 (1): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): CU3GE_D03, type code %, sha256 `af99f4c24e73a88e…`

~~~~text
55: PHASE CU3GE_D03 % 2 0.735 0.265 !
56: CONST CU3GE_D03 : CU : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874979](https://doi.org/10.1007/bf02874979) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase diagrams 7 (1986) 28.  
_cited as the source of values for this phase_

## CU3GE_D0A (Cu–Ge)

- Id: `phase:cu-ge:cu3ge-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.7500, Ge 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–947.61 K, x(Ge) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:cu3ge-d0a)

Names (3): _corpus: _corpus:phase:cu-ge:cu3ge-d0a  
_paper: _paper:10.1016/j.jallcom.2010.05.077:η-Cu0.75Ge0.25  
_tdb: _tdb:CuGe-10Wan.tdb:CU3GE_D0A  


### TDB models of CU3GE_D0A (1): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): CU3GE_D0A, type code %, sha256 `af99f4c24e73a88e…`

~~~~text
50: PHASE CU3GE_D0A % 2 0.75 0.25 !
51: CONST CU3GE_D0A : CU : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874979](https://doi.org/10.1007/bf02874979) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase diagrams 7 (1986) 28.  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Ge)

- Id: `phase:cu-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1360.77 K, x(Ge) 0–0.11795
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-ge:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2010.05.077:fcc  
_tdb: _tdb:CuGe-10Wan.tdb:FCC_A1, tdb:CuGe-Rand.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): FCC_A1, type code %A, sha256 `af99f4c24e73a88e…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CU% GE : VA : !
~~~~

[CuGe-Rand.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-Rand.tdb): FCC_A1, type code %A, sha256 `39799a146bda7651…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CU% GE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874979](https://doi.org/10.1007/bf02874979) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase diagrams 7 (1986) 28.  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Ge)

- Id: `phase:cu-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1097.53 K, x(Ge) 0.09624–0.1857
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-ge:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2010.05.077:hcp  
_tdb: _tdb:CuGe-10Wan.tdb:HCP_A3, tdb:CuGe-Rand.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): HCP_A3, type code %A, sha256 `af99f4c24e73a88e…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CU GE : VA : !
~~~~

[CuGe-Rand.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-Rand.tdb): HCP_A3, type code %A, sha256 `39799a146bda7651…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CU GE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874979](https://doi.org/10.1007/bf02874979) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase diagrams 7 (1986) 28.  
_cited as the source of values for this phase_

## LIQUID (Cu–Ge)

- Id: `phase:cu-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 908.02–2500 K, x(Ge) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ge:liquid)

Names (4): _corpus: _corpus:phase:cu-ge:liquid  
_paper: _paper:10.1016/j.jallcom.2010.05.077:L  
_tdb: _tdb:CuGe-10Wan.tdb:LIQUID, tdb:CuGe-Rand.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuGe-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-10Wan.tdb): LIQUID, type code %, sha256 `af99f4c24e73a88e…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CU GE : !
~~~~

[CuGe-Rand.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGe-Rand.tdb): LIQUID, type code %, sha256 `39799a146bda7651…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CU GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.05.077](https://doi.org/10.1016/j.jallcom.2010.05.077) J. Wang, S. Jin, C. Leinenbach, A. Jacot, Thermodynamic assessment of the Cu–Ge binary system, Journal of Alloys and Compounds 504, 159-165 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02874979](https://doi.org/10.1007/bf02874979) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase diagrams 7 (1986) 28.  
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
