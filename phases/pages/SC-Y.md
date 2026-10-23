# Sc–Y phases

> Sc–Y system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SC-Y.html · Markdown: https://data.orchid-project.org/phases/pages/SC-Y.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SC-Y) · [full JSON](https://data.orchid-project.org/phases/systems/SC-Y.json) · [Sc–Y system page](https://data.orchid-project.org/systems/SC-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/SC-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sc–Y system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-sc-y-bcc-a2); _phase:sc-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1453.08–2499.26 K, x(Y) 0–1 | 18 | 2 |
| [FCC_A1](#phase-sc-y-fcc-a1); _phase:sc-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-sc-y-hcp-a3); _phase:sc-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1784.13 K, x(Y) 0–1 | 9 | 2 |
| [LIQUID](#phase-sc-y-liquid); _phase:sc-y:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1641.14–2500 K, x(Y) 0–1 | 9 | 2 |

## BCC_A2 (Sc–Y)

- Id: `phase:sc-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1453.08–2499.26 K, x(Y) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-y:bcc-a2)

Names (6): _corpus: _corpus:phase:sc-y:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.09.053:(βSc, βY), paper:10.1016/j.jallcom.2008.09.053:βSc, paper:10.1016/j.jallcom.2008.09.053:βY  
_tdb: _tdb:ScY-00Nor.tdb:BCC_A2, tdb:ScY-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ScY-00Nor.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-00Nor.tdb): BCC_A2, type code %B, sha256 `244681b40e362092…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : SC% Y% : VA : !
~~~~

[ScY-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-09Wan.tdb): BCC_A2, type code %B, sha256 `45f44917339661b3…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SC% Y% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Y and Sc–Y systems, Journal of Alloys and Compounds 476, 187-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868085](https://doi.org/10.1007/bf02868085) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 4 (4) (1983) 377–379.  
_cited as the source of values for this phase_

## FCC_A1 (Sc–Y)

- Id: `phase:sc-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-y:fcc-a1)

Names (3): _corpus: _corpus:phase:sc-y:fcc-a1  
_tdb: _tdb:ScY-00Nor.tdb:FCC_A1, tdb:ScY-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ScY-00Nor.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-00Nor.tdb): FCC_A1, type code %A, sha256 `244681b40e362092…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SC Y : VA : !
~~~~

[ScY-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-09Wan.tdb): FCC_A1, type code %A, sha256 `45f44917339661b3…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SC Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Y and Sc–Y systems, Journal of Alloys and Compounds 476, 187-192 (2009).  
_assessment that models this phase_

## HCP_A3 (Sc–Y)

- Id: `phase:sc-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1784.13 K, x(Y) 0–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-y:hcp-a3)

Names (6): _corpus: _corpus:phase:sc-y:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.09.053:(αSc, αY), paper:10.1016/j.jallcom.2008.09.053:αSc, paper:10.1016/j.jallcom.2008.09.053:αY  
_tdb: _tdb:ScY-00Nor.tdb:HCP_A3, tdb:ScY-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ScY-00Nor.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-00Nor.tdb): HCP_A3, type code %A, sha256 `244681b40e362092…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SC% Y% : VA : !
~~~~

[ScY-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-09Wan.tdb): HCP_A3, type code %A, sha256 `45f44917339661b3…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SC% Y% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Y and Sc–Y systems, Journal of Alloys and Compounds 476, 187-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868085](https://doi.org/10.1007/bf02868085) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 4 (4) (1983) 377–379.  
_cited as the source of values for this phase_

## LIQUID (Sc–Y)

- Id: `phase:sc-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1641.14–2500 K, x(Y) 0–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-y:liquid)

Names (4): _corpus: _corpus:phase:sc-y:liquid  
_paper: _paper:10.1016/j.jallcom.2008.09.053:L  
_tdb: _tdb:ScY-00Nor.tdb:LIQUID, tdb:ScY-09Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ScY-00Nor.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-00Nor.tdb): LIQUID, type code %, sha256 `244681b40e362092…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SC Y : !
~~~~

[ScY-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScY-09Wan.tdb): LIQUID, type code %, sha256 `45f44917339661b3…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SC Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Y and Sc–Y systems, Journal of Alloys and Compounds 476, 187-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868085](https://doi.org/10.1007/bf02868085) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 4 (4) (1983) 377–379.  
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
