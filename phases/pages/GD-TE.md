# Gd–Te phases

> Gd–Te system: 11 phases (tier A 5, tier C 5, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-TE.html · Markdown: https://data.orchid-project.org/phases/pages/GD-TE.md

11 phases (tier A 5, tier C 5, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-TE) · [full JSON](https://data.orchid-project.org/phases/systems/GD-TE.json) · [Gd–Te system page](https://data.orchid-project.org/systems/GD-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–Te system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-gd-te-a8-hexagonal); _phase:gd-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.8 K, x(Te) 1–1 | 0 | 1 |
| [BCC_A2](#phase-gd-te-bcc-a2); _phase:gd-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1508.16–1588.11 K, x(Te) 0–0 | 0 | 1 |
| [FCC_A1](#phase-gd-te-fcc-a1); _phase:gd-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GD2TE3](#phase-gd-te-gd2te3); _phase:gd-te:gd2te3_ | Th2S3 · oP20 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1541.18 K, x(Te) 0.57178–0.6 | 3 | 1 |
| [GD2TE5](#phase-gd-te-gd2te5); _phase:gd-te:gd2te5_ | Nd2Te5 · oC28 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1191.68 K, x(Te) 0.71429–0.71429 | 3 | 1 |
| [GD4TE7](#phase-gd-te-gd4te7); _phase:gd-te:gd4te7_ | UAs2 · tP6 · P4/nmm (129) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1445.07 K, x(Te) 0.63636–0.63636 | 1 | 1 |
| [GDTE_B1](#phase-gd-te-gdte-b1); _phase:gd-te:gdte-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2100.31 K, x(Te) 0.5–0.5 | 0 | 1 |
| [GDTE2](#phase-gd-te-gdte2); _phase:gd-te:gdte2_ | Fe2As · tP6 · P4/nmm (129) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1271.99 K, x(Te) 0.66667–0.66667 | 2 | 1 |
| [GDTE3](#phase-gd-te-gdte3); _phase:gd-te:gdte3_ | NdTe3 · oC16 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1104.88 K, x(Te) 0.75–0.75 | 3 | 1 |
| [HCP_A3](#phase-gd-te-hcp-a3); _phase:gd-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1508.16 K, x(Te) 0–0 | 0 | 1 |
| [LIQUID](#phase-gd-te-liquid); _phase:gd-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 718.55–2500 K, x(Te) 0–1 | 1 | 1 |

## HEXAGONAL_A8 (Gd–Te)

- Id: `phase:gd-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.8 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:a8-hexagonal)

Names (2): _corpus: _corpus:phase:gd-te:a8-hexagonal  
_tdb: _tdb:GdTe-23Cui.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): HEXAGONAL_A8, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
50: PHASE HEXAGONAL_A8 % 1 1 !
51: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## BCC_A2 (Gd–Te)

- Id: `phase:gd-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1508.16–1588.11 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:bcc-a2)

Names (2): _corpus: _corpus:phase:gd-te:bcc-a2  
_tdb: _tdb:GdTe-23Cui.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): BCC_A2, type code %B, sha256 `4411ddc5ee70cff7…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : GD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## FCC_A1 (Gd–Te)

- Id: `phase:gd-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:fcc-a1)

Names (2): _corpus: _corpus:phase:gd-te:fcc-a1  
_tdb: _tdb:GdTe-23Cui.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): FCC_A1, type code %A, sha256 `4411ddc5ee70cff7…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : GD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## GD2TE3 (Gd–Te)

- Id: `phase:gd-te:gd2te3`; status `assigned`
- Structure: Th2S3 · oP20 · Pnma (62); type `st:th2s3-op20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1541.18 K, x(Te) 0.57178–0.6
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:gd2te3)

Names (3): _corpus: _corpus:phase:gd-te:gd2te3  
_paper: _paper:10.1007/s11669-023-01051-1:Gd2Te3  
_tdb: _tdb:GdTe-23Cui.tdb:GD2TE3  


### TDB models of GD2TE3 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): GD2TE3, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
60: PHASE GD2TE3 % 3 0.4 0.5714 0.0286 !
61: CONST GD2TE3 : GD : TE : GD TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1107/s0021889887087065](https://doi.org/10.1107/s0021889887087065) J. S. Swinnea, H. Steinfink, L. R. Danielson, Crystal chemistry and thermoelectric properties of Gd\<sub>2\</sub>Te\<sub>3\</sub>, J Appl Crystallogr 20, 102-104 (1987).  
_cited as the source of values for this phase_

## GD2TE5 (Gd–Te)

- Id: `phase:gd-te:gd2te5`; status `assigned`
- Structure: Nd2Te5 · oC28 · Cmcm (63); type `st:nd2te5-oc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.2857, Te 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–1191.68 K, x(Te) 0.71429–0.71429
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:gd2te5)

Names (3): _corpus: _corpus:phase:gd-te:gd2te5  
_paper: _paper:10.1007/s11669-023-01051-1:Gd2Te5  
_tdb: _tdb:GdTe-23Cui.tdb:GD2TE5  


### TDB models of GD2TE5 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): GD2TE5, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
75: PHASE GD2TE5 % 2 2 5 !
76: CONST GD2TE5 : GD : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## GD4TE7 (Gd–Te)

- Id: `phase:gd-te:gd4te7`; status `assigned`
- Structure: UAs2 · tP6 · P4/nmm (129); type `st:uas2-tp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.3636, Te 0.6364
- Stability: stable in 1 of 1 calculated diagram(s): 300–1445.07 K, x(Te) 0.63636–0.63636
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:gd4te7)

Names (3): _corpus: _corpus:phase:gd-te:gd4te7  
_paper: _paper:10.1007/s11669-023-01051-1:Gd4Te7  
_tdb: _tdb:GdTe-23Cui.tdb:GD4TE7  


### TDB models of GD4TE7 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): GD4TE7, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
65: PHASE GD4TE7 % 2 4 7 !
66: CONST GD4TE7 : GD : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## GDTE_B1 (Gd–Te)

- Id: `phase:gd-te:gdte-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2100.31 K, x(Te) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:gdte-b1)

Names (2): _corpus: _corpus:phase:gd-te:gdte-b1  
_tdb: _tdb:GdTe-23Cui.tdb:GDTE_B1  


### TDB models of GDTE_B1 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): GDTE_B1, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
55: PHASE GDTE_B1 % 2 1 1 !
56: CONST GDTE_B1 : GD : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## GDTE2 (Gd–Te)

- Id: `phase:gd-te:gdte2`; status `assigned`
- Structure: Fe2As · tP6 · P4/nmm (129); type `st:fe2as-tp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.3333, Te 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1271.99 K, x(Te) 0.66667–0.66667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:gdte2)

Names (3): _corpus: _corpus:phase:gd-te:gdte2  
_paper: _paper:10.1007/s11669-023-01051-1:GdTe2  
_tdb: _tdb:GdTe-23Cui.tdb:GDTE2  


### TDB models of GDTE2 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): GDTE2, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
70: PHASE GDTE2 % 2 1 2 !
71: CONST GDTE2 : GD : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1246/bcsj.45.1239](https://doi.org/10.1246/bcsj.45.1239) Koichi Niihara, Toetsu Shishido, Seishi Yajima, The Nonstoichiometry of Gadolinium Ditelluride, Bulletin of the Chemical Society of Japan 45, 1239-1240 (1972).  
_cited as the source of values for this phase_

## GDTE3 (Gd–Te)

- Id: `phase:gd-te:gdte3`; status `assigned`
- Structure: NdTe3 · oC16 · Cmcm (63); type `st:ndte3-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.2500, Te 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1104.88 K, x(Te) 0.75–0.75
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:gdte3)

Names (3): _corpus: _corpus:phase:gd-te:gdte3  
_paper: _paper:10.1007/s11669-023-01051-1:GdTe3  
_tdb: _tdb:GdTe-23Cui.tdb:GDTE3  


### TDB models of GDTE3 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): GDTE3, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
80: PHASE GDTE3 % 2 1 3 !
81: CONST GDTE3 : GD : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Gd–Te)

- Id: `phase:gd-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1508.16 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:hcp-a3)

Names (2): _corpus: _corpus:phase:gd-te:hcp-a3  
_tdb: _tdb:GdTe-23Cui.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): HCP_A3, type code %A, sha256 `4411ddc5ee70cff7…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : GD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## LIQUID (Gd–Te)

- Id: `phase:gd-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 718.55–2500 K, x(Te) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-te:liquid)

Names (3): _corpus: _corpus:phase:gd-te:liquid  
_paper: _paper:10.1007/s11669-023-01051-1:liquid  
_tdb: _tdb:GdTe-23Cui.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GdTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdTe-23Cui.tdb): LIQUID, type code %, sha256 `4411ddc5ee70cff7…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : GD GDTE TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

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
