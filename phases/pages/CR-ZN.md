# Cr–Zn phases

> Cr–Zn system: 6 phases (tier A 3, tier C 1, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/CR-ZN.md

6 phases (tier A 3, tier C 1, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/CR-ZN.json) · [Cr–Zn system page](https://data.orchid-project.org/systems/CR-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Zn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-zn-bcc-a2); _phase:cr-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2358.62 K, x(Zn) 0–0.02062 | 9 | 3 |
| [CRZN13](#phase-cr-zn-crzn13); _phase:cr-zn:crzn13_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–761.42 K, x(Zn) 0.92857–0.92857 | 7 | 2 |
| [CRZN17](#phase-cr-zn-crzn17); _phase:cr-zn:crzn17_ | Au2.5Cr7.5Zn90 · cF548 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–736.52 K, x(Zn) 0.94444–0.94444 | 15 | 3 |
| [FCC_A1](#phase-cr-zn-fcc-a1); _phase:cr-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-cr-zn-hcp-a3); _phase:cr-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3998.93 K, x(Zn) 1–1 | 5 | 3 |
| [LIQUID](#phase-cr-zn-liquid); _phase:cr-zn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 691.46–4000 K, x(Zn) 0–1 | 22 | 3 |

## BCC_A2 (Cr–Zn)

- Id: `phase:cr-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2358.62 K, x(Zn) 0–0.02062
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-zn:bcc-a2)

Names (8): _corpus: _corpus:phase:cr-zn:bcc-a2  
_paper: _paper:10.1007/s11669-003-0006-4:bcc_A2, paper:10.1016/j.jallcom.2010.02.087:(Cr), paper:10.1016/j.jallcom.2010.02.087:β-Cr, paper:10.1016/s0364-5916(98)00037-6:bcc-A2  
_tdb: _tdb:CrZn-03Reu-LB.tdb:BCC_A2, tdb:CrZn-10Su.tdb:BCC_A2, tdb:CrZn-98Ans.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CrZn-03Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-03Reu-LB.tdb): BCC_A2, type code %B, sha256 `a1b249392f3b86f0…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% ZN : VA : !
~~~~

[CrZn-10Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-10Su.tdb): BCC_A2, type code %B, sha256 `132759fcba46e488…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR% ZN : VA : !
~~~~

[CrZn-98Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-98Ans.tdb): BCC_A2, type code %B, sha256 `1d3d06ce513339db…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% ZN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.087](https://doi.org/10.1016/j.jallcom.2010.02.087) Xuping Su, Ya Liu, Daniel Y.H. Liu, Jean-Claude Tedenac, Fucheng Yin, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Cr system, Journal of Alloys and Compounds 496, 159-163 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-003-0006-4](https://doi.org/10.1007/s11669-003-0006-4) Guy Reumont, Pierre Perrot, Thermodynamic assessment of the Zinc-Rich part of the Cr-Zn system, JPE 24, 50-54 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1515/ijmr-1948-390202](https://doi.org/10.1515/ijmr-1948-390202) T. Heumann, Z. Metallkd 39 (1948) 45 (in German).  
_cited as the source of values for this phase_

## CRZN13 (Cr–Zn)

- Id: `phase:cr-zn:crzn13`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (CrZn13) · m\*\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (CrZn13) — Hallstedt 2025 mmc2 row for CRZN13: CrZn13
- Stoichiometry: Cr 0.0714, Zn 0.9286
- Stability: stable in 2 of 2 calculated diagram(s): 300–761.42 K, x(Zn) 0.92857–0.92857
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-zn:crzn13)

Names (5): _corpus: _corpus:phase:cr-zn:crzn13  
_paper: _paper:10.1007/s11669-003-0006-4:CrZn13, paper:10.1016/s0364-5916(98)00037-6:CrZn13  
_tdb: _tdb:CrZn-03Reu-LB.tdb:CRZN13, tdb:CrZn-98Ans.tdb:CRZN13  


### TDB models of CRZN13 (2): PHASE and CONSTITUENT statements as written

[CrZn-03Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-03Reu-LB.tdb): CRZN13, type code %, sha256 `a1b249392f3b86f0…`

~~~~text
40: PHASE CRZN13 % 2 1 13 !
41: CONST CRZN13 : CR : ZN : !
~~~~

[CrZn-98Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-98Ans.tdb): CRZN13, type code %, sha256 `1d3d06ce513339db…`

~~~~text
40: PHASE CRZN13 % 2 1 13 !
41: CONST CRZN13 : CR : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-003-0006-4](https://doi.org/10.1007/s11669-003-0006-4) Guy Reumont, Pierre Perrot, Thermodynamic assessment of the Zinc-Rich part of the Cr-Zn system, JPE 24, 50-54 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## CRZN17 (Cr–Zn)

- Id: `phase:cr-zn:crzn17`; status `assigned`
- Structure: Au2.5Cr7.5Zn90 · cF548 · F-43m (216); type `st:au2-5cr7-5zn90-cf548`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cr 0.0556, Zn 0.9444
- Stability: stable in 3 of 3 calculated diagram(s): 300–736.52 K, x(Zn) 0.94444–0.94444
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-zn:crzn17)

Names (7): _corpus: _corpus:phase:cr-zn:crzn17  
_paper: _paper:10.1007/s11669-003-0006-4:CrZn17, paper:10.1016/j.jallcom.2010.02.087:CrZn17, paper:10.1016/s0364-5916(98)00037-6:CrZn17  
_tdb: _tdb:CrZn-03Reu-LB.tdb:CRZN17, tdb:CrZn-10Su.tdb:CRZN17, tdb:CrZn-98Ans.tdb:CRZN17  


### TDB models of CRZN17 (3): PHASE and CONSTITUENT statements as written

[CrZn-03Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-03Reu-LB.tdb): CRZN17, type code %, sha256 `a1b249392f3b86f0…`

~~~~text
45: PHASE CRZN17 % 2 1 17 !
46: CONST CRZN17 : CR : ZN : !
~~~~

[CrZn-10Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-10Su.tdb): CRZN17, type code %, sha256 `132759fcba46e488…`

~~~~text
42: PHASE CRZN17 % 2 1 17 !
43: CONST CRZN17 : CR : ZN : !
~~~~

[CrZn-98Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-98Ans.tdb): CRZN17, type code %, sha256 `1d3d06ce513339db…`

~~~~text
45: PHASE CRZN17 % 2 1 17 !
46: CONST CRZN17 : CR : ZN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2010.02.087](https://doi.org/10.1016/j.jallcom.2010.02.087) Xuping Su, Ya Liu, Daniel Y.H. Liu, Jean-Claude Tedenac, Fucheng Yin, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Cr system, Journal of Alloys and Compounds 496, 159-163 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-003-0006-4](https://doi.org/10.1007/s11669-003-0006-4) Guy Reumont, Pierre Perrot, Thermodynamic assessment of the Zinc-Rich part of the Cr-Zn system, JPE 24, 50-54 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1515/ijmr-1948-390202](https://doi.org/10.1515/ijmr-1948-390202) T. Heumann, Z. Metallkd 39 (1948) 45 (in German).  
_cited as the source of values for this phase_

## FCC_A1 (Cr–Zn)

- Id: `phase:cr-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-zn:fcc-a1)

Names (4): _corpus: _corpus:phase:cr-zn:fcc-a1  
_tdb: _tdb:CrZn-03Reu-LB.tdb:FCC_A1, tdb:CrZn-10Su.tdb:FCC_A1, tdb:CrZn-98Ans.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CrZn-03Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-03Reu-LB.tdb): FCC_A1, type code %A, sha256 `a1b249392f3b86f0…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR ZN : VA : !
~~~~

[CrZn-10Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-10Su.tdb): FCC_A1, type code %A, sha256 `132759fcba46e488…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR ZN : VA : !
~~~~

[CrZn-98Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-98Ans.tdb): FCC_A1, type code %A, sha256 `1d3d06ce513339db…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-003-0006-4](https://doi.org/10.1007/s11669-003-0006-4) Guy Reumont, Pierre Perrot, Thermodynamic assessment of the Zinc-Rich part of the Cr-Zn system, JPE 24, 50-54 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.02.087](https://doi.org/10.1016/j.jallcom.2010.02.087) Xuping Su, Ya Liu, Daniel Y.H. Liu, Jean-Claude Tedenac, Fucheng Yin, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Cr system, Journal of Alloys and Compounds 496, 159-163 (2010).  
_assessment that models this phase_

## HCP_A3 (Cr–Zn)

- Id: `phase:cr-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3998.93 K, x(Zn) 1–1
- Literature: 5 values (5 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-zn:hcp-a3)

Names (7): _corpus: _corpus:phase:cr-zn:hcp-a3  
_paper: _paper:10.1007/s11669-003-0006-4:hcp_A3, paper:10.1016/j.jallcom.2010.02.087:(hcp(Zn)), paper:10.1016/s0364-5916(98)00037-6:hcp-Zn  
_tdb: _tdb:CrZn-03Reu-LB.tdb:HCP_A3, tdb:CrZn-10Su.tdb:HCP_A3, tdb:CrZn-98Ans.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CrZn-03Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-03Reu-LB.tdb): HCP_A3, type code %A, sha256 `a1b249392f3b86f0…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR ZN% : VA : !
~~~~

[CrZn-10Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-10Su.tdb): HCP_A3, type code %A, sha256 `132759fcba46e488…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CR ZN% : VA : !
~~~~

[CrZn-98Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-98Ans.tdb): HCP_A3, type code %A, sha256 `1d3d06ce513339db…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR ZN% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-003-0006-4](https://doi.org/10.1007/s11669-003-0006-4) Guy Reumont, Pierre Perrot, Thermodynamic assessment of the Zinc-Rich part of the Cr-Zn system, JPE 24, 50-54 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.02.087](https://doi.org/10.1016/j.jallcom.2010.02.087) Xuping Su, Ya Liu, Daniel Y.H. Liu, Jean-Claude Tedenac, Fucheng Yin, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Cr system, Journal of Alloys and Compounds 496, 159-163 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1515/ijmr-1948-390202](https://doi.org/10.1515/ijmr-1948-390202) T. Heumann, Z. Metallkd 39 (1948) 45 (in German).  
_cited as the source of values for this phase_

## LIQUID (Cr–Zn)

- Id: `phase:cr-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 691.46–4000 K, x(Zn) 0–1
- Literature: 22 values (22 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-zn:liquid)

Names (9): _corpus: _corpus:phase:cr-zn:liquid  
_paper: _paper:10.1007/s11669-003-0006-4:L, paper:10.1007/s11669-003-0006-4:liquid, paper:10.1016/j.jallcom.2010.02.087:L, paper:10.1016/j.jallcom.2010.02.087:Liquid, paper:10.1016/s0364-5916(98)00037-6:L  
_tdb: _tdb:CrZn-03Reu-LB.tdb:LIQUID, tdb:CrZn-10Su.tdb:LIQUID, tdb:CrZn-98Ans.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CrZn-03Reu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-03Reu-LB.tdb): LIQUID, type code %, sha256 `a1b249392f3b86f0…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR ZN : !
~~~~

[CrZn-10Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-10Su.tdb): LIQUID, type code %, sha256 `132759fcba46e488…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CR ZN : !
~~~~

[CrZn-98Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/CrZn-98Ans.tdb): LIQUID, type code %, sha256 `1d3d06ce513339db…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR ZN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-003-0006-4](https://doi.org/10.1007/s11669-003-0006-4) Guy Reumont, Pierre Perrot, Thermodynamic assessment of the Zinc-Rich part of the Cr-Zn system, JPE 24, 50-54 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.02.087](https://doi.org/10.1016/j.jallcom.2010.02.087) Xuping Su, Ya Liu, Daniel Y.H. Liu, Jean-Claude Tedenac, Fucheng Yin, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Cr system, Journal of Alloys and Compounds 496, 159-163 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1515/ijmr-1948-390202](https://doi.org/10.1515/ijmr-1948-390202) T. Heumann, Z. Metallkd 39 (1948) 45 (in German).  
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
