# Sb–Tm phases

> Sb–Tm system: 10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SB-TM.html · Markdown: https://data.orchid-project.org/phases/pages/SB-TM.md

10 phases (tier A 5, tier C 1, liquid 1, needs_review 3); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SB-TM) · [full JSON](https://data.orchid-project.org/phases/systems/SB-TM.json) · [Sb–Tm system page](https://data.orchid-project.org/systems/SB-TM.html) · [Markdown](https://data.orchid-project.org/phases/pages/SB-TM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sb–Tm system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-sb-tm-a7-rhombohedral); _phase:sb-tm:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.23 K, x(Tm) 0–0 | 2 | 1 |
| [BCC_A2](#phase-sb-tm-bcc-a2); _phase:sb-tm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-sb-tm-fcc-a1); _phase:sb-tm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-sb-tm-hcp-a3); _phase:sb-tm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.68 K, x(Tm) 0.98767–1 | 2 | 1 |
| [LIQUID](#phase-sb-tm-liquid); _phase:sb-tm:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 900.19–2500 K, x(Tm) 0–1 | 10 | 1 |
| [SB2TM](#phase-sb-tm-sb2tm); _phase:sb-tm:sb2tm_ | HoSb2 · oC6 · C222 (21) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–912.24 K, x(Tm) 0.33333–0.33333 | 6 | 1 |
| [SB3TM5_ALPHA](#phase-sb-tm-sb3tm5-alpha); _phase:sb-tm:sb3tm5-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1893.73 K, x(Tm) 0.625–0.625 | 6 | 1 |
| [SB3TM5_BETA](#phase-sb-tm-sb3tm5-beta); _phase:sb-tm:sb3tm5-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1893.73–1913.65 K, x(Tm) 0.625–0.625 | 4 | 1 |
| [SBTM_B1](#phase-sb-tm-sbtm-b1); _phase:sb-tm:sbtm-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2053.94 K, x(Tm) 0.5–0.5 | 10 | 1 |
| [SBTM_BETA](#phase-sb-tm-sbtm-beta); _phase:sb-tm:sbtm-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2053.94–2293.16 K, x(Tm) 0.5–0.5 | 4 | 1 |

## RHOMBOHEDRAL_A7 (Sb–Tm)

- Id: `phase:sb-tm:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.23 K, x(Tm) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:sb-tm:a7-rhombohedral, corpus:phase:sb-tm:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2011.08.001:(Sb)  
_tdb: _tdb:SbTm-11Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6a2d363b98bbe70b…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Sb–Tm)

- Id: `phase:sb-tm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:bcc-a2)

Names (2): _corpus: _corpus:phase:sb-tm:bcc-a2  
_tdb: _tdb:SbTm-11Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): BCC_A2, type code %B, sha256 `6a2d363b98bbe70b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : SB TM : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase_

## FCC_A1 (Sb–Tm)

- Id: `phase:sb-tm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:fcc-a1)

Names (2): _corpus: _corpus:phase:sb-tm:fcc-a1  
_tdb: _tdb:SbTm-11Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): FCC_A1, type code %A, sha256 `6a2d363b98bbe70b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SB TM : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase_

## HCP_A3 (Sb–Tm)

- Id: `phase:sb-tm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.68 K, x(Tm) 0.98767–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:hcp-a3)

Names (3): _corpus: _corpus:phase:sb-tm:hcp-a3  
_paper: _paper:10.1016/j.calphad.2011.08.001:(Tm)  
_tdb: _tdb:SbTm-11Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): HCP_A3, type code %A, sha256 `6a2d363b98bbe70b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SB TM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Sb–Tm)

- Id: `phase:sb-tm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 900.19–2500 K, x(Tm) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:liquid)

Names (3): _corpus: _corpus:phase:sb-tm:liquid  
_paper: _paper:10.1016/j.calphad.2011.08.001:L  
_tdb: _tdb:SbTm-11Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): LIQUID, type code %, sha256 `6a2d363b98bbe70b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SB TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_

## SB2TM (Sb–Tm)

- Id: `phase:sb-tm:sb2tm`; status `assigned`
- Structure: HoSb2 · oC6 · C222 (21); type `st:hosb2-oc6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sb 0.6667, Tm 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–912.24 K, x(Tm) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:sb2tm)

Names (3): _corpus: _corpus:phase:sb-tm:sb2tm  
_paper: _paper:10.1016/j.calphad.2011.08.001:Sb2Tm  
_tdb: _tdb:SbTm-11Wan.tdb:SB2TM  


### TDB models of SB2TM (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): SB2TM, type code %, sha256 `6a2d363b98bbe70b…`

