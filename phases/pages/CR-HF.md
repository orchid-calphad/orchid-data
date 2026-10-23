# Cr–Hf phases

> Cr–Hf system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-HF.html · Markdown: https://data.orchid-project.org/phases/pages/CR-HF.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-HF) · [full JSON](https://data.orchid-project.org/phases/systems/CR-HF.json) · [Cr–Hf system page](https://data.orchid-project.org/systems/CR-HF.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-HF.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Hf system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-hf-bcc-a2); _phase:cr-hf:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3271 K, x(Hf) 0–1 | 0 | 2 |
| [C14_LAVES](#phase-cr-hf-c14-laves); _phase:cr-hf:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1580.01–2100.54 K, x(Hf) 0.33326–0.35856 | 0 | 2 |
| [C15_LAVES](#phase-cr-hf-c15-laves); _phase:cr-hf:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1595.6 K, x(Hf) 0.3332–0.35387 | 0 | 2 |
| [FCC_A1](#phase-cr-hf-fcc-a1); _phase:cr-hf:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-cr-hf-hcp-a3); _phase:cr-hf:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2171.02 K, x(Hf) 0.97669–1 | 0 | 2 |
| [LIQUID](#phase-cr-hf-liquid); _phase:cr-hf:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1774.22–4000 K, x(Hf) 0–1 | 0 | 2 |

## BCC_A2 (Cr–Hf)

- Id: `phase:cr-hf:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3271 K, x(Hf) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-hf:bcc-a2)

Names (3): _corpus: _corpus:phase:cr-hf:bcc-a2  
_tdb: _tdb:CrHf-10Pav-3SL.tdb:BCC_A2, tdb:CrHf-10Pav.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CrHf-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav-3SL.tdb): BCC_A2, type code %B, sha256 `2f6ed12b7f156a64…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CR% HF% : VA : !
~~~~

[CrHf-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav.tdb): BCC_A2, type code %B, sha256 `8556f8a49f653998…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CR% HF% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## C14_LAVES (Cr–Hf)

- Id: `phase:cr-hf:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrHf-10Pav-3SL.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrHf-10Pav.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 1580.01–2100.54 K, x(Hf) 0.33326–0.35856
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-hf:c14-laves)

Names (3): _corpus: _corpus:phase:cr-hf:c14-laves  
_tdb: _tdb:CrHf-10Pav-3SL.tdb:C14_LAVES, tdb:CrHf-10Pav.tdb:C14_LAVES  


### TDB models of C14_LAVES (2): PHASE and CONSTITUENT statements as written

[CrHf-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav-3SL.tdb): C14_LAVES, type code %, sha256 `2f6ed12b7f156a64…`

~~~~text
43: PHASE C14_LAVES % 3 2 4 6 !
44: CONST C14_LAVES : CR : CR HF : CR HF : !
~~~~

[CrHf-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav.tdb): C14_LAVES, type code %, sha256 `8556f8a49f653998…`

~~~~text
47: PHASE C14_LAVES % 2 2 1 !
48: CONST C14_LAVES : CR HF : CR HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## C15_LAVES (Cr–Hf)

- Id: `phase:cr-hf:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrHf-10Pav-3SL.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrHf-10Pav.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1595.6 K, x(Hf) 0.3332–0.35387
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-hf:c15-laves)

Names (3): _corpus: _corpus:phase:cr-hf:c15-laves  
_tdb: _tdb:CrHf-10Pav-3SL.tdb:C15_LAVES, tdb:CrHf-10Pav.tdb:C15_LAVES  


### TDB models of C15_LAVES (2): PHASE and CONSTITUENT statements as written

[CrHf-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav-3SL.tdb): C15_LAVES, type code %, sha256 `2f6ed12b7f156a64…`

~~~~text
48: PHASE C15_LAVES % 2 2 1 !
49: CONST C15_LAVES : CR HF : CR HF : !
~~~~

[CrHf-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav.tdb): C15_LAVES, type code %, sha256 `8556f8a49f653998…`

~~~~text
52: PHASE C15_LAVES % 2 2 1 !
53: CONST C15_LAVES : CR HF : CR HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## FCC_A1 (Cr–Hf)

- Id: `phase:cr-hf:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-hf:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-hf:fcc-a1  
_tdb: _tdb:CrHf-10Pav-3SL.tdb:FCC_A1, tdb:CrHf-10Pav.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CrHf-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav-3SL.tdb): FCC_A1, type code %A, sha256 `2f6ed12b7f156a64…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CR HF : VA : !
~~~~

[CrHf-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav.tdb): FCC_A1, type code %A, sha256 `8556f8a49f653998…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CR HF : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## HCP_A3 (Cr–Hf)

- Id: `phase:cr-hf:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2171.02 K, x(Hf) 0.97669–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-hf:hcp-a3)

Names (3): _corpus: _corpus:phase:cr-hf:hcp-a3  
_tdb: _tdb:CrHf-10Pav-3SL.tdb:HCP_A3, tdb:CrHf-10Pav.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CrHf-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav-3SL.tdb): HCP_A3, type code %A, sha256 `2f6ed12b7f156a64…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CR HF% : VA : !
~~~~

[CrHf-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav.tdb): HCP_A3, type code %A, sha256 `8556f8a49f653998…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CR HF% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
_assessment that models this phase_

## LIQUID (Cr–Hf)

- Id: `phase:cr-hf:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1774.22–4000 K, x(Hf) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-hf:liquid)

Names (3): _corpus: _corpus:phase:cr-hf:liquid  
_tdb: _tdb:CrHf-10Pav-3SL.tdb:LIQUID, tdb:CrHf-10Pav.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CrHf-10Pav-3SL.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav-3SL.tdb): LIQUID, type code %, sha256 `2f6ed12b7f156a64…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CR HF : !
~~~~

[CrHf-10Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/CrHf-10Pav.tdb): LIQUID, type code %, sha256 `8556f8a49f653998…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CR HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.03.003](https://doi.org/10.1016/j.calphad.2010.03.003) J. Pavlů, J. Vřešt’ál, M. Šob, Thermodynamic modeling of Laves phases in the Cr–Hf and Cr–Ti systems: Reassessment using first-principles results, Calphad 34, 215-221 (2010).  
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
