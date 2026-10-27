# Ag–Sr phases

> Ag–Sr system: 9 phases (tier A 4, tier B 1, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-SR.html · Markdown: https://data.orchid-project.org/phases/pages/AG-SR.md

9 phases (tier A 4, tier B 1, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-SR) · [full JSON](https://data.orchid-project.org/phases/systems/AG-SR.json) · [Ag–Sr system page](https://data.orchid-project.org/systems/AG-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Sr system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2SR](#phase-ag-sr-ag2sr); _phase:ag-sr:ag2sr_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1033.38 K, x(Sr) 0.33333–0.33333 | 6 | 1 |
| [AG2SR3](#phase-ag-sr-ag2sr3); _phase:ag-sr:ag2sr3_ | Er3Ni2 · hR15 · R-3 (148) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–938.23 K, x(Sr) 0.6–0.6 | 0 | 1 |
| [AG4SR](#phase-ag-sr-ag4sr); _phase:ag-sr:ag4sr_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–985.57 K, x(Sr) 0.2–0.2 | 4 | 1 |
| [AG5SR_D2D](#phase-ag-sr-ag5sr-d2d); _phase:ag-sr:ag5sr-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1056.08 K, x(Sr) 0.16667–0.16667 | 6 | 1 |
| [AGSR](#phase-ag-sr-agsr); _phase:ag-sr:agsr_ | AgSr · oP16 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–945.96 K, x(Sr) 0.5–0.5 | 2 | 1 |
| [BCC_A2](#phase-ag-sr-bcc-a2); _phase:ag-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 820–1050 K, x(Sr) 0.99908–1 | 0 | 1 |
| [FCC_A1](#phase-ag-sr-fcc-a1); _phase:ag-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1268.58 K, x(Sr) 0–1 | 2 | 1 |
| [HCP_A3](#phase-ag-sr-hcp-a3); _phase:ag-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-sr-liquid); _phase:ag-sr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 709.45–2500 K, x(Sr) 0–1 | 12 | 1 |

## AG2SR (Ag–Sr)

- Id: `phase:ag-sr:ag2sr`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.6667, Sr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1033.38 K, x(Sr) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:ag2sr)

Names (3): _corpus: _corpus:phase:ag-sr:ag2sr  
_paper: _paper:10.1016/j.jallcom.2005.06.019:Ag2Sr  
_tdb: _tdb:AgSr-06Liu.tdb:AG2SR  


### TDB models of AG2SR (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): AG2SR, type code %, sha256 `88cea835a729b38b…`

~~~~text
55: PHASE AG2SR % 2 2 1 !
56: CONST AG2SR : AG : SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(01)00041-4](https://doi.org/10.1016/s0364-5916%2801%2900041-4) G.B. Olson, Calphad 25 (2) (2001) 175–190.  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1999.tb02283.x](https://doi.org/10.1111/j.1151-2916.1999.tb02283.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase‐Diagram Study and Thermodynamic Optimization of the Silver‐Strontium‐Copper‐Oxygen (Ag‐Sr‐Cu‐O) and Silver‐Calcium‐Copper‐Oxygen (Ag‐Ca‐Cu‐O) Systems, Journal of the American Ceramic Society 82, 3591-3596 (1999).  
_cited as the source of values for this phase_

## AG2SR3 (Ag–Sr)

- Id: `phase:ag-sr:ag2sr3`; status `assigned`
- Structure: Er3Ni2 · hR15 · R-3 (148); type `st:er3ni2-hr15`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ag 0.4000, Sr 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–938.23 K, x(Sr) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:ag2sr3)

Names (4): _corpus: _corpus:phase:ag-sr:ag2sr3  
_mp: _mp:mp-aaaabsxp  
_oqmd: _oqmd:oqmd-10670  
_tdb: _tdb:AgSr-06Liu.tdb:AG2SR3  


### TDB models of AG2SR3 (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): AG2SR3, type code %, sha256 `88cea835a729b38b…`

~~~~text
65: PHASE AG2SR3 % 2 2 3 !
66: CONST AG2SR3 : AG : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase_

## AG4SR (Ag–Sr)

- Id: `phase:ag-sr:ag4sr`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Ag4Sr) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ag4Sr) — Hallstedt 2025 mmc2 row for AG4SR: Ag4Sr
- Stoichiometry: Ag 0.8000, Sr 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–985.57 K, x(Sr) 0.2–0.2
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:ag4sr)

Names (3): _corpus: _corpus:phase:ag-sr:ag4sr  
_paper: _paper:10.1016/j.jallcom.2005.06.019:Ag4Sr  
_tdb: _tdb:AgSr-06Liu.tdb:AG4SR  


### TDB models of AG4SR (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): AG4SR, type code %, sha256 `88cea835a729b38b…`

~~~~text
50: PHASE AG4SR % 2 4 1 !
51: CONST AG4SR : AG : SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(01)00041-4](https://doi.org/10.1016/s0364-5916%2801%2900041-4) G.B. Olson, Calphad 25 (2) (2001) 175–190.  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1999.tb02283.x](https://doi.org/10.1111/j.1151-2916.1999.tb02283.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase‐Diagram Study and Thermodynamic Optimization of the Silver‐Strontium‐Copper‐Oxygen (Ag‐Sr‐Cu‐O) and Silver‐Calcium‐Copper‐Oxygen (Ag‐Ca‐Cu‐O) Systems, Journal of the American Ceramic Society 82, 3591-3596 (1999).  
_cited as the source of values for this phase_

## AG5SR_D2D (Ag–Sr)

- Id: `phase:ag-sr:ag5sr-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaados and oqmd-10671, space group 191
- Stoichiometry: Ag 0.8333, Sr 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1056.08 K, x(Sr) 0.16667–0.16667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:ag5sr-d2d)

Names (5): _corpus: _corpus:phase:ag-sr:ag5sr-d2d  
_mp: _mp:mp-aaaaados  
_oqmd: _oqmd:oqmd-10671  
_paper: _paper:10.1016/j.jallcom.2005.06.019:Ag5Sr  
_tdb: _tdb:AgSr-06Liu.tdb:AG5SR_D2D  


### TDB models of AG5SR_D2D (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): AG5SR_D2D, type code %, sha256 `88cea835a729b38b…`

~~~~text
45: PHASE AG5SR_D2D % 2 5 1 !
46: CONST AG5SR_D2D : AG : SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(01)00041-4](https://doi.org/10.1016/s0364-5916%2801%2900041-4) G.B. Olson, Calphad 25 (2) (2001) 175–190.  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1999.tb02283.x](https://doi.org/10.1111/j.1151-2916.1999.tb02283.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase‐Diagram Study and Thermodynamic Optimization of the Silver‐Strontium‐Copper‐Oxygen (Ag‐Sr‐Cu‐O) and Silver‐Calcium‐Copper‐Oxygen (Ag‐Ca‐Cu‐O) Systems, Journal of the American Ceramic Society 82, 3591-3596 (1999).  
_cited as the source of values for this phase_

## AGSR (Ag–Sr)

- Id: `phase:ag-sr:agsr`; status `assigned`
- Structure: AgSr · oP16 · Pnma (62); type `st:agsr-op16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_0_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.5000, Sr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–945.96 K, x(Sr) 0.5–0.5
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:agsr)

Names (3): _corpus: _corpus:phase:ag-sr:agsr  
_paper: _paper:10.1016/j.jallcom.2005.06.019:AgSr  
_tdb: _tdb:AgSr-06Liu.tdb:AGSR  


### TDB models of AGSR (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): AGSR, type code %, sha256 `88cea835a729b38b…`

~~~~text
60: PHASE AGSR % 2 1 1 !
61: CONST AGSR : AG : SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(01)00041-4](https://doi.org/10.1016/s0364-5916%2801%2900041-4) G.B. Olson, Calphad 25 (2) (2001) 175–190.  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1999.tb02283.x](https://doi.org/10.1111/j.1151-2916.1999.tb02283.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase‐Diagram Study and Thermodynamic Optimization of the Silver‐Strontium‐Copper‐Oxygen (Ag‐Sr‐Cu‐O) and Silver‐Calcium‐Copper‐Oxygen (Ag‐Ca‐Cu‐O) Systems, Journal of the American Ceramic Society 82, 3591-3596 (1999).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Sr)

- Id: `phase:ag-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 820–1050 K, x(Sr) 0.99908–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-sr:bcc-a2  
_tdb: _tdb:AgSr-06Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): BCC_A2, type code %B, sha256 `88cea835a729b38b…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG SR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase_

## FCC_A1 (Ag–Sr)

- Id: `phase:ag-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1268.58 K, x(Sr) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-sr:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2005.06.019:fccAg  
_tdb: _tdb:AgSr-06Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): FCC_A1, type code %A, sha256 `88cea835a729b38b…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% SR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(01)00041-4](https://doi.org/10.1016/s0364-5916%2801%2900041-4) G.B. Olson, Calphad 25 (2) (2001) 175–190.  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1999.tb02283.x](https://doi.org/10.1111/j.1151-2916.1999.tb02283.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase‐Diagram Study and Thermodynamic Optimization of the Silver‐Strontium‐Copper‐Oxygen (Ag‐Sr‐Cu‐O) and Silver‐Calcium‐Copper‐Oxygen (Ag‐Ca‐Cu‐O) Systems, Journal of the American Ceramic Society 82, 3591-3596 (1999).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Sr)

- Id: `phase:ag-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-sr:hcp-a3  
_tdb: _tdb:AgSr-06Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): HCP_A3, type code %A, sha256 `88cea835a729b38b…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase_

## LIQUID (Ag–Sr)

- Id: `phase:ag-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 709.45–2500 K, x(Sr) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sr:liquid)

Names (3): _corpus: _corpus:phase:ag-sr:liquid  
_paper: _paper:10.1016/j.jallcom.2005.06.019:L  
_tdb: _tdb:AgSr-06Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgSr-06Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb): LIQUID, type code %, sha256 `88cea835a729b38b…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(01)00041-4](https://doi.org/10.1016/s0364-5916%2801%2900041-4) G.B. Olson, Calphad 25 (2) (2001) 175–190.  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1999.tb02283.x](https://doi.org/10.1111/j.1151-2916.1999.tb02283.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase‐Diagram Study and Thermodynamic Optimization of the Silver‐Strontium‐Copper‐Oxygen (Ag‐Sr‐Cu‐O) and Silver‐Calcium‐Copper‐Oxygen (Ag‐Ca‐Cu‐O) Systems, Journal of the American Ceramic Society 82, 3591-3596 (1999).  
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
