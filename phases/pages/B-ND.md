# B–Nd phases

> B–Nd system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-ND.html · Markdown: https://data.orchid-project.org/phases/pages/B-ND.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-ND) · [full JSON](https://data.orchid-project.org/phases/systems/B-ND.json) · [B–Nd system page](https://data.orchid-project.org/systems/B-ND.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-ND.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Nd system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-nd-b-beta-rhombo); _phase:b-nd:b-beta-rhombo_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–2349 K, x(B) 1–1 | 0 | 4 |
| [BCC_A2](#phase-b-nd-bcc-a2); _phase:b-nd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1127.59–3999.83 K, x(B) 0–0.00049 | 0 | 4 |
| [DHCP](#phase-b-nd-dhcp-a3); _phase:b-nd:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1283 K, x(B) 0–0 | 0 | 4 |
| [FCC_A1](#phase-b-nd-fcc-a1); _phase:b-nd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-b-nd-hcp-a3); _phase:b-nd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-b-nd-liquid); _phase:b-nd:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1250.83–4000 K, x(B) 0–1 | 2 | 4 |
| [ND2B5](#phase-b-nd-nd2b5); _phase:b-nd:nd2b5_ | Pr2B5 · mC56 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–2382.42 K, x(B) 0.71429–0.71429 | 0 | 4 |
| [NDB4_D1E](#phase-b-nd-ndb4-d1e); _phase:b-nd:ndb4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2630.77 K, x(B) 0.8–0.8 | 0 | 4 |
| [NDB6_D21](#phase-b-nd-ndb6-d21); _phase:b-nd:ndb6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2899.14 K, x(B) 0.85714–0.91413 | 2 | 4 |
| [NDB66](#phase-b-nd-ndb66); _phase:b-nd:ndb66_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–2422.97 K, x(B) 0.98–0.98507 | 10 | 4 |

## BETA_RHOMBO_B (B–Nd)

- Id: `phase:b-nd:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NdB-16Zho-corrected.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NdB-19Che.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NdB-95Hal-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NdB-98Che.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2349 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:b-beta-rhombo)

Names (5): _corpus: _corpus:phase:b-nd:b-beta-rhombo  
_tdb: _tdb:NdB-16Zho-corrected.tdb:BETA_RHOMBO_B, tdb:NdB-19Che.tdb:BETA_RHOMBO_B, tdb:NdB-95Hal-LB.tdb:BETA_RHOMBO_B, tdb:NdB-98Che.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): BETA_RHOMBO_B, type code %, sha256 `cae81a496f38b11b…`

~~~~text
51: PHASE BETA_RHOMBO_B % 1 1 !
52: CONST BETA_RHOMBO_B : B : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): BETA_RHOMBO_B, type code %, sha256 `dff8ac7c4ad64e6c…`

~~~~text
48: PHASE BETA_RHOMBO_B % 1 1 !
49: CONST BETA_RHOMBO_B : B : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `a14f51e14303dba1…`

~~~~text
51: PHASE BETA_RHOMBO_B % 1 1 !
52: CONST BETA_RHOMBO_B : B : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): BETA_RHOMBO_B, type code %, sha256 `502e0edcb7d117b4…`

~~~~text
49: PHASE BETA_RHOMBO_B % 1 1 !
50: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## BCC_A2 (B–Nd)

- Id: `phase:b-nd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1127.59–3999.83 K, x(B) 0–0.00049
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:bcc-a2)

Names (5): _corpus: _corpus:phase:b-nd:bcc-a2  
_tdb: _tdb:NdB-16Zho-corrected.tdb:BCC_A2, tdb:NdB-19Che.tdb:BCC_A2, tdb:NdB-95Hal-LB.tdb:BCC_A2, tdb:NdB-98Che.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): BCC_A2, type code %B, sha256 `cae81a496f38b11b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : B ND : VA : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): BCC_A2, type code %B, sha256 `dff8ac7c4ad64e6c…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : B ND : VA : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): BCC_A2, type code %B, sha256 `a14f51e14303dba1…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : ND : B, VA : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): BCC_A2, type code %B, sha256 `502e0edcb7d117b4…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : ND : B, VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## DHCP (B–Nd)

- Id: `phase:b-nd:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Nd 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1283 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:dhcp-a3)

Names (5): _corpus: _corpus:phase:b-nd:dhcp-a3  
_tdb: _tdb:NdB-16Zho-corrected.tdb:DHCP, tdb:NdB-19Che.tdb:DHCP, tdb:NdB-95Hal-LB.tdb:DHCP, tdb:NdB-98Che.tdb:DHCP  


### TDB models of DHCP (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): DHCP, type code %, sha256 `cae81a496f38b11b…`

~~~~text
46: PHASE DHCP % 1 1 !
47: CONST DHCP : ND : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): DHCP, type code %, sha256 `dff8ac7c4ad64e6c…`

~~~~text
43: PHASE DHCP % 1 1 !
44: CONST DHCP : ND : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): DHCP, type code %, sha256 `a14f51e14303dba1…`

~~~~text
46: PHASE DHCP % 1 1 !
47: CONST DHCP : ND : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): DHCP, type code %, sha256 `502e0edcb7d117b4…`

~~~~text
44: PHASE DHCP % 1 1 !
45: CONST DHCP : ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## FCC_A1 (B–Nd)

- Id: `phase:b-nd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:fcc-a1)

Names (5): _corpus: _corpus:phase:b-nd:fcc-a1  
_tdb: _tdb:NdB-16Zho-corrected.tdb:FCC_A1, tdb:NdB-19Che.tdb:FCC_A1, tdb:NdB-95Hal-LB.tdb:FCC_A1, tdb:NdB-98Che.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): FCC_A1, type code %A, sha256 `cae81a496f38b11b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : B ND : VA : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): FCC_A1, type code %A, sha256 `dff8ac7c4ad64e6c…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : B ND : VA : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): FCC_A1, type code %A, sha256 `a14f51e14303dba1…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : ND : B, VA : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): FCC_A1, type code %A, sha256 `502e0edcb7d117b4…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : ND : B, VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## HCP_A3 (B–Nd)

- Id: `phase:b-nd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:hcp-a3)

Names (5): _corpus: _corpus:phase:b-nd:hcp-a3  
_tdb: _tdb:NdB-16Zho-corrected.tdb:HCP_A3, tdb:NdB-19Che.tdb:HCP_A3, tdb:NdB-95Hal-LB.tdb:HCP_A3, tdb:NdB-98Che.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): HCP_A3, type code %A, sha256 `cae81a496f38b11b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : B ND : VA : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): HCP_A3, type code %A, sha256 `dff8ac7c4ad64e6c…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : B ND : VA : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): HCP_A3, type code %A, sha256 `a14f51e14303dba1…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : ND : B, VA : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): HCP_A3, type code %A, sha256 `502e0edcb7d117b4…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : ND : B, VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## LIQUID (B–Nd)

- Id: `phase:b-nd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1250.83–4000 K, x(B) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:liquid)

