# Cd–Sb phases

> Cd–Sb system: 8 phases (tier A 5, tier C 2, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-SB.html · Markdown: https://data.orchid-project.org/phases/pages/CD-SB.md

8 phases (tier A 5, tier C 2, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-SB) · [full JSON](https://data.orchid-project.org/phases/systems/CD-SB.json) · [Cd–Sb system page](https://data.orchid-project.org/systems/CD-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Sb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-cd-sb-a7-rhombohedral); _phase:cd-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 12 | 3 |
| [BCC_A2](#phase-cd-sb-bcc-a2); _phase:cd-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [CD3SB2](#phase-cd-sb-cd3sb2); _phase:cd-sb:cd3sb2_ | Cd3Sb2 · cP15 · P432 (207) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CD4SB3](#phase-cd-sb-cd4sb3); _phase:cd-sb:cd4sb3_ | Sb17Zn23 · hR22 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 1 | 1 |
| [CDSB_BE](#phase-cd-sb-cdsb-be); _phase:cd-sb:cdsb-be_ | CdSb · B_e · oP16 · Pbca (61) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–732.22 K, x(Sb) 0.5–0.51008 | 32 | 3 |
| [FCC_A1](#phase-cd-sb-fcc-a1); _phase:cd-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-cd-sb-hcp-a3); _phase:cd-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–594.22 K, x(Sb) 0–0.0052 | 13 | 3 |
| [LIQUID](#phase-cd-sb-liquid); _phase:cd-sb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 567.25–2500 K, x(Sb) 0–1 | 36 | 3 |

## RHOMBOHEDRAL_A7 (Cd–Sb)

- Id: `phase:cd-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:a7-rhombohedral)

Names (7): _corpus: _corpus:phase:cd-sb:a7-rhombohedral, corpus:phase:cd-sb:rhombohedral-a7  
_paper: _paper:10.1016/0364-5916(93)90012-z:(Sb), paper:10.1016/j.calphad.2009.08.006:(Sb)  
_tdb: _tdb:CdSb-09Liu.tdb:RHOMBOHEDRAL_A7, tdb:CdSb-93Zab.tdb:RHOMBOHEDRAL_A7, tdb:CdSb-97Zab-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `0fbb59f521a43ca0…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[CdSb-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-93Zab.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9701b309eb2aee30…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[CdSb-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-97Zab-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `37511ef3a5b64682…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(93)90012-Z](https://doi.org/10.1016/0364-5916%2893%2990012-Z) L.A. Zabdyr, Calphad, 17, 125-32(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(93)90005-v](https://doi.org/10.1016/0364-5916%2893%2990005-v) L.A. Zabdyr, CALPHAD 17 (3) (1993) 269.  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(03)00157-2](https://doi.org/10.1016/s0966-9795%2803%2900157-2) M.C. Record, V. Izard, M. Bulanova, J.C. Tedenac, Phase transformations in the Zn–Cd–Sb system, Intermetallics 11, 1189-1194 (2003).  
_cited as the source of values for this phase_

## BCC_A2 (Cd–Sb)

- Id: `phase:cd-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:bcc-a2)

Names (4): _corpus: _corpus:phase:cd-sb:bcc-a2  
_tdb: _tdb:CdSb-09Liu.tdb:BCC_A2, tdb:CdSb-93Zab.tdb:BCC_A2, tdb:CdSb-97Zab-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): BCC_A2, type code %B, sha256 `0fbb59f521a43ca0…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CD SB : VA : !
~~~~

[CdSb-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-93Zab.tdb): BCC_A2, type code %B, sha256 `9701b309eb2aee30…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CD SB : VA : !
~~~~

[CdSb-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-97Zab-LB.tdb): BCC_A2, type code %B, sha256 `37511ef3a5b64682…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CD SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90012-Z](https://doi.org/10.1016/0364-5916%2893%2990012-Z) L.A. Zabdyr, Calphad, 17, 125-32(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_

## CD3SB2 (Cd–Sb)

- Id: `phase:cd-sb:cd3sb2`; status `assigned`
- Structure: Cd3Sb2 · cP15 · P432 (207); type `st:cd3sb2-cp15`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.6000, Sb 0.4000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:cd3sb2)

Names (2): _corpus: _corpus:phase:cd-sb:cd3sb2  
_tdb: _tdb:CdSb-09Liu.tdb:CD3SB2  


### TDB models of CD3SB2 (1): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): CD3SB2, type code %, sha256 `0fbb59f521a43ca0…`

~~~~text
54: PHASE CD3SB2 %  2 3 2 !
55: CONST CD3SB2 : CD : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase_

## CD4SB3 (Cd–Sb)

- Id: `phase:cd-sb:cd4sb3`; status `assigned`
- Structure: Sb17Zn23 · hR22 · R-3c (167); type `st:sb17zn23-hr22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:cd4sb3)

Names (3): _corpus: _corpus:phase:cd-sb:cd4sb3  
_paper: _paper:10.1016/0364-5916(93)90012-z:Cd4Sb3  
_tdb: _tdb:CdSb-09Liu.tdb:CD4SB3  


### TDB models of CD4SB3 (1): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): CD4SB3, type code %, sha256 `0fbb59f521a43ca0…`

~~~~text
59: PHASE CD4SB3 %  2 4 3 !
60: CONST CD4SB3 : CD% VA : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(93)90012-z](https://doi.org/10.1016/0364-5916%2893%2990012-z) Leszek A. Zabdyr, Equilibrium diagram and thermodynamic properties of cadmium — antimony binary alloys. Critical assessment, Calphad 17, 125-132 (1993).  
_reports values for this phase_

## CDSB_BE (Cd–Sb)

- Id: `phase:cd-sb:cdsb-be`; status `assigned`
- Structure: CdSb · B_e · oP16 · Pbca (61); type `st:b-e-cdsb-op16`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–732.22 K, x(Sb) 0.5–0.51008
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:cdsb-be)

Names (6): _corpus: _corpus:phase:cd-sb:cdsb-be  
_paper: _paper:10.1016/0364-5916(93)90012-z:CdSb, paper:10.1016/j.calphad.2009.08.006:ω-CdSb  
_tdb: _tdb:CdSb-09Liu.tdb:CDSB_BE, tdb:CdSb-93Zab.tdb:CDSB_BE, tdb:CdSb-97Zab-LB.tdb:CDSB_BE  


### TDB models of CDSB_BE (3): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): CDSB_BE, type code %, sha256 `0fbb59f521a43ca0…`

~~~~text
48: PHASE CDSB_BE %  2 1 1 !
49: CONST CDSB_BE : CD% VA : SB : !
~~~~

[CdSb-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-93Zab.tdb): CDSB_BE, type code %, sha256 `9701b309eb2aee30…`

~~~~text
47: PHASE CDSB_BE %  2 1 1 !
48: CONST CDSB_BE : CD : SB : !
~~~~

[CdSb-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-97Zab-LB.tdb): CDSB_BE, type code %, sha256 `37511ef3a5b64682…`

~~~~text
49: PHASE CDSB_BE %  2 1 1 !
50: CONST CDSB_BE : CD : SB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(93)90012-Z](https://doi.org/10.1016/0364-5916%2893%2990012-Z) L.A. Zabdyr, Calphad, 17, 125-32(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_
- [doi:10.1016/s0966-9795(03)00157-2](https://doi.org/10.1016/s0966-9795%2803%2900157-2) M.C. Record, V. Izard, M. Bulanova, J.C. Tedenac, Phase transformations in the Zn–Cd–Sb system, Intermetallics 11, 1189-1194 (2003).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(93)90005-v](https://doi.org/10.1016/0364-5916%2893%2990005-v) L.A. Zabdyr, CALPHAD 17 (3) (1993) 269.  
_cited as the source of values for this phase_

## FCC_A1 (Cd–Sb)

- Id: `phase:cd-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:fcc-a1)

Names (4): _corpus: _corpus:phase:cd-sb:fcc-a1  
_tdb: _tdb:CdSb-09Liu.tdb:FCC_A1, tdb:CdSb-93Zab.tdb:FCC_A1, tdb:CdSb-97Zab-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): FCC_A1, type code %A, sha256 `0fbb59f521a43ca0…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CD SB : VA : !
~~~~

[CdSb-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-93Zab.tdb): FCC_A1, type code %A, sha256 `9701b309eb2aee30…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CD SB : VA : !
~~~~

[CdSb-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-97Zab-LB.tdb): FCC_A1, type code %A, sha256 `37511ef3a5b64682…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CD SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90012-Z](https://doi.org/10.1016/0364-5916%2893%2990012-Z) L.A. Zabdyr, Calphad, 17, 125-32(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_

## HCP_A3 (Cd–Sb)

- Id: `phase:cd-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–594.22 K, x(Sb) 0–0.0052
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:hcp-a3)

Names (6): _corpus: _corpus:phase:cd-sb:hcp-a3  
_paper: _paper:10.1016/0364-5916(93)90012-z:(Cd), paper:10.1016/j.calphad.2009.08.006:(Cd)  
_tdb: _tdb:CdSb-09Liu.tdb:HCP_A3, tdb:CdSb-93Zab.tdb:HCP_A3, tdb:CdSb-97Zab-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): HCP_A3, type code %A, sha256 `0fbb59f521a43ca0…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CD% SB : VA : !
~~~~

[CdSb-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-93Zab.tdb): HCP_A3, type code %A, sha256 `9701b309eb2aee30…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CD% SB : VA : !
~~~~

[CdSb-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-97Zab-LB.tdb): HCP_A3, type code %A, sha256 `37511ef3a5b64682…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CD% SB : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0364-5916(93)90012-Z](https://doi.org/10.1016/0364-5916%2893%2990012-Z) L.A. Zabdyr, Calphad, 17, 125-32(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(93)90005-v](https://doi.org/10.1016/0364-5916%2893%2990005-v) L.A. Zabdyr, CALPHAD 17 (3) (1993) 269.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2006.04.051](https://doi.org/10.1016/j.jallcom.2006.04.051) Fouzia Adjadj, El-djemai Belbacha, Malek Bouharkat, Differential calorimetric analysis of the binary system Sb–Zn, Journal of Alloys and Compounds 430, 85-91 (2007).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(03)00157-2](https://doi.org/10.1016/s0966-9795%2803%2900157-2) M.C. Record, V. Izard, M. Bulanova, J.C. Tedenac, Phase transformations in the Zn–Cd–Sb system, Intermetallics 11, 1189-1194 (2003).  
_cited as the source of values for this phase_

## LIQUID (Cd–Sb)

- Id: `phase:cd-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 567.25–2500 K, x(Sb) 0–1
- Literature: 36 values (36 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sb:liquid)

Names (7): _corpus: _corpus:phase:cd-sb:liquid  
_paper: _paper:10.1016/0364-5916(93)90012-z:L, paper:10.1016/0364-5916(93)90012-z:liquid, paper:10.1016/j.calphad.2009.08.006:L  
_tdb: _tdb:CdSb-09Liu.tdb:LIQUID, tdb:CdSb-93Zab.tdb:LIQUID, tdb:CdSb-97Zab-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CdSb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-09Liu.tdb): LIQUID, type code %, sha256 `0fbb59f521a43ca0…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CD SB : !
~~~~

[CdSb-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-93Zab.tdb): LIQUID, type code %, sha256 `9701b309eb2aee30…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CD SB : !
~~~~

[CdSb-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSb-97Zab-LB.tdb): LIQUID, type code %, sha256 `37511ef3a5b64682…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CD SB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0364-5916(93)90012-Z](https://doi.org/10.1016/0364-5916%2893%2990012-Z) L.A. Zabdyr, Calphad, 17, 125-32(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_
- [doi:10.1016/s0966-9795(03)00157-2](https://doi.org/10.1016/s0966-9795%2803%2900157-2) M.C. Record, V. Izard, M. Bulanova, J.C. Tedenac, Phase transformations in the Zn–Cd–Sb system, Intermetallics 11, 1189-1194 (2003).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(93)90005-v](https://doi.org/10.1016/0364-5916%2893%2990005-v) L.A. Zabdyr, CALPHAD 17 (3) (1993) 269.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2006.04.051](https://doi.org/10.1016/j.jallcom.2006.04.051) Fouzia Adjadj, El-djemai Belbacha, Malek Bouharkat, Differential calorimetric analysis of the binary system Sb–Zn, Journal of Alloys and Compounds 430, 85-91 (2007).  
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
