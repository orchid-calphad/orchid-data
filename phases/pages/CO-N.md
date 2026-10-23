# Co–N phases

> Co–N system: 6 phases (tier A 3, tier C 1, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-N.html · Markdown: https://data.orchid-project.org/phases/pages/CO-N.md

6 phases (tier A 3, tier C 1, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-N) · [full JSON](https://data.orchid-project.org/phases/systems/CO-N.json) · [Co–N system page](https://data.orchid-project.org/systems/CO-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–N system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-n-bcc-a2); _phase:co-n:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CO4N_L1](#phase-co-n-co4n-l1); _phase:co-n:co4n-l1_ | Fe4N · L'1 · cP5 · Pm-3m (221) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-co-n-fcc-a1); _phase:co-n:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 695.36–1769.74 K, x(N) 0–3e-05 | 0 | 1 |
| [HCP_A3](#phase-co-n-hcp-a3); _phase:co-n:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–695.36 K, x(N) 0–4e-05 | 0 | 1 |
| [LIQUID](#phase-co-n-liquid); _phase:co-n:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1767.74–2500 K, x(N) 0–0.00029 | 0 | 1 |
| [N2GAS](#phase-co-n-n2gas); _phase:co-n:n2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(N) 1–1 | 0 | 1 |

## BCC_A2 (Co–N)

- Id: `phase:co-n:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-n:bcc-a2)

Names (2): _corpus: _corpus:phase:co-n:bcc-a2  
_tdb: _tdb:CoN-92Fer-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoN-92Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoN-92Fer-LB.tdb): BCC_A2, type code %B, sha256 `61cf1466a7997e36…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CO : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830107](https://doi.org/10.1515/ijmr-1992-830107) A. Fernandez Guillermet, S. Jonsson, Z. Metallkd., 83, 21-31(1992).  
_assessment that models this phase_

## CO4N_L1 (Co–N)

- Id: `phase:co-n:co4n-l1`; status `assigned`
- Structure: Fe4N · L'1 · cP5 · Pm-3m (221); type `st:l-1-fe4n-cp5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:L1, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.8000, N 0.2000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-n:co4n-l1)

Names (2): _corpus: _corpus:phase:co-n:co4n-l1  
_tdb: _tdb:CoN-92Fer-LB.tdb:CO4N_L1  


### TDB models of CO4N_L1 (1): PHASE and CONSTITUENT statements as written

[CoN-92Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoN-92Fer-LB.tdb): CO4N_L1, type code %, sha256 `61cf1466a7997e36…`

~~~~text
45: PHASE CO4N_L1 % 2 4 1 !
46: CONST CO4N_L1 : CO : N :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830107](https://doi.org/10.1515/ijmr-1992-830107) A. Fernandez Guillermet, S. Jonsson, Z. Metallkd., 83, 21-31(1992).  
_assessment that models this phase_

## FCC_A1 (Co–N)

- Id: `phase:co-n:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 695.36–1769.74 K, x(N) 0–3e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-n:fcc-a1)

Names (2): _corpus: _corpus:phase:co-n:fcc-a1  
_tdb: _tdb:CoN-92Fer-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoN-92Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoN-92Fer-LB.tdb): FCC_A1, type code %A, sha256 `61cf1466a7997e36…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CO : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830107](https://doi.org/10.1515/ijmr-1992-830107) A. Fernandez Guillermet, S. Jonsson, Z. Metallkd., 83, 21-31(1992).  
_assessment that models this phase_

## HCP_A3 (Co–N)

- Id: `phase:co-n:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–695.36 K, x(N) 0–4e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-n:hcp-a3)

Names (2): _corpus: _corpus:phase:co-n:hcp-a3  
_tdb: _tdb:CoN-92Fer-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoN-92Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoN-92Fer-LB.tdb): HCP_A3, type code %A, sha256 `61cf1466a7997e36…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CO : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830107](https://doi.org/10.1515/ijmr-1992-830107) A. Fernandez Guillermet, S. Jonsson, Z. Metallkd., 83, 21-31(1992).  
_assessment that models this phase_

## LIQUID (Co–N)

- Id: `phase:co-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1767.74–2500 K, x(N) 0–0.00029
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-n:liquid)

Names (2): _corpus: _corpus:phase:co-n:liquid  
_tdb: _tdb:CoN-92Fer-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoN-92Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoN-92Fer-LB.tdb): LIQUID, type code %, sha256 `61cf1466a7997e36…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CO N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830107](https://doi.org/10.1515/ijmr-1992-830107) A. Fernandez Guillermet, S. Jonsson, Z. Metallkd., 83, 21-31(1992).  
_assessment that models this phase_

## N2GAS (Co–N)

- Id: `phase:co-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-n:n2gas)

Names (2): _corpus: _corpus:phase:co-n:n2gas  
_tdb: _tdb:CoN-92Fer-LB.tdb:N2GAS  


### TDB models of N2GAS (1): PHASE and CONSTITUENT statements as written

[CoN-92Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoN-92Fer-LB.tdb): N2GAS, type code %, sha256 `61cf1466a7997e36…`

~~~~text
48: PHASE N2GAS % 1 1 !
49: CONST N2GAS : N2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830107](https://doi.org/10.1515/ijmr-1992-830107) A. Fernandez Guillermet, S. Jonsson, Z. Metallkd., 83, 21-31(1992).  
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
