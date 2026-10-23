# H–Mg phases

> H–Mg system: 6 phases (tier A 4, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-MG.html · Markdown: https://data.orchid-project.org/phases/pages/H-MG.md

6 phases (tier A 4, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-MG) · [full JSON](https://data.orchid-project.org/phases/systems/H-MG.json) · [H–Mg system page](https://data.orchid-project.org/systems/H-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Mg system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-mg-bcc-a2); _phase:h-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-h-mg-fcc-a1); _phase:h-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-h-mg-gas); _phase:h-mg:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1 | 11 | 2 |
| [HCP_A3](#phase-h-mg-hcp-a3); _phase:h-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–922.82 K, x(H) 0–0.00072 | 11 | 2 |
| [LIQUID](#phase-h-mg-liquid); _phase:h-mg:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 922.77–1367.51 K, x(H) 0–0.00158 | 4 | 2 |
| [MGH2_C4](#phase-h-mg-mgh2-c4); _phase:h-mg:mgh2-c4_ | TiO2 · C4 · tP6 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–561.44 K, x(H) 0.66667–0.66667 | 9 | 2 |

## BCC_A2 (H–Mg)

- Id: `phase:h-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mg:bcc-a2)

Names (3): _corpus: _corpus:phase:h-mg:bcc-a2  
_tdb: _tdb:MgH-07Pal.tdb:BCC_A2, tdb:MgH-99Zen.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MgH-07Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-07Pal.tdb): BCC_A2, type code %B, sha256 `8871b1dc6e5850f7…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : MG : VA : !
~~~~

[MgH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-99Zen.tdb): BCC_A2, type code %B, sha256 `7133dff29673a4f1…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.005](https://doi.org/10.1016/j.calphad.2007.04.005) M. Palumbo, F.J. Torres, J.R. Ares, C. Pisani, J.F. Fernandez, M. Baricco, Thermodynamic and ab initio investigation of the Al–H–Mg system, Calphad 31, 457-467 (2007).  
_assessment that models this phase_
- [doi:10.1016/S0360-3199(98)00132-3](https://doi.org/10.1016/S0360-3199%2898%2900132-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, Int. J. Hydrogen Energy, 24, 989-1004(1999).  
_assessment that models this phase_

## FCC_A1 (H–Mg)

- Id: `phase:h-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mg:fcc-a1)

Names (3): _corpus: _corpus:phase:h-mg:fcc-a1  
_tdb: _tdb:MgH-07Pal.tdb:FCC_A1, tdb:MgH-99Zen.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MgH-07Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-07Pal.tdb): FCC_A1, type code %A, sha256 `8871b1dc6e5850f7…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MG : VA : !
~~~~

[MgH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-99Zen.tdb): FCC_A1, type code %A, sha256 `7133dff29673a4f1…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.04.005](https://doi.org/10.1016/j.calphad.2007.04.005) M. Palumbo, F.J. Torres, J.R. Ares, C. Pisani, J.F. Fernandez, M. Baricco, Thermodynamic and ab initio investigation of the Al–H–Mg system, Calphad 31, 457-467 (2007).  
_assessment that models this phase_
- [doi:10.1016/S0360-3199(98)00132-3](https://doi.org/10.1016/S0360-3199%2898%2900132-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, Int. J. Hydrogen Energy, 24, 989-1004(1999).  
_assessment that models this phase_

## GAS (H–Mg)

- Id: `phase:h-mg:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mg:gas)

Names (4): _corpus: _corpus:phase:h-mg:gas  
_paper: _paper:10.1016/s0360-3199(98)00132-3:gas  
_tdb: _tdb:MgH-07Pal.tdb:GAS, tdb:MgH-99Zen.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[MgH-07Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-07Pal.tdb): GAS, type code %, sha256 `8871b1dc6e5850f7…`

~~~~text
50: PHASE GAS:G % 1 1 !
51: CONST GAS:G : H H2 MG MG2 MGH : !
~~~~

[MgH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-99Zen.tdb): GAS, type code %, sha256 `7133dff29673a4f1…`

~~~~text
50: PHASE GAS:G % 1 1 !
51: CONST GAS:G : H H2 MG MG2 MGH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0360-3199(98)00132-3](https://doi.org/10.1016/S0360-3199%2898%2900132-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, Int. J. Hydrogen Energy, 24, 989-1004(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.04.005](https://doi.org/10.1016/j.calphad.2007.04.005) M. Palumbo, F.J. Torres, J.R. Ares, C. Pisani, J.F. Fernandez, M. Baricco, Thermodynamic and ab initio investigation of the Al–H–Mg system, Calphad 31, 457-467 (2007).  
_assessment that models this phase_

## HCP_A3 (H–Mg)

- Id: `phase:h-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–922.82 K, x(H) 0–0.00072
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mg:hcp-a3)

Names (4): _corpus: _corpus:phase:h-mg:hcp-a3  
_paper: _paper:10.1016/s0360-3199(98)00132-3:(Mg)  
_tdb: _tdb:MgH-07Pal.tdb:HCP_A3, tdb:MgH-99Zen.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MgH-07Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-07Pal.tdb): HCP_A3, type code %A, sha256 `8871b1dc6e5850f7…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : MG : H VA% : !
~~~~

[MgH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-99Zen.tdb): HCP_A3, type code %A, sha256 `7133dff29673a4f1…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : MG : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0360-3199(98)00132-3](https://doi.org/10.1016/S0360-3199%2898%2900132-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, Int. J. Hydrogen Energy, 24, 989-1004(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.04.005](https://doi.org/10.1016/j.calphad.2007.04.005) M. Palumbo, F.J. Torres, J.R. Ares, C. Pisani, J.F. Fernandez, M. Baricco, Thermodynamic and ab initio investigation of the Al–H–Mg system, Calphad 31, 457-467 (2007).  
_assessment that models this phase_

## LIQUID (H–Mg)

- Id: `phase:h-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 922.77–1367.51 K, x(H) 0–0.00158
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mg:liquid)

Names (5): _corpus: _corpus:phase:h-mg:liquid  
_paper: _paper:10.1016/s0360-3199(98)00132-3:L, paper:10.1016/s0360-3199(98)00132-3:Liquid  
_tdb: _tdb:MgH-07Pal.tdb:LIQUID, tdb:MgH-99Zen.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MgH-07Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-07Pal.tdb): LIQUID, type code %, sha256 `8871b1dc6e5850f7…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : H MG : !
~~~~

[MgH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-99Zen.tdb): LIQUID, type code %, sha256 `7133dff29673a4f1…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : H MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0360-3199(98)00132-3](https://doi.org/10.1016/S0360-3199%2898%2900132-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, Int. J. Hydrogen Energy, 24, 989-1004(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.04.005](https://doi.org/10.1016/j.calphad.2007.04.005) M. Palumbo, F.J. Torres, J.R. Ares, C. Pisani, J.F. Fernandez, M. Baricco, Thermodynamic and ab initio investigation of the Al–H–Mg system, Calphad 31, 457-467 (2007).  
_assessment that models this phase_

## MGH2_C4 (H–Mg)

- Id: `phase:h-mg:mgh2-c4`; status `assigned`
- Structure: TiO2 · C4 · tP6 · P4_2/mnm (136); type `st:c4-tio2-tp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabjby and oqmd-3742, space group 136
- Stoichiometry: H 0.6667, Mg 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–561.44 K, x(H) 0.66667–0.66667
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-mg:mgh2-c4)

Names (6): _corpus: _corpus:phase:h-mg:mgh2-c4  
_mp: _mp:mp-aaaabjby  
_oqmd: _oqmd:oqmd-3742  
_paper: _paper:10.1016/s0360-3199(98)00132-3:MgH2  
_tdb: _tdb:MgH-07Pal.tdb:MGH2_C4, tdb:MgH-99Zen.tdb:MGH2_C4  


### TDB models of MGH2_C4 (2): PHASE and CONSTITUENT statements as written

[MgH-07Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-07Pal.tdb): MGH2_C4, type code %, sha256 `8871b1dc6e5850f7…`

~~~~text
47: PHASE MGH2_C4 % 2 1 2 !
48: CONST MGH2_C4 : MG : H : !
~~~~

[MgH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/MgH-99Zen.tdb): MGH2_C4, type code %, sha256 `7133dff29673a4f1…`

~~~~text
47: PHASE MGH2_C4 % 2 1 2 !
48: CONST MGH2_C4 : MG : H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0360-3199(98)00132-3](https://doi.org/10.1016/S0360-3199%2898%2900132-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, Int. J. Hydrogen Energy, 24, 989-1004(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.04.005](https://doi.org/10.1016/j.calphad.2007.04.005) M. Palumbo, F.J. Torres, J.R. Ares, C. Pisani, J.F. Fernandez, M. Baricco, Thermodynamic and ab initio investigation of the Al–H–Mg system, Calphad 31, 457-467 (2007).  
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
