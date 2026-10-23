# Cu–Ir phases

> Cu–Ir system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-IR.html · Markdown: https://data.orchid-project.org/phases/pages/CU-IR.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-IR) · [full JSON](https://data.orchid-project.org/phases/systems/CU-IR.json) · [Cu–Ir system page](https://data.orchid-project.org/systems/CU-IR.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-IR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Ir system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-ir-bcc-a2); _phase:cu-ir:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-cu-ir-fcc-a1); _phase:cu-ir:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999 K, x(Ir) 0–1 | 0 | 2 |
| [HCP_A3](#phase-cu-ir-hcp-a3); _phase:cu-ir:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cu-ir-liquid); _phase:cu-ir:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1332.77–4000 K, x(Ir) 0–1 | 10 | 2 |

## BCC_A2 (Cu–Ir)

- Id: `phase:cu-ir:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ir:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-ir:bcc-a2  
_tdb: _tdb:CuIr-04Kor-LB.tdb:BCC_A2, tdb:CuIr-87Cha.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuIr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-04Kor-LB.tdb): BCC_A2, type code %B, sha256 `bc7d8e92a01c7ed0…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU IR : VA : !
~~~~

[CuIr-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-87Cha.tdb): BCC_A2, type code %B, sha256 `f9fe888f4dc6f8ff…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CU IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873198](https://doi.org/10.1007/BF02873198) D.J. Chakrabarti, D.E. Laughlin, Bull. Alloy Phase Diag., 8, 132-36(1987).  
_assessment that models this phase_

## FCC_A1 (Cu–Ir)

- Id: `phase:cu-ir:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999 K, x(Ir) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ir:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-ir:fcc-a1  
_tdb: _tdb:CuIr-04Kor-LB.tdb:FCC_A1, tdb:CuIr-87Cha.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuIr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-04Kor-LB.tdb): FCC_A1, type code %A, sha256 `bc7d8e92a01c7ed0…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU IR : VA : !
~~~~

[CuIr-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-87Cha.tdb): FCC_A1, type code %A, sha256 `f9fe888f4dc6f8ff…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CU IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873198](https://doi.org/10.1007/BF02873198) D.J. Chakrabarti, D.E. Laughlin, Bull. Alloy Phase Diag., 8, 132-36(1987).  
_assessment that models this phase_

## HCP_A3 (Cu–Ir)

- Id: `phase:cu-ir:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ir:hcp-a3)

Names (3): _corpus: _corpus:phase:cu-ir:hcp-a3  
_tdb: _tdb:CuIr-04Kor-LB.tdb:HCP_A3, tdb:CuIr-87Cha.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuIr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-04Kor-LB.tdb): HCP_A3, type code %A, sha256 `bc7d8e92a01c7ed0…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU IR : VA : !
~~~~

[CuIr-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-87Cha.tdb): HCP_A3, type code %A, sha256 `f9fe888f4dc6f8ff…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CU IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873198](https://doi.org/10.1007/BF02873198) D.J. Chakrabarti, D.E. Laughlin, Bull. Alloy Phase Diag., 8, 132-36(1987).  
_assessment that models this phase_

## LIQUID (Cu–Ir)

- Id: `phase:cu-ir:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1332.77–4000 K, x(Ir) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ir:liquid)

Names (4): _corpus: _corpus:phase:cu-ir:liquid  
_paper: _paper:10.1007/bf02873198:L  
_tdb: _tdb:CuIr-04Kor-LB.tdb:LIQUID, tdb:CuIr-87Cha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuIr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-04Kor-LB.tdb): LIQUID, type code %, sha256 `bc7d8e92a01c7ed0…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU IR : !
~~~~

[CuIr-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuIr-87Cha.tdb): LIQUID, type code %, sha256 `f9fe888f4dc6f8ff…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CU IR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873198](https://doi.org/10.1007/BF02873198) D.J. Chakrabarti, D.E. Laughlin, Bull. Alloy Phase Diag., 8, 132-36(1987).  
_assessment that models this phase; reports values for this phase_

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
