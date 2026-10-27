# Sn–Zn phases

> Sn–Zn system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SN-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/SN-ZN.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SN-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/SN-ZN.json) · [Sn–Zn system page](https://data.orchid-project.org/systems/SN-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SN-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sn–Zn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sn-zn-a4-diamond); _phase:sn-zn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [BCT_A5](#phase-sn-zn-a5-bct); _phase:sn-zn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–505.08 K, x(Zn) 0–0.01231 | 8 | 4 |
| [BCC_A2](#phase-sn-zn-bcc-a2); _phase:sn-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-sn-zn-fcc-a1); _phase:sn-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-sn-zn-hcp-a3); _phase:sn-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2498.93 K, x(Zn) 0.99684–1 | 8 | 4 |
| [LIQUID](#phase-sn-zn-liquid); _phase:sn-zn:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 465.53–2500 K, x(Zn) 0–1 | 8 | 4 |

## DIAMOND_A4 (Sn–Zn)

- Id: `phase:sn-zn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-zn:a4-diamond)

Names (5): _corpus: _corpus:phase:sn-zn:a4-diamond  
_tdb: _tdb:SnZn-93Sri.tdb:DIAMOND_A4, tdb:SnZn-96Lee.tdb:DIAMOND_A4, tdb:SnZn-98Fri-LB.tdb:DIAMOND_A4, tdb:SnZn-99Oht.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SnZn-93Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-93Sri.tdb): DIAMOND_A4, type code %, sha256 `a477685a7eeb967e…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[SnZn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-96Lee.tdb): DIAMOND_A4, type code %, sha256 `242f5b5ef74d7149…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN% ZN : !
~~~~

[SnZn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-98Fri-LB.tdb): DIAMOND_A4, type code %, sha256 `c592cd8539bbd468…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SN% ZN : !
~~~~

[SnZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-99Oht.tdb): DIAMOND_A4, type code %, sha256 `b9bc638c140accc3…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## BCT_A5 (Sn–Zn)

- Id: `phase:sn-zn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–505.08 K, x(Zn) 0–0.01231
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-zn:a5-bct)

Names (8): _corpus: _corpus:phase:sn-zn:a5-bct, corpus:phase:sn-zn:bct-a5  
_paper: _paper:10.1007/bf02667882:(Sn), paper:sha256-85fd53a1a176b694:bct-A5  
_tdb: _tdb:SnZn-93Sri.tdb:BCT_A5, tdb:SnZn-96Lee.tdb:BCT_A5, tdb:SnZn-98Fri-LB.tdb:BCT_A5, tdb:SnZn-99Oht.tdb:BCT_A5  


### TDB models of BCT_A5 (4): PHASE and CONSTITUENT statements as written

[SnZn-93Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-93Sri.tdb): BCT_A5, type code %, sha256 `a477685a7eeb967e…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN% ZN : !
~~~~

[SnZn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-96Lee.tdb): BCT_A5, type code %, sha256 `242f5b5ef74d7149…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN% ZN : !
~~~~

[SnZn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-98Fri-LB.tdb): BCT_A5, type code %, sha256 `c592cd8539bbd468…`

~~~~text
45: PHASE BCT_A5 % 1 1 !
46: CONST BCT_A5 : SN% ZN : !
~~~~

[SnZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-99Oht.tdb): BCT_A5, type code %, sha256 `b9bc638c140accc3…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : SN% ZN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## BCC_A2 (Sn–Zn)

- Id: `phase:sn-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-zn:bcc-a2)

Names (5): _corpus: _corpus:phase:sn-zn:bcc-a2  
_tdb: _tdb:SnZn-93Sri.tdb:BCC_A2, tdb:SnZn-96Lee.tdb:BCC_A2, tdb:SnZn-98Fri-LB.tdb:BCC_A2, tdb:SnZn-99Oht.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[SnZn-93Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-93Sri.tdb): BCC_A2, type code %B, sha256 `a477685a7eeb967e…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SN ZN : VA : !
~~~~

[SnZn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-96Lee.tdb): BCC_A2, type code %B, sha256 `242f5b5ef74d7149…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SN ZN : VA : !
~~~~

[SnZn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-98Fri-LB.tdb): BCC_A2, type code %B, sha256 `c592cd8539bbd468…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : SN ZN : VA : !
~~~~

[SnZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-99Oht.tdb): BCC_A2, type code %B, sha256 `b9bc638c140accc3…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : SN ZN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## FCC_A1 (Sn–Zn)

- Id: `phase:sn-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-zn:fcc-a1)

Names (5): _corpus: _corpus:phase:sn-zn:fcc-a1  
_tdb: _tdb:SnZn-93Sri.tdb:FCC_A1, tdb:SnZn-96Lee.tdb:FCC_A1, tdb:SnZn-98Fri-LB.tdb:FCC_A1, tdb:SnZn-99Oht.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[SnZn-93Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-93Sri.tdb): FCC_A1, type code %A, sha256 `a477685a7eeb967e…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SN ZN : VA : !
~~~~

[SnZn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-96Lee.tdb): FCC_A1, type code %A, sha256 `242f5b5ef74d7149…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SN ZN : VA : !
~~~~

[SnZn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-98Fri-LB.tdb): FCC_A1, type code %A, sha256 `c592cd8539bbd468…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SN ZN : VA : !
~~~~

[SnZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-99Oht.tdb): FCC_A1, type code %A, sha256 `b9bc638c140accc3…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SN ZN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## HCP_A3 (Sn–Zn)

- Id: `phase:sn-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2498.93 K, x(Zn) 0.99684–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-zn:hcp-a3)

