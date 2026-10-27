# Ge–Si phases

> Ge–Si system: 5 phases (tier A 4, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-SI.html · Markdown: https://data.orchid-project.org/phases/pages/GE-SI.md

5 phases (tier A 4, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-SI) · [full JSON](https://data.orchid-project.org/phases/systems/GE-SI.json) · [Ge–Si system page](https://data.orchid-project.org/systems/GE-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Si system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-si-a4-diamond); _phase:ge-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.5 K, x(Si) 0–1 | 0 | 2 |
| [BCC_A2](#phase-ge-si-bcc-a2); _phase:ge-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ge-si-fcc-a1); _phase:ge-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ge-si-hcp-a3); _phase:ge-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ge-si-liquid); _phase:ge-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1211.4–2500 K, x(Si) 0–1 | 31 | 2 |

## DIAMOND_A4 (Ge–Si)

- Id: `phase:ge-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.5 K, x(Si) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-si:a4-diamond)

Names (3): _corpus: _corpus:phase:ge-si:a4-diamond  
_tdb: _tdb:GeSi-84Ole.tdb:DIAMOND_A4, tdb:GeSi-92Ber-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GeSi-84Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-84Ole.tdb): DIAMOND_A4, type code %, sha256 `22f65f7d038399c1…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : GE% SI% : !
~~~~

[GeSi-92Ber-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-92Ber-LB.tdb): DIAMOND_A4, type code %, sha256 `f1f9fad361e69cdf…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : GE% SI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667471](https://doi.org/10.1007/BF02667471) C. Bergman, R. Chastel, R. Castanet, J. Phase Equilib., 13, 113-18(1992).  
_assessment that models this phase_
- [doi:10.1007/BF02868957](https://doi.org/10.1007/BF02868957) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 5, 180-83(1984).  
_assessment that models this phase_

## BCC_A2 (Ge–Si)

- Id: `phase:ge-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-si:bcc-a2)

Names (3): _corpus: _corpus:phase:ge-si:bcc-a2  
_tdb: _tdb:GeSi-84Ole.tdb:BCC_A2, tdb:GeSi-92Ber-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GeSi-84Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-84Ole.tdb): BCC_A2, type code %B, sha256 `22f65f7d038399c1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GE SI : VA : !
~~~~

[GeSi-92Ber-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-92Ber-LB.tdb): BCC_A2, type code %B, sha256 `f1f9fad361e69cdf…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : GE SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667471](https://doi.org/10.1007/BF02667471) C. Bergman, R. Chastel, R. Castanet, J. Phase Equilib., 13, 113-18(1992).  
_assessment that models this phase_
- [doi:10.1007/BF02868957](https://doi.org/10.1007/BF02868957) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 5, 180-83(1984).  
_assessment that models this phase_

## FCC_A1 (Ge–Si)

- Id: `phase:ge-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-si:fcc-a1)

Names (3): _corpus: _corpus:phase:ge-si:fcc-a1  
_tdb: _tdb:GeSi-84Ole.tdb:FCC_A1, tdb:GeSi-92Ber-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GeSi-84Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-84Ole.tdb): FCC_A1, type code %A, sha256 `22f65f7d038399c1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GE SI : VA : !
~~~~

[GeSi-92Ber-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-92Ber-LB.tdb): FCC_A1, type code %A, sha256 `f1f9fad361e69cdf…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : GE SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667471](https://doi.org/10.1007/BF02667471) C. Bergman, R. Chastel, R. Castanet, J. Phase Equilib., 13, 113-18(1992).  
_assessment that models this phase_
- [doi:10.1007/BF02868957](https://doi.org/10.1007/BF02868957) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 5, 180-83(1984).  
_assessment that models this phase_

## HCP_A3 (Ge–Si)

- Id: `phase:ge-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-si:hcp-a3)

Names (3): _corpus: _corpus:phase:ge-si:hcp-a3  
_tdb: _tdb:GeSi-84Ole.tdb:HCP_A3, tdb:GeSi-92Ber-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GeSi-84Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-84Ole.tdb): HCP_A3, type code %A, sha256 `22f65f7d038399c1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GE SI : VA: !
~~~~

[GeSi-92Ber-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-92Ber-LB.tdb): HCP_A3, type code %A, sha256 `f1f9fad361e69cdf…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : GE SI : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667471](https://doi.org/10.1007/BF02667471) C. Bergman, R. Chastel, R. Castanet, J. Phase Equilib., 13, 113-18(1992).  
_assessment that models this phase_
- [doi:10.1007/BF02868957](https://doi.org/10.1007/BF02868957) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 5, 180-83(1984).  
_assessment that models this phase_

## LIQUID (Ge–Si)

- Id: `phase:ge-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1211.4–2500 K, x(Si) 0–1
- Literature: 31 values (31 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-si:liquid)

Names (4): _corpus: _corpus:phase:ge-si:liquid  
_paper: _paper:10.1007/bf02667471:liquid  
_tdb: _tdb:GeSi-84Ole.tdb:LIQUID, tdb:GeSi-92Ber-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GeSi-84Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-84Ole.tdb): LIQUID, type code %, sha256 `22f65f7d038399c1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GE SI : !
~~~~

[GeSi-92Ber-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSi-92Ber-LB.tdb): LIQUID, type code %, sha256 `f1f9fad361e69cdf…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : GE SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667471](https://doi.org/10.1007/BF02667471) C. Bergman, R. Chastel, R. Castanet, J. Phase Equilib., 13, 113-18(1992).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02868957](https://doi.org/10.1007/BF02868957) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 5, 180-83(1984).  
_assessment that models this phase_

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
