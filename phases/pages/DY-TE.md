# Dy–Te phases

> Dy–Te system: 10 phases (tier A 4, tier C 5, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/DY-TE.html · Markdown: https://data.orchid-project.org/phases/pages/DY-TE.md

10 phases (tier A 4, tier C 5, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=DY-TE) · [full JSON](https://data.orchid-project.org/phases/systems/DY-TE.json) · [Dy–Te system page](https://data.orchid-project.org/systems/DY-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/DY-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Dy–Te system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-dy-te-a8-hexagonal); _phase:dy-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.63 K, x(Te) 1–1 | 0 | 1 |
| [BCC_A2](#phase-dy-te-bcc-a2); _phase:dy-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1654.15–1695.11 K, x(Te) 0–0 | 0 | 1 |
| [DY2TE](#phase-dy-te-dy2te); _phase:dy-te:dy2te_ | Sc2Te · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1244.52 K, x(Te) 0.33333–0.33333 | 5 | 1 |
| [DY2TE3](#phase-dy-te-dy2te3); _phase:dy-te:dy2te3_ | Sc2S3 · oF80 · Fddd (70) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1837.11 K, x(Te) 0.5714–0.59849 | 3 | 1 |
| [DY4TE11](#phase-dy-te-dy4te11); _phase:dy-te:dy4te11_ | NdTe3 · oC16 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1129.71 K, x(Te) 0.73333–0.73333 | 4 | 1 |
| [DY4TE7](#phase-dy-te-dy4te7); _phase:dy-te:dy4te7_ | UAs2 · tP6 · P4/nmm (129) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1495.37 K, x(Te) 0.63636–0.63636 | 2 | 1 |
| [DY4TE9](#phase-dy-te-dy4te9); _phase:dy-te:dy4te9_ | Nd2Te5 · oC28 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1193.33 K, x(Te) 0.69231–0.69231 | 3 | 1 |
| [DYTE_B1](#phase-dy-te-dyte-b1); _phase:dy-te:dyte-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2113.43 K, x(Te) 0.5–0.5 | 0 | 1 |
| [HCP_A3](#phase-dy-te-hcp-a3); _phase:dy-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1654.15 K, x(Te) 0–0 | 0 | 1 |
| [LIQUID](#phase-dy-te-liquid); _phase:dy-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 722.63–2500 K, x(Te) 0–1 | 1 | 1 |

## HEXAGONAL_A8 (Dy–Te)

- Id: `phase:dy-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.63 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:a8-hexagonal)

Names (2): _corpus: _corpus:phase:dy-te:a8-hexagonal  
_tdb: _tdb:DyTe-23Cui.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): HEXAGONAL_A8, type code %, sha256 `a26fd7267d158c68…`

~~~~text
44: PHASE HEXAGONAL_A8 % 1 1 !
45: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## BCC_A2 (Dy–Te)

- Id: `phase:dy-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1654.15–1695.11 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:bcc-a2)

Names (2): _corpus: _corpus:phase:dy-te:bcc-a2  
_tdb: _tdb:DyTe-23Cui.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): BCC_A2, type code %B, sha256 `a26fd7267d158c68…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## DY2TE (Dy–Te)

- Id: `phase:dy-te:dy2te`; status `assigned`
- Structure: Sc2Te · oP36 · Pnma (62); type `st:sc2te-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Dy 0.6667, Te 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1244.52 K, x(Te) 0.33333–0.33333
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:dy2te)

Names (3): _corpus: _corpus:phase:dy-te:dy2te  
_paper: _paper:10.1007/s11669-023-01051-1:Dy2Te  
_tdb: _tdb:DyTe-23Cui.tdb:DY2TE  


### TDB models of DY2TE (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): DY2TE, type code %, sha256 `a26fd7267d158c68…`

~~~~text
49: PHASE DY2TE % 2 2 1 !
50: CONST DY2TE : DY : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## DY2TE3 (Dy–Te)

- Id: `phase:dy-te:dy2te3`; status `assigned`
- Structure: Sc2S3 · oF80 · Fddd (70); type `st:sc2s3-of80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1837.11 K, x(Te) 0.5714–0.59849
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:dy2te3)

Names (3): _corpus: _corpus:phase:dy-te:dy2te3  
_paper: _paper:10.1007/s11669-023-01051-1:Dy2Te3  
_tdb: _tdb:DyTe-23Cui.tdb:DY2TE3  


### TDB models of DY2TE3 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): DY2TE3, type code %, sha256 `a26fd7267d158c68…`

~~~~text
59: PHASE DY2TE3 % 3 0.4 0.5714 0.0286 !
60: CONST DY2TE3 : DY : TE : DY TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## DY4TE11 (Dy–Te)

- Id: `phase:dy-te:dy4te11`; status `assigned`
- Structure: NdTe3 · oC16 · Cmcm (63); type `st:ndte3-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Dy 0.2667, Te 0.7333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1129.71 K, x(Te) 0.73333–0.73333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:dy4te11)

Names (3): _corpus: _corpus:phase:dy-te:dy4te11  
_paper: _paper:10.1007/s11669-023-01051-1:Dy4Te11  
_tdb: _tdb:DyTe-23Cui.tdb:DY4TE11  


### TDB models of DY4TE11 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): DY4TE11, type code %, sha256 `a26fd7267d158c68…`

~~~~text
74: PHASE DY4TE11 % 2 4 11 !
75: CONST DY4TE11 : DY : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## DY4TE7 (Dy–Te)

- Id: `phase:dy-te:dy4te7`; status `assigned`
- Structure: UAs2 · tP6 · P4/nmm (129); type `st:uas2-tp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Dy 0.3636, Te 0.6364
- Stability: stable in 1 of 1 calculated diagram(s): 300–1495.37 K, x(Te) 0.63636–0.63636
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:dy4te7)

Names (3): _corpus: _corpus:phase:dy-te:dy4te7  
_paper: _paper:10.1007/s11669-023-01051-1:Dy4Te7  
_tdb: _tdb:DyTe-23Cui.tdb:DY4TE7  


### TDB models of DY4TE7 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): DY4TE7, type code %, sha256 `a26fd7267d158c68…`

~~~~text
64: PHASE DY4TE7 % 2 4 7 !
65: CONST DY4TE7 : DY : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## DY4TE9 (Dy–Te)

- Id: `phase:dy-te:dy4te9`; status `assigned`
- Structure: Nd2Te5 · oC28 · Cmcm (63); type `st:nd2te5-oc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Dy 0.3077, Te 0.6923
- Stability: stable in 1 of 1 calculated diagram(s): 300–1193.33 K, x(Te) 0.69231–0.69231
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:dy4te9)

Names (3): _corpus: _corpus:phase:dy-te:dy4te9  
_paper: _paper:10.1007/s11669-023-01051-1:Dy4Te9  
_tdb: _tdb:DyTe-23Cui.tdb:DY4TE9  


### TDB models of DY4TE9 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): DY4TE9, type code %, sha256 `a26fd7267d158c68…`

~~~~text
69: PHASE DY4TE9 % 2 4 9 !
70: CONST DY4TE9 : DY : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

## DYTE_B1 (Dy–Te)

- Id: `phase:dy-te:dyte-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2113.43 K, x(Te) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:dyte-b1)

Names (2): _corpus: _corpus:phase:dy-te:dyte-b1  
_tdb: _tdb:DyTe-23Cui.tdb:DYTE_B1  


### TDB models of DYTE_B1 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): DYTE_B1, type code %, sha256 `a26fd7267d158c68…`

~~~~text
54: PHASE DYTE_B1 % 2 1 1 !
55: CONST DYTE_B1 : DY : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## HCP_A3 (Dy–Te)

- Id: `phase:dy-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1654.15 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:hcp-a3)

Names (2): _corpus: _corpus:phase:dy-te:hcp-a3  
_tdb: _tdb:DyTe-23Cui.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): HCP_A3, type code %A, sha256 `a26fd7267d158c68…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : DY : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## LIQUID (Dy–Te)

- Id: `phase:dy-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 722.63–2500 K, x(Te) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-te:liquid)

Names (3): _corpus: _corpus:phase:dy-te:liquid  
_paper: _paper:10.1007/s11669-023-01051-1:Liquid  
_tdb: _tdb:DyTe-23Cui.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[DyTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb): LIQUID, type code %, sha256 `a26fd7267d158c68…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : DY DYTE TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase; reports values for this phase_

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
