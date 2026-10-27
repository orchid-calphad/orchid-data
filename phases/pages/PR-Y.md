# Pr–Y phases

> Pr–Y system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PR-Y.html · Markdown: https://data.orchid-project.org/phases/pages/PR-Y.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PR-Y) · [full JSON](https://data.orchid-project.org/phases/systems/PR-Y.json) · [Pr–Y system page](https://data.orchid-project.org/systems/PR-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/PR-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pr–Y system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pr-y-bcc-a2); _phase:pr-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1068–2499 K, x(Y) 0–1 | 1 | 1 |
| [DHCP](#phase-pr-y-dhcp-a3); _phase:pr-y:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1277.55 K, x(Y) 0–0.31523 | 3 | 1 |
| [FCC_A1](#phase-pr-y-fcc-a1); _phase:pr-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-pr-y-hcp-a3); _phase:pr-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 0.3311–1 | 3 | 1 |
| [LIQUID](#phase-pr-y-liquid); _phase:pr-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1200.15–2500 K, x(Y) 0–1 | 0 | 1 |
| [PR2Y_C19](#phase-pr-y-pr2y-c19); _phase:pr-y:pr2y-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–846.52 K, x(Y) 0.32128–0.33332 | 2 | 1 |

## BCC_A2 (Pr–Y)

- Id: `phase:pr-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1068–2499 K, x(Y) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-y:bcc-a2)

Names (3): _corpus: _corpus:phase:pr-y:bcc-a2  
_paper: _paper:10.1016/j.calphad.2007.05.007:bcc  
_tdb: _tdb:PrY-08Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PrY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb): BCC_A2, type code %B, sha256 `e55017ddbbde8b1a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : PR Y : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; reports values for this phase_

## DHCP (Pr–Y)

- Id: `phase:pr-y:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1277.55 K, x(Y) 0–0.31523
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-y:dhcp-a3)

Names (4): _corpus: _corpus:phase:pr-y:dhcp-a3, corpus:phase:pr-y:dhcp  
_paper: _paper:10.1016/j.calphad.2007.05.007:dhcp  
_tdb: _tdb:PrY-08Guo.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[PrY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb): DHCP, type code %A, sha256 `e55017ddbbde8b1a…`

~~~~text
40: PHASE DHCP %A 1 1 !
41: CONST DHCP : PR% Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Pr–Y)

- Id: `phase:pr-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-y:fcc-a1)

Names (2): _corpus: _corpus:phase:pr-y:fcc-a1  
_tdb: _tdb:PrY-08Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PrY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb): FCC_A1, type code %A, sha256 `e55017ddbbde8b1a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : PR Y : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase_

## HCP_A3 (Pr–Y)

- Id: `phase:pr-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 0.3311–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-y:hcp-a3)

Names (3): _corpus: _corpus:phase:pr-y:hcp-a3  
_paper: _paper:10.1016/j.calphad.2007.05.007:hcp  
_tdb: _tdb:PrY-08Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PrY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb): HCP_A3, type code %A, sha256 `e55017ddbbde8b1a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : PR Y% : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Pr–Y)

- Id: `phase:pr-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1200.15–2500 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-y:liquid)

Names (2): _corpus: _corpus:phase:pr-y:liquid  
_tdb: _tdb:PrY-08Guo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PrY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb): LIQUID, type code %, sha256 `e55017ddbbde8b1a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : PR Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase_

## PR2Y_C19 (Pr–Y)

- Id: `phase:pr-y:pr2y-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PrY-08Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–846.52 K, x(Y) 0.32128–0.33332
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-y:pr2y-c19)

Names (3): _corpus: _corpus:phase:pr-y:pr2y-c19  
_paper: _paper:10.1016/j.calphad.2007.05.007:Pr2Y  
_tdb: _tdb:PrY-08Guo.tdb:PR2Y_C19  


### TDB models of PR2Y_C19 (1): PHASE and CONSTITUENT statements as written

[PrY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb): PR2Y_C19, type code %, sha256 `e55017ddbbde8b1a…`

~~~~text
45: PHASE PR2Y_C19 % 2 2 1 !
46: CONST PR2Y_C19 : PR% Y : PR Y% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008).  
_assessment that models this phase; reports values for this phase_

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
