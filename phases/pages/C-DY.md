# C–Dy phases

> C–Dy system: 9 phases (tier A 7, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-DY.html · Markdown: https://data.orchid-project.org/phases/pages/C-DY.md

9 phases (tier A 7, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-DY) · [full JSON](https://data.orchid-project.org/phases/systems/C-DY.json) · [Markdown](https://data.orchid-project.org/phases/pages/C-DY.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Dy system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-dy-a4-diamond); _phase:c-dy:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-c-dy-bcc-a2); _phase:c-dy:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1654.13–3999.13 K, x(C) 0–0 | 0 | 1 |
| [DY2C3_D5C](#phase-c-dy-dy2c3-d5c); _phase:c-dy:dy2c3-d5c_ | Pu2C3 · D5_c · cI40 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1895.03 K, x(C) 0.6–0.6 | 0 | 1 |
| [DYC2_C1](#phase-c-dy-dyc2-c1); _phase:c-dy:dyc2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1568.63–2564.18 K, x(C) 0.66667–0.66667 | 0 | 1 |
| [DYC2_C11A](#phase-c-dy-dyc2-c11a); _phase:c-dy:dyc2-c11a_ | CaC2 · C11_a · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1568.63 K, x(C) 0.66667–0.66667 | 0 | 1 |
| [FCC_A1](#phase-c-dy-fcc-a1); _phase:c-dy:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GRAPHITE](#phase-c-dy-graphite); _phase:c-dy:graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 1 |
| [HCP_A3](#phase-c-dy-hcp-a3); _phase:c-dy:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1669.13 K, x(C) 0–0 | 0 | 1 |
| [LIQUID](#phase-c-dy-liquid); _phase:c-dy:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1212.54–4000 K, x(C) 0–0.84943 | 0 | 1 |

## DIAMOND_A4 (C–Dy)

- Id: `phase:c-dy:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:a4-diamond)

Names (2): _corpus: _corpus:phase:c-dy:a4-diamond  
_tdb: _tdb:DyC-20Xu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): DIAMOND_A4, type code %, sha256 `773f0d8f1049a3a6…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## BCC_A2 (C–Dy)

- Id: `phase:c-dy:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1654.13–3999.13 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:bcc-a2)

Names (2): _corpus: _corpus:phase:c-dy:bcc-a2  
_tdb: _tdb:DyC-20Xu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): BCC_A2, type code %B, sha256 `773f0d8f1049a3a6…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : DY : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## DY2C3_D5C (C–Dy)

- Id: `phase:c-dy:dy2c3-d5c`; status `assigned`
- Structure: Pu2C3 · D5_c · cI40 · I-43d (220); type `st:d5-c-pu2c3-ci40`; tier A: standard phase name; confidence high
- Stoichiometry: C 0.6000, Dy 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1895.03 K, x(C) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:dy2c3-d5c)

Names (2): _corpus: _corpus:phase:c-dy:dy2c3-d5c  
_tdb: _tdb:DyC-20Xu.tdb:DY2C3_D5C  


### TDB models of DY2C3_D5C (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): DY2C3_D5C, type code %, sha256 `773f0d8f1049a3a6…`

~~~~text
56: PHASE DY2C3_D5C % 2 2 3 !
57: CONST DY2C3_D5C : DY : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## DYC2_C1 (C–Dy)

- Id: `phase:c-dy:dyc2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.6667, Dy 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1568.63–2564.18 K, x(C) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:dyc2-c1)

Names (2): _corpus: _corpus:phase:c-dy:dyc2-c1  
_tdb: _tdb:DyC-20Xu.tdb:DYC2_C1  


### TDB models of DYC2_C1 (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): DYC2_C1, type code %, sha256 `773f0d8f1049a3a6…`

~~~~text
66: PHASE DYC2_C1 % 2 1 2 !
67: CONST DYC2_C1 : DY : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## DYC2_C11A (C–Dy)

- Id: `phase:c-dy:dyc2-c11a`; status `assigned`
- Structure: CaC2 · C11_a · tI6 · I4/mmm (139); type `st:c11-a-cac2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: C 0.6667, Dy 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1568.63 K, x(C) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:dyc2-c11a)

Names (2): _corpus: _corpus:phase:c-dy:dyc2-c11a  
_tdb: _tdb:DyC-20Xu.tdb:DYC2_C11A  


### TDB models of DYC2_C11A (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): DYC2_C11A, type code %, sha256 `773f0d8f1049a3a6…`

~~~~text
61: PHASE DYC2_C11A % 2 1 2 !
62: CONST DYC2_C11A : DY : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## FCC_A1 (C–Dy)

- Id: `phase:c-dy:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:fcc-a1)

Names (2): _corpus: _corpus:phase:c-dy:fcc-a1  
_tdb: _tdb:DyC-20Xu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): FCC_A1, type code %A, sha256 `773f0d8f1049a3a6…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : DY : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## GRAPHITE (C–Dy)

- Id: `phase:c-dy:graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:graphite)

Names (2): _corpus: _corpus:phase:c-dy:graphite  
_tdb: _tdb:DyC-20Xu.tdb:GRAPHITE  


### TDB models of GRAPHITE (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): GRAPHITE, type code %, sha256 `773f0d8f1049a3a6…`

~~~~text
51: PHASE GRAPHITE % 1 1 !
52: CONST GRAPHITE : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## HCP_A3 (C–Dy)

- Id: `phase:c-dy:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1669.13 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:hcp-a3)

Names (2): _corpus: _corpus:phase:c-dy:hcp-a3  
_tdb: _tdb:DyC-20Xu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): HCP_A3, type code %A, sha256 `773f0d8f1049a3a6…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : DY : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
_assessment that models this phase_

## LIQUID (C–Dy)

- Id: `phase:c-dy:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1212.54–4000 K, x(C) 0–0.84943
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-dy:liquid)

Names (2): _corpus: _corpus:phase:c-dy:liquid  
_tdb: _tdb:DyC-20Xu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[DyC-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/DyC-20Xu.tdb): LIQUID, type code %, sha256 `773f0d8f1049a3a6…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : C DY : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101738](https://doi.org/10.1016/j.calphad.2020.101738) K. Xu, L. Chen, K. Chang, P. Wan, M. Li, Z. Deng, F. Huang, Q. Huang, Calphad, 68, 101738(2020).  
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