Names (6): _corpus: _corpus:phase:b-nd:liquid  
_paper: _paper:10.1007/bf02664851:L  
_tdb: _tdb:NdB-16Zho-corrected.tdb:LIQUID, tdb:NdB-19Che.tdb:LIQUID, tdb:NdB-95Hal-LB.tdb:LIQUID, tdb:NdB-98Che.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): LIQUID, type code %, sha256 `cae81a496f38b11b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : B ND : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): LIQUID, type code %, sha256 `dff8ac7c4ad64e6c…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : B ND : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): LIQUID, type code %, sha256 `a14f51e14303dba1…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : B ND : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): LIQUID, type code %, sha256 `502e0edcb7d117b4…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## ND2B5 (B–Nd)

- Id: `phase:b-nd:nd2b5`; status `assigned`
- Structure: Pr2B5 · mC56 · C2/c (15); type `st:pr2b5-mc56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_15_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.7143, Nd 0.2857
- Stability: stable in 4 of 4 calculated diagram(s): 300–2382.42 K, x(B) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:nd2b5)

Names (5): _corpus: _corpus:phase:b-nd:nd2b5  
_tdb: _tdb:NdB-16Zho-corrected.tdb:ND2B5, tdb:NdB-19Che.tdb:ND2B5, tdb:NdB-95Hal-LB.tdb:ND2B5, tdb:NdB-98Che.tdb:ND2B5  


### TDB models of ND2B5 (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): ND2B5, type code %, sha256 `cae81a496f38b11b…`

~~~~text
56: PHASE ND2B5 % 2 2 5 !
57: CONST ND2B5 : ND : B : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): ND2B5, type code %, sha256 `dff8ac7c4ad64e6c…`

~~~~text
53: PHASE ND2B5 % 2 2 5 !
54: CONST ND2B5 : ND : B : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): ND2B5, type code %, sha256 `a14f51e14303dba1…`

~~~~text
56: PHASE ND2B5 % 2 2 5 !
57: CONST ND2B5 : ND : B : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): ND2B5, type code %, sha256 `502e0edcb7d117b4…`

~~~~text
54: PHASE ND2B5 % 2 2 5 !
55: CONST ND2B5 : ND : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## NDB4_D1E (B–Nd)

- Id: `phase:b-nd:ndb4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacku and oqmd-19849, space group 127
- Stoichiometry: B 0.8000, Nd 0.2000
- Stability: stable in 4 of 4 calculated diagram(s): 300–2630.77 K, x(B) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:ndb4-d1e)

