# Cr–Pt phases

> Cr–Pt system: 7 phases (tier A 4, liquid 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-PT.html · Markdown: https://data.orchid-project.org/phases/pages/CR-PT.md

7 phases (tier A 4, liquid 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-PT) · [full JSON](https://data.orchid-project.org/phases/systems/CR-PT.json) · [Cr–Pt system page](https://data.orchid-project.org/systems/CR-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Pt system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-pt-bcc-a2); _phase:cr-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2202.68 K, x(Pt) 0–0.0706 | 2 | 3 |
| [CR3PT_A15](#phase-cr-pt-cr3pt-a15); _phase:cr-pt:cr3pt-a15_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1904.94 K, x(Pt) 0.16476–0.25 | 7 | 3 |
| [CRPT3_L12](#phase-cr-pt-crpt3-l12); _phase:cr-pt:crpt3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1421.05 K, x(Pt) 0.37505–0.84228 | 0 | 1 |
| [FCC_4SL](#phase-cr-pt-fcc-4sl); _phase:cr-pt:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2050 K, x(Pt) 0.28697–1 | 4 | 1 |
| [FCC_A1](#phase-cr-pt-fcc-a1); _phase:cr-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2062.24 K, x(Pt) 0.28028–1 | 8 | 4 |
| [HCP_A3](#phase-cr-pt-hcp-a3); _phase:cr-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-cr-pt-liquid); _phase:cr-pt:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1821.34–4000 K, x(Pt) 0–1 | 8 | 3 |

## BCC_A2 (Cr–Pt)

- Id: `phase:cr-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2202.68 K, x(Pt) 0–0.0706
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-pt:bcc-a2)

Names (6): _corpus: _corpus:phase:cr-pt:bcc-a2  
_paper: _paper:10.1016/j.msea.2008.10.059:Cr bcc, paper:10.1016/j.msea.2008.10.059:bcc  
_tdb: _tdb:CrPt-01Oik.tdb:BCC_A2, tdb:CrPt-09Pre.tdb:BCC_A2, tdb:CrPt-98Spe-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CrPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-01Oik.tdb): BCC_A2, type code %B, sha256 `e67e8c07062774a0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR% PT : VA : !
~~~~

[CrPt-09Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-09Pre.tdb): BCC_A2, type code %B, sha256 `812667dfc13e00cf…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : CR% PT : VA : !
~~~~

[CrPt-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-98Spe-LB.tdb): BCC_A2, type code %B, sha256 `82886ea74acc67cb…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% PT : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2008.10.059](https://doi.org/10.1016/j.msea.2008.10.059) Johannes Preußner, Sara Prins, Rainer Völkl, Zi-Kui Liu, Uwe Glatzel, Determination of phases in the system chromium–platinum (Cr–Pt) and thermodynamic calculations, Materials Science and Engineering: A 510-511, 322-327 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
_assessment that models this phase_

## CR3PT_A15 (Cr–Pt)

- Id: `phase:cr-pt:cr3pt-a15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_A15; stoichiometry_contradicts_A15:CrPt-98Spe-LB.tdb
- Candidate (literature_printed): Cr3Si · cP8 — printed with a label mapped to this phase
- Candidate (name_token): Cr3Si · A15 · cP8 · Pm-3n (223) — Strukturbericht/word 'A15' in the TDB name
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for CR3PT_A15: Cr4Pt
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — CrPt-01Oik.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — CrPt-09Pre.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — CrPt-98Spe-LB.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Stability: stable in 3 of 3 calculated diagram(s): 300–1904.94 K, x(Pt) 0.16476–0.25
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-pt:cr3pt-a15)

Names (6): _corpus: _corpus:phase:cr-pt:cr3pt-a15  
_paper: _paper:10.1016/j.msea.2008.10.059:A15, paper:10.1016/j.msea.2008.10.059:A15 Cr3Pt  
_tdb: _tdb:CrPt-01Oik.tdb:CR3PT_A15, tdb:CrPt-09Pre.tdb:CR3PT_A15, tdb:CrPt-98Spe-LB.tdb:CR3PT_A15  


### TDB models of CR3PT_A15 (3): PHASE and CONSTITUENT statements as written

[CrPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-01Oik.tdb): CR3PT_A15, type code %, sha256 `e67e8c07062774a0…`

~~~~text
41: PHASE CR3PT_A15 % 2 3 1 !
42: CONST CR3PT_A15 : CR% PT : CR PT% : !
~~~~

[CrPt-09Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-09Pre.tdb): CR3PT_A15, type code %, sha256 `812667dfc13e00cf…`

~~~~text
57: PHASE CR3PT_A15 % 2 3 1 !
58: CONST CR3PT_A15 : CR% PT : CR PT% : !
~~~~

[CrPt-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-98Spe-LB.tdb): CR3PT_A15, type code %, sha256 `82886ea74acc67cb…`

~~~~text
45: PHASE CR3PT_A15 % 2 4 1 !
46: CONST CR3PT_A15 : CR : PT : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2008.10.059](https://doi.org/10.1016/j.msea.2008.10.059) Johannes Preußner, Sara Prins, Rainer Völkl, Zi-Kui Liu, Uwe Glatzel, Determination of phases in the system chromium–platinum (Cr–Pt) and thermodynamic calculations, Materials Science and Engineering: A 510-511, 322-327 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
_assessment that models this phase_

## CRPT3_L12 (Cr–Pt)

- Id: `phase:cr-pt:crpt3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1421.05 K, x(Pt) 0.37505–0.84228
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-pt:crpt3-l12)

Names (2): _corpus: _corpus:phase:cr-pt:crpt3-l12  
_tdb: _tdb:CrPt-98Spe-LB.tdb:CRPT3_L12  


### TDB models of CRPT3_L12 (1): PHASE and CONSTITUENT statements as written

[CrPt-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-98Spe-LB.tdb): CRPT3_L12, type code %, sha256 `82886ea74acc67cb…`

~~~~text
50: PHASE CRPT3_L12 % 1 1 !
51: CONST CRPT3_L12 : CR PT : !
~~~~

## FCC_4SL (Cr–Pt)

- Id: `phase:cr-pt:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:CrPt-09Pre.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; sgte_mmc2_rows_disagree; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Pm-3m (221) — on-hull MP CrPt3 at x(PT)=0.7500
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Cr1 Pt3 at x(PT)=0.7500
- Candidate (literature_printed): AuCu · tP4 — printed with a label mapped to this phase
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (sgte_mmc2): AuCu · L1_0 · tP4 · P4/mmm (123) — Hallstedt 2025 mmc2 row for FCC_4SL: AlTi, AuCu, CoPt, CrPt, FeNi, FePt, MnNi
- Candidate (sgte_mmc2): AuCu3 · L1_2 · cP4 · Pm-3m (221) — Hallstedt 2025 mmc2 row for FCC_4SL: Ag3Mg, Al3Li, AlNi3, AlPt3, Au3Cu, AuCu3, Co3Pt, CoPt3, Cr3Pt, CrPt3, Cu3Pt, FeNi3, Fe3Pt, FePt3, MnNi3, Ni3Pt, NiPt3, Ni3Si (beta-1)
- Candidate (tdb_comment): AuCu · L1_0 · tP2, P4/mmm — CrPt-09Pre.tdb: 'Prototype AuCu (L1_0, tP2, P4/mmm) and AuCu3 (L1_2, cP4, Pm-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–2050 K, x(Pt) 0.28697–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-pt:fcc-4sl)

Names (5): _corpus: _corpus:phase:cr-pt:fcc-4sl  
_paper: _paper:10.1016/j.msea.2008.10.059:L10 CrPt, paper:10.1016/j.msea.2008.10.059:L12 Cr3Pt, paper:10.1016/j.msea.2008.10.059:L12 CrPt3  
_tdb: _tdb:CrPt-09Pre.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[CrPt-09Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-09Pre.tdb): FCC_4SL, type code %AY, sha256 `812667dfc13e00cf…`

~~~~text
42: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
43: CONST FCC_4SL:F : CR% PT : CR PT% : CR PT% : CR PT% : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2008.10.059](https://doi.org/10.1016/j.msea.2008.10.059) Johannes Preußner, Sara Prins, Rainer Völkl, Zi-Kui Liu, Uwe Glatzel, Determination of phases in the system chromium–platinum (Cr–Pt) and thermodynamic calculations, Materials Science and Engineering: A 510-511, 322-327 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cr–Pt)

- Id: `phase:cr-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2062.24 K, x(Pt) 0.28028–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-pt:fcc-a1)

Names (7): _corpus: _corpus:phase:cr-pt:fcc-a1  
_paper: _paper:10.1016/j.msea.2008.10.059:Pt fcc, paper:10.1016/j.msea.2008.10.059:fcc  
_tdb: _tdb:CrPt-01Oik.tdb:FCC_A1, tdb:CrPt-09Pre.tdb:A1_FCC, tdb:CrPt-09Pre.tdb:FCC_A1, tdb:CrPt-98Spe-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CrPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-01Oik.tdb): FCC_A1, type code %A, sha256 `e67e8c07062774a0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR PT% : VA : !
~~~~

[CrPt-09Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-09Pre.tdb): A1_FCC, type code %A, sha256 `812667dfc13e00cf…`

~~~~text
37: PHASE A1_FCC %A 2 1 1 !
38: CONST A1_FCC : CR PT% : VA : !
~~~~

[CrPt-09Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-09Pre.tdb): FCC_A1, type code %A, sha256 `812667dfc13e00cf…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CR PT% : VA : !
~~~~

[CrPt-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-98Spe-LB.tdb): FCC_A1, type code %A, sha256 `82886ea74acc67cb…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR PT% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2008.10.059](https://doi.org/10.1016/j.msea.2008.10.059) Johannes Preußner, Sara Prins, Rainer Völkl, Zi-Kui Liu, Uwe Glatzel, Determination of phases in the system chromium–platinum (Cr–Pt) and thermodynamic calculations, Materials Science and Engineering: A 510-511, 322-327 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
_assessment that models this phase_

## HCP_A3 (Cr–Pt)

- Id: `phase:cr-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-pt:hcp-a3)

Names (4): _corpus: _corpus:phase:cr-pt:hcp-a3  
_tdb: _tdb:CrPt-01Oik.tdb:HCP_A3, tdb:CrPt-09Pre.tdb:HCP_A3, tdb:CrPt-98Spe-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CrPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-01Oik.tdb): HCP_A3, type code %A, sha256 `e67e8c07062774a0…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR PT : VA : !
~~~~

[CrPt-09Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-09Pre.tdb): HCP_A3, type code %A, sha256 `812667dfc13e00cf…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : CR PT : VA : !
~~~~

[CrPt-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-98Spe-LB.tdb): HCP_A3, type code %A, sha256 `82886ea74acc67cb…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CR PT : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2008.10.059](https://doi.org/10.1016/j.msea.2008.10.059) Johannes Preußner, Sara Prins, Rainer Völkl, Zi-Kui Liu, Uwe Glatzel, Determination of phases in the system chromium–platinum (Cr–Pt) and thermodynamic calculations, Materials Science and Engineering: A 510-511, 322-327 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
_assessment that models this phase_

## LIQUID (Cr–Pt)

- Id: `phase:cr-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1821.34–4000 K, x(Pt) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-pt:liquid)

Names (5): _corpus: _corpus:phase:cr-pt:liquid  
_paper: _paper:10.1016/j.msea.2008.10.059:L  
_tdb: _tdb:CrPt-01Oik.tdb:LIQUID, tdb:CrPt-09Pre.tdb:LIQUID, tdb:CrPt-98Spe-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CrPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-01Oik.tdb): LIQUID, type code %, sha256 `e67e8c07062774a0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR PT : !
~~~~

[CrPt-09Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-09Pre.tdb): LIQUID, type code %, sha256 `812667dfc13e00cf…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CR PT : !
~~~~

[CrPt-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrPt-98Spe-LB.tdb): LIQUID, type code %, sha256 `82886ea74acc67cb…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR PT : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2008.10.059](https://doi.org/10.1016/j.msea.2008.10.059) Johannes Preußner, Sara Prins, Rainer Völkl, Zi-Kui Liu, Uwe Glatzel, Determination of phases in the system chromium–platinum (Cr–Pt) and thermodynamic calculations, Materials Science and Engineering: A 510-511, 322-327 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
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