~~~~text
45: PHASE SB2TM % 2 2 1 !
46: CONST SB2TM : SB : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## SB3TM5_ALPHA (Sb–Tm)

- Id: `phase:sb-tm:sb3tm5-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P6_3/mcm (193) — on-hull MP Tm5Sb3 at x(TM)=0.6250
- Candidate (dft_oqmd): P63/mcm (193) — on-hull OQMD Sb3 Tm5 at x(TM)=0.6250
- Candidate (sgte_mmc2): Bi3Y5 · oP32 · Pnma (62) — Hallstedt 2025 mmc2 row for SB3TM5_ALPHA: Sb3Tm5-alpha
- Candidate (tdb_comment): Bi3Y5 · oP32 · Pnma — SbTm-11Wan.tdb: 'Prototype Bi3Y5 (oP32, Pnma)'
- Stoichiometry: Sb 0.3750, Tm 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1893.73 K, x(Tm) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:sb3tm5-alpha)

Names (3): _corpus: _corpus:phase:sb-tm:sb3tm5-alpha  
_paper: _paper:10.1016/j.calphad.2011.08.001:αSb3Tm5  
_tdb: _tdb:SbTm-11Wan.tdb:SB3TM5_ALPHA  


### TDB models of SB3TM5_ALPHA (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): SB3TM5_ALPHA, type code %, sha256 `6a2d363b98bbe70b…`

~~~~text
60: PHASE SB3TM5_ALPHA % 2 3 5 !
61: CONST SB3TM5_ALPHA : SB : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## SB3TM5_BETA (Sb–Tm)

- Id: `phase:sb-tm:sb3tm5-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P6_3/mcm (193) — on-hull MP Tm5Sb3 at x(TM)=0.6250
- Candidate (dft_oqmd): P63/mcm (193) — on-hull OQMD Sb3 Tm5 at x(TM)=0.6250
- Candidate (sgte_mmc2): Sb3Yb5 · oP32 · Pnma (62) — Hallstedt 2025 mmc2 row for SB3TM5_BETA: Sb3Tm5-beta
- Candidate (tdb_comment): Sb3Yb5 · oP32 · Pnma — SbTm-11Wan.tdb: 'Prototype Sb3Yb5 (oP32, Pnma)'
- Stoichiometry: Sb 0.3750, Tm 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1893.73–1913.65 K, x(Tm) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:sb3tm5-beta)

Names (3): _corpus: _corpus:phase:sb-tm:sb3tm5-beta  
_paper: _paper:10.1016/j.calphad.2011.08.001:βSb3Tm5  
_tdb: _tdb:SbTm-11Wan.tdb:SB3TM5_BETA  


### TDB models of SB3TM5_BETA (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): SB3TM5_BETA, type code %, sha256 `6a2d363b98bbe70b…`

~~~~text
65: PHASE SB3TM5_BETA % 2 3 5 !
66: CONST SB3TM5_BETA : SB : TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_

## SBTM_B1 (Sb–Tm)

- Id: `phase:sb-tm:sbtm-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.5000, Tm 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2053.94 K, x(Tm) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:sbtm-b1)

Names (3): _corpus: _corpus:phase:sb-tm:sbtm-b1  
_paper: _paper:10.1016/j.calphad.2011.08.001:αSbTm  
_tdb: _tdb:SbTm-11Wan.tdb:SBTM_B1  


### TDB models of SBTM_B1 (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): SBTM_B1, type code %, sha256 `6a2d363b98bbe70b…`

~~~~text
50: PHASE SBTM_B1 % 2 1 1 !
51: CONST SBTM_B1 : SB : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## SBTM_BETA (Sb–Tm)

- Id: `phase:sb-tm:sbtm-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Fm-3m (225) — on-hull MP TmSb at x(TM)=0.5000
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Sb1 Tm1 at x(TM)=0.5000
- Candidate (sgte_mmc2): (SbTm) — Hallstedt 2025 mmc2 row for SBTM_BETA: SbTm-beta
- Stoichiometry: Sb 0.5000, Tm 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 2053.94–2293.16 K, x(Tm) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-tm:sbtm-beta)

Names (3): _corpus: _corpus:phase:sb-tm:sbtm-beta  
_paper: _paper:10.1016/j.calphad.2011.08.001:βSbTm  
_tdb: _tdb:SbTm-11Wan.tdb:SBTM_BETA  


### TDB models of SBTM_BETA (1): PHASE and CONSTITUENT statements as written

[SbTm-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb): SBTM_BETA, type code %, sha256 `6a2d363b98bbe70b…`

~~~~text
55: PHASE SBTM_BETA % 2 1 1 !
56: CONST SBTM_BETA : SB : TM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_

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