Names (7): _corpus: _corpus:phase:b-nd:ndb4-d1e  
_mp: _mp:mp-aaaaacku  
_oqmd: _oqmd:oqmd-19849  
_tdb: _tdb:NdB-16Zho-corrected.tdb:NDB4_D1E, tdb:NdB-19Che.tdb:NDB4_D1E, tdb:NdB-95Hal-LB.tdb:NDB4_D1E, tdb:NdB-98Che.tdb:NDB4_D1E  


### TDB models of NDB4_D1E (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): NDB4_D1E, type code %, sha256 `cae81a496f38b11b…`

~~~~text
61: PHASE NDB4_D1E % 2 1 4 !
62: CONST NDB4_D1E : ND : B : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): NDB4_D1E, type code %, sha256 `dff8ac7c4ad64e6c…`

~~~~text
58: PHASE NDB4_D1E % 2 1 4 !
59: CONST NDB4_D1E : ND : B : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): NDB4_D1E, type code %, sha256 `a14f51e14303dba1…`

~~~~text
61: PHASE NDB4_D1E % 2 1 4 !
62: CONST NDB4_D1E : ND : B : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): NDB4_D1E, type code %, sha256 `502e0edcb7d117b4…`

~~~~text
59: PHASE NDB4_D1E % 2 1 4 !
60: CONST NDB4_D1E : ND : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## NDB6_D21 (B–Nd)

