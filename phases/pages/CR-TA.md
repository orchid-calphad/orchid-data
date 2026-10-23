# Cr–Ta phases

> Cr–Ta system: 6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-TA.html · Markdown: https://data.orchid-project.org/phases/pages/CR-TA.md

6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-TA) · [full JSON](https://data.orchid-project.org/phases/systems/CR-TA.json) · [Cr–Ta system page](https://data.orchid-project.org/systems/CR-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Ta system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-ta-bcc-a2); _phase:cr-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.99 K, x(Ta) 0–1 | 0 | 2 |
| [C14_LAVES](#phase-cr-ta-c14-laves); _phase:cr-ta:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1903.36–2307.5 K, x(Ta) 0.30232–0.38351 | 0 | 2 |
| [C15_LAVES](#phase-cr-ta-c15-laves); _phase:cr-ta:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2190 K, x(Ta) 0.3111–0.37408 | 4 | 2 |
| [FCC_A1](#phase-cr-ta-fcc-a1); _phase:cr-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-cr-ta-hcp-a3); _phase:cr-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cr-ta-liquid); _phase:cr-ta:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2043.56–4000 K, x(Ta) 0–1 | 0 | 2 |

## BCC_A2 (Cr–Ta)

- Id: `phase:cr-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.99 K, x(Ta) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ta:bcc-a2)

Names (3): _corpus: _corpus:phase:cr-ta:bcc-a2  
_tdb: _tdb:CrTa-09Pav.tdb:BCC_A2, tdb:CrTa-93Dup-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CrTa-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-09Pav.tdb): BCC_A2, type code %B, sha256 `9b511b195240080d…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR% TA% : VA : !
~~~~

[CrTa-93Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-93Dup-LB.tdb): BCC_A2, type code %B, sha256 `4ebec6dec118a81c…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CR% TA% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02671963](https://doi.org/10.1007/BF02671963) N. Dupin, I. Ansara, J. Phase Equilib., 14, 451-56(1993), addendum, ibid, 15, 135(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_

## C14_LAVES (Cr–Ta)

- Id: `phase:cr-ta:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTa-09Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTa-93Dup-LB.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 1903.36–2307.5 K, x(Ta) 0.30232–0.38351
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ta:c14-laves)

Names (3): _corpus: _corpus:phase:cr-ta:c14-laves  
_tdb: _tdb:CrTa-09Pav.tdb:C14_LAVES, tdb:CrTa-93Dup-LB.tdb:C14_LAVES  


### TDB models of C14_LAVES (2): PHASE and CONSTITUENT statements as written

[CrTa-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-09Pav.tdb): C14_LAVES, type code %, sha256 `9b511b195240080d…`

~~~~text
41: PHASE C14_LAVES % 2 2 1 !
42: CONST C14_LAVES : CR% TA : CR TA% : !
~~~~

[CrTa-93Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-93Dup-LB.tdb): C14_LAVES, type code %, sha256 `4ebec6dec118a81c…`

~~~~text
51: PHASE C14_LAVES % 2 2 1 !
52: CONST C14_LAVES : CR% TA : CR TA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02671963](https://doi.org/10.1007/BF02671963) N. Dupin, I. Ansara, J. Phase Equilib., 14, 451-56(1993), addendum, ibid, 15, 135(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_

## C15_LAVES (Cr–Ta)

- Id: `phase:cr-ta:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrTa-09Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrTa-93Dup-LB.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–2190 K, x(Ta) 0.3111–0.37408
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ta:c15-laves)

Names (4): _corpus: _corpus:phase:cr-ta:c15-laves  
_paper: _paper:10.1007/bf02671963:Cr2Ta (LT)  
_tdb: _tdb:CrTa-09Pav.tdb:C15_LAVES, tdb:CrTa-93Dup-LB.tdb:C15_LAVES  


### TDB models of C15_LAVES (2): PHASE and CONSTITUENT statements as written

[CrTa-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-09Pav.tdb): C15_LAVES, type code %, sha256 `9b511b195240080d…`

~~~~text
46: PHASE C15_LAVES % 2 2 1 !
47: CONST C15_LAVES : CR% TA : CR TA% : !
~~~~

[CrTa-93Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-93Dup-LB.tdb): C15_LAVES, type code %, sha256 `4ebec6dec118a81c…`

~~~~text
56: PHASE C15_LAVES % 2 2 1 !
57: CONST C15_LAVES : CR% TA : CR TA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02671963](https://doi.org/10.1007/BF02671963) N. Dupin, I. Ansara, J. Phase Equilib., 14, 451-56(1993), addendum, ibid, 15, 135(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90032-f](https://doi.org/10.1016/0364-5916%2891%2990032-f) L. Kaufman, "Coupled Thermochemical and Phase Diagram Data for Tantalum Based Binary Alloys," Calphad, 15(4), 317-426 (1991). 91V'fl: P. Villars and L.D. Calvert, Pearson's Handbaok of Crystallographic Data for Intermetallic Phase, 2nd ed., Vol 3, ASM International, Materials Park, OH, 2750 (1991 ).  
_cited as the source of values for this phase_
- [doi:10.1039/tf9646001941](https://doi.org/10.1039/tf9646001941) P. Feschotte, O. Kubaschewski, Thermochemical properties of the laves phase, Cr2Ta, Trans. Faraday Soc. 60, 1941 (1964).  
_cited as the source of values for this phase_

## FCC_A1 (Cr–Ta)

- Id: `phase:cr-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ta:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-ta:fcc-a1  
_tdb: _tdb:CrTa-09Pav.tdb:FCC_A1, tdb:CrTa-93Dup-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CrTa-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-09Pav.tdb): FCC_A1, type code %A, sha256 `9b511b195240080d…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR TA : VA : !
~~~~

[CrTa-93Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-93Dup-LB.tdb): FCC_A1, type code %A, sha256 `4ebec6dec118a81c…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : CR TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02671963](https://doi.org/10.1007/BF02671963) N. Dupin, I. Ansara, J. Phase Equilib., 14, 451-56(1993), addendum, ibid, 15, 135(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_

## HCP_A3 (Cr–Ta)

- Id: `phase:cr-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ta:hcp-a3)

Names (3): _corpus: _corpus:phase:cr-ta:hcp-a3  
_tdb: _tdb:CrTa-09Pav.tdb:HCP_A3, tdb:CrTa-93Dup-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CrTa-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-09Pav.tdb): HCP_A3, type code %A, sha256 `9b511b195240080d…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR TA : VA : !
~~~~

[CrTa-93Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-93Dup-LB.tdb): HCP_A3, type code %A, sha256 `4ebec6dec118a81c…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : CR TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02671963](https://doi.org/10.1007/BF02671963) N. Dupin, I. Ansara, J. Phase Equilib., 14, 451-56(1993), addendum, ibid, 15, 135(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
_assessment that models this phase_

## LIQUID (Cr–Ta)

- Id: `phase:cr-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2043.56–4000 K, x(Ta) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ta:liquid)

Names (3): _corpus: _corpus:phase:cr-ta:liquid  
_tdb: _tdb:CrTa-09Pav.tdb:LIQUID, tdb:CrTa-93Dup-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CrTa-09Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-09Pav.tdb): LIQUID, type code %, sha256 `9b511b195240080d…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR TA : !
~~~~

[CrTa-93Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrTa-93Dup-LB.tdb): LIQUID, type code %, sha256 `4ebec6dec118a81c…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : CR TA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02671963](https://doi.org/10.1007/BF02671963) N. Dupin, I. Ansara, J. Phase Equilib., 14, 451-56(1993), addendum, ibid, 15, 135(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.04.006](https://doi.org/10.1016/j.calphad.2008.04.006) J. Pavlů, J. Vřešt’ál, M. Šob, Re-modeling of Laves phases in the Cr–Nb and Cr–Ta systems using first-principles results, Calphad 33, 179-186 (2009).  
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
