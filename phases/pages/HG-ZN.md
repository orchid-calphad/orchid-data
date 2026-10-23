# Hg–Zn phases

> Hg–Zn system: 8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HG-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/HG-ZN.md

8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HG-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/HG-ZN.json) · [Hg–Zn system page](https://data.orchid-project.org/systems/HG-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/HG-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hg–Zn system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBO_A10](#phase-hg-zn-a10-rhombo); _phase:hg-zn:a10-rhombo_ | alpha-Hg · A10 · hR1 · R-3m (166) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-hg-zn-bcc-a2); _phase:hg-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-hg-zn-fcc-a1); _phase:hg-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-hg-zn-hcp-a3); _phase:hg-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–692.68 K, x(Zn) 0.95854–1 | 0 | 1 |
| [HG3ZN](#phase-hg-zn-hg3zn); _phase:hg-zn:hg3zn_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HGZN2](#phase-hg-zn-hgzn2); _phase:hg-zn:hgzn2_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HGZN3](#phase-hg-zn-hgzn3); _phase:hg-zn:hgzn3_ | Cu3Ti · oC4 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–315.63 K, x(Zn) 0.75–0.75 | 0 | 1 |
| [LIQUID](#phase-hg-zn-liquid); _phase:hg-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Zn) 0–1 | 0 | 1 |

## RHOMBO_A10 (Hg–Zn)

- Id: `phase:hg-zn:a10-rhombo`; status `assigned`
- Structure: alpha-Hg · A10 · hR1 · R-3m (166); type `st:a10-alpha-hg-hr1`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:a10-rhombo)

Names (2): _corpus: _corpus:phase:hg-zn:a10-rhombo  
_tdb: _tdb:HgZn-98Han-LB.tdb:RHOMBO_A10  


### TDB models of RHOMBO_A10 (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): RHOMBO_A10, type code %, sha256 `bc1b12ff7603ad23…`

~~~~text
40: PHASE RHOMBO_A10 % 1 1 !
41: CONST RHOMBO_A10 : HG% ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## BCC_A2 (Hg–Zn)

- Id: `phase:hg-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Zn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:bcc-a2)

Names (2): _corpus: _corpus:phase:hg-zn:bcc-a2  
_tdb: _tdb:HgZn-98Han-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): BCC_A2, type code %B, sha256 `bc1b12ff7603ad23…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## FCC_A1 (Hg–Zn)

- Id: `phase:hg-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:fcc-a1)

Names (2): _corpus: _corpus:phase:hg-zn:fcc-a1  
_tdb: _tdb:HgZn-98Han-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): FCC_A1, type code %A, sha256 `bc1b12ff7603ad23…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : HG ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## HCP_A3 (Hg–Zn)

- Id: `phase:hg-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–692.68 K, x(Zn) 0.95854–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:hcp-a3)

Names (2): _corpus: _corpus:phase:hg-zn:hcp-a3  
_tdb: _tdb:HgZn-98Han-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): HCP_A3, type code %A, sha256 `bc1b12ff7603ad23…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : HG ZN% : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## HG3ZN (Hg–Zn)

- Id: `phase:hg-zn:hg3zn`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Hg3Zn) — Hallstedt 2025 mmc2 row for HG3ZN: Hg3Zn
- Stoichiometry: Hg 0.7500, Zn 0.2500
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:hg3zn)

Names (2): _corpus: _corpus:phase:hg-zn:hg3zn  
_tdb: _tdb:HgZn-98Han-LB.tdb:HG3ZN  


### TDB models of HG3ZN (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): HG3ZN, type code %, sha256 `bc1b12ff7603ad23…`

~~~~text
45: PHASE HG3ZN % 2 3 1 !
46: CONST HG3ZN : HG : ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## HGZN2 (Hg–Zn)

- Id: `phase:hg-zn:hgzn2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (HgZn2) — Hallstedt 2025 mmc2 row for HGZN2: HgZn2
- Stoichiometry: Hg 0.3333, Zn 0.6667
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:hgzn2)

Names (2): _corpus: _corpus:phase:hg-zn:hgzn2  
_tdb: _tdb:HgZn-98Han-LB.tdb:HGZN2  


### TDB models of HGZN2 (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): HGZN2, type code %, sha256 `bc1b12ff7603ad23…`

~~~~text
50: PHASE HGZN2 % 2 1 2 !
51: CONST HGZN2 : HG : ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## HGZN3 (Hg–Zn)

- Id: `phase:hg-zn:hgzn3`; status `assigned`
- Structure: Cu3Ti · oC4 · Cmcm (63); type `st:cu3ti-oc4`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hg 0.2500, Zn 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–315.63 K, x(Zn) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:hgzn3)

Names (2): _corpus: _corpus:phase:hg-zn:hgzn3  
_tdb: _tdb:HgZn-98Han-LB.tdb:HGZN3  


### TDB models of HGZN3 (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): HGZN3, type code %, sha256 `bc1b12ff7603ad23…`

~~~~text
55: PHASE HGZN3 % 2 1 3 !
56: CONST HGZN3 : HG : ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## LIQUID (Hg–Zn)

- Id: `phase:hg-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Zn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-zn:liquid)

Names (2): _corpus: _corpus:phase:hg-zn:liquid  
_tdb: _tdb:HgZn-98Han-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HgZn-98Han-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgZn-98Han-LB.tdb): LIQUID, type code %, sha256 `bc1b12ff7603ad23…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : HG ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
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