- Id: `phase:b-nd:ndb6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2899.14 K, x(B) 0.85714–0.91413
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:ndb6-d21)

Names (6): _corpus: _corpus:phase:b-nd:ndb6-d21  
_paper: _paper:10.1007/bf02664851:NdB6  
_tdb: _tdb:NdB-16Zho-corrected.tdb:NDB6_D21, tdb:NdB-19Che.tdb:NDB6_D21, tdb:NdB-95Hal-LB.tdb:NDB6_D21, tdb:NdB-98Che.tdb:NDB6_D21  


### TDB models of NDB6_D21 (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): NDB6_D21, type code %, sha256 `cae81a496f38b11b…`

~~~~text
66: PHASE NDB6_D21 % 2 1 6 !
67: CONST NDB6_D21 : ND : B : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): NDB6_D21, type code %, sha256 `dff8ac7c4ad64e6c…`

~~~~text
63: PHASE NDB6_D21 % 2 1 6 !
64: CONST NDB6_D21 : B ND% : B : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): NDB6_D21, type code %, sha256 `a14f51e14303dba1…`

~~~~text
66: PHASE NDB6_D21 % 2 1 6 !
67: CONST NDB6_D21 : ND : B : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): NDB6_D21, type code %, sha256 `502e0edcb7d117b4…`

~~~~text
64: PHASE NDB6_D21 % 2 1 6 !
65: CONST NDB6_D21 : ND : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_

## NDB66 (B–Nd)

- Id: `phase:b-nd:ndb66`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; no_structure_token
- Candidate (sgte_mmc2): YB66 · cF1936 · Fm-3c (226) — Hallstedt 2025 mmc2 row for NDB66: NdB66
- Candidate (tdb_comment): YB66 · cF1936 · Fm-3c — NdB-16Zho-corrected.tdb: 'Prototype YB66 (cF1936, Fm-3c)'
- Candidate (tdb_comment): YB66 · cF1936 · Fm-3c — NdB-19Che.tdb: 'Prototype YB66 (cF1936, Fm-3c)'
- Candidate (tdb_comment): YB66 · cF1936 · Fm-3c — NdB-95Hal-LB.tdb: 'Prototype YB66 (cF1936, Fm-3c)'
- Candidate (tdb_comment): YB66 · cF1936 · Fm-3c — NdB-98Che.tdb: 'Prototype YB66 (cF1936, Fm-3c)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–2422.97 K, x(B) 0.98–0.98507
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-nd:ndb66)

Names (6): _corpus: _corpus:phase:b-nd:ndb66  
_paper: _paper:10.1007/bf02664851:NdB66  
_tdb: _tdb:NdB-16Zho-corrected.tdb:NDB66, tdb:NdB-19Che.tdb:NDB66, tdb:NdB-95Hal-LB.tdb:NDB66, tdb:NdB-98Che.tdb:NDB66  


### TDB models of NDB66 (4): PHASE and CONSTITUENT statements as written

[NdB-16Zho-corrected.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-16Zho-corrected.tdb): NDB66, type code %, sha256 `cae81a496f38b11b…`

~~~~text
71: PHASE NDB66 % 2 0.02 0.98 !
72: CONST NDB66 : ND : B : !
~~~~

[NdB-19Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-19Che.tdb): NDB66, type code %, sha256 `dff8ac7c4ad64e6c…`

~~~~text
68: PHASE NDB66 % 2 1 66 !
69: CONST NDB66 : ND : B : !
~~~~

[NdB-95Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-95Hal-LB.tdb): NDB66, type code %, sha256 `a14f51e14303dba1…`

~~~~text
71: PHASE NDB66 % 2 1 66 !
72: CONST NDB66 : ND : B : !
~~~~

[NdB-98Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdB-98Che.tdb): NDB66, type code %, sha256 `502e0edcb7d117b4…`

~~~~text
69: PHASE NDB66 % 2 1 66 !
70: CONST NDB66 : ND : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02664851](https://doi.org/10.1007/BF02664851) B. Hallemans, P. Wollants, J.R. Roos, J. Phase Equilib., 16, 137-49(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101627](https://doi.org/10.1016/j.calphad.2019.101627) T.L. Chen, J. Wang, C.P. Guo, C.R. Li, Z.M. Du, G.H. Rao, H.Y. Zhou, Calphad, 66, 101627(2019).  
_assessment that models this phase_
- [doi:10.1021/j150611a015](https://doi.org/10.1021/j150611a015) E. K. Storms, Phase relationship, vaporization, and thermodynamic properties of neodymium hexaboride, J. Phys. Chem. 85, 1536-1540 (1981).  
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