Names (7): _corpus: _corpus:phase:sn-zn:hcp-a3  
_paper: _paper:10.1007/bf02667882:(Zn), paper:sha256-85fd53a1a176b694:hcp-Zn  
_tdb: _tdb:SnZn-93Sri.tdb:HCP_A3, tdb:SnZn-96Lee.tdb:HCP_A3, tdb:SnZn-98Fri-LB.tdb:HCP_A3, tdb:SnZn-99Oht.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[SnZn-93Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-93Sri.tdb): HCP_A3, type code %A, sha256 `a477685a7eeb967e…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SN ZN% : VA: !
~~~~

[SnZn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-96Lee.tdb): HCP_A3, type code %A, sha256 `242f5b5ef74d7149…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SN ZN% : VA: !
~~~~

[SnZn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-98Fri-LB.tdb): HCP_A3, type code %A, sha256 `c592cd8539bbd468…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SN ZN% : VA: !
~~~~

[SnZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-99Oht.tdb): HCP_A3, type code %A, sha256 `b9bc638c140accc3…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : SN ZN% : VA: !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## LIQUID (Sn–Zn)

- Id: `phase:sn-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 465.53–2500 K, x(Zn) 0–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-zn:liquid)

Names (7): _corpus: _corpus:phase:sn-zn:liquid  
_paper: _paper:10.1007/bf02667882:L, paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:SnZn-93Sri.tdb:LIQUID, tdb:SnZn-96Lee.tdb:LIQUID, tdb:SnZn-98Fri-LB.tdb:LIQUID, tdb:SnZn-99Oht.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SnZn-93Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-93Sri.tdb): LIQUID, type code %, sha256 `a477685a7eeb967e…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SN ZN : !
~~~~

[SnZn-96Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-96Lee.tdb): LIQUID, type code %, sha256 `242f5b5ef74d7149…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SN ZN : !
~~~~

[SnZn-98Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-98Fri-LB.tdb): LIQUID, type code %, sha256 `c592cd8539bbd468…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SN ZN : !
~~~~

[SnZn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/SnZn-99Oht.tdb): LIQUID, type code %, sha256 `b9bc638c140accc3…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SN ZN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667882](https://doi.org/10.1007/BF02667882) M. Srivastava, R.C. Sharma, J. Phase Equilib., 14, 700-709(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(97)00009-6](https://doi.org/10.1016/S0364-5916%2897%2900009-6) B.-J. Lee, Calphad, 20, 471-80(1996).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

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
