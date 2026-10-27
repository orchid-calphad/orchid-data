# S–Zn phases

> S–Zn system: 9 phases (tier A 6, liquid 1, gas 1, needs_review 1); 0 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/S-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/S-ZN.md

9 phases (tier A 6, liquid 1, gas 1, needs_review 1); 0 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=S-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/S-ZN.json) · [Markdown](https://data.orchid-project.org/phases/pages/S-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the S–Zn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-s-zn-a16-orthorhombic); _phase:s-zn:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [BCC_A2](#phase-s-zn-bcc-a2); _phase:s-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [FCC_A1](#phase-s-zn-fcc-a1); _phase:s-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [GAS](#phase-s-zn-gas); _phase:s-zn:gas_ | gas | gas | no calculated diagram | 0 | 1 |
| [HCP_A3](#phase-s-zn-hcp-a3); _phase:s-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [LIQUID](#phase-s-zn-liquid); _phase:s-zn:liquid_ | liquid | liquid | no calculated diagram | 0 | 1 |
| [MONOCLINIC_S](#phase-s-zn-s-monoclinic); _phase:s-zn:s-monoclinic_ |  | needs_review | no calculated diagram | 0 | 1 |
| [ZNS_B3](#phase-s-zn-zns-b3); _phase:s-zn:zns-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [ZNS_B4](#phase-s-zn-zns-b4); _phase:s-zn:zns-b4_ | ZnS (wurtzite) · B4 · hP4 · P6_3mc (186) | tier A: standard phase name | no calculated diagram | 0 | 1 |

## ORTHORHOMBIC_A16 (S–Zn)

- Id: `phase:s-zn:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:s-zn:a16-orthorhombic  
_tdb: _tdb:ZnS-17Gua.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): ORTHORHOMBIC_A16, type code %, sha256 `d2ec903c3b000cae…`

~~~~text
64: PHASE ORTHORHOMBIC_A16 % 1 1 !
65: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## BCC_A2 (S–Zn)

- Id: `phase:s-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Zn 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:bcc-a2)

Names (2): _corpus: _corpus:phase:s-zn:bcc-a2  
_tdb: _tdb:ZnS-17Gua.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): BCC_A2, type code %B, sha256 `d2ec903c3b000cae…`

~~~~text
54: PHASE BCC_A2 %B 2 1 3 !
55: CONST BCC_A2 : ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## FCC_A1 (S–Zn)

- Id: `phase:s-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Zn 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:fcc-a1)

Names (2): _corpus: _corpus:phase:s-zn:fcc-a1  
_tdb: _tdb:ZnS-17Gua.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): FCC_A1, type code %A, sha256 `d2ec903c3b000cae…`

~~~~text
49: PHASE FCC_A1 %A 2 1 1 !
50: CONST FCC_A1 : ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## GAS (S–Zn)

- Id: `phase:s-zn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:gas)

Names (2): _corpus: _corpus:phase:s-zn:gas  
_tdb: _tdb:ZnS-17Gua.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): GAS, type code %, sha256 `d2ec903c3b000cae…`

~~~~text
82: PHASE GAS:G % 1 1 !
83: CONST GAS:G : S S2 S3 S4 S5 S6 S7 S8 ZN ZNS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## HCP_A3 (S–Zn)

- Id: `phase:s-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Zn 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:hcp-a3)

Names (2): _corpus: _corpus:phase:s-zn:hcp-a3  
_tdb: _tdb:ZnS-17Gua.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): HCP_A3, type code %A, sha256 `d2ec903c3b000cae…`

~~~~text
59: PHASE HCP_A3 %A 2 1 0.5 !
60: CONST HCP_A3 : ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## LIQUID (S–Zn)

- Id: `phase:s-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:liquid)

Names (2): _corpus: _corpus:phase:s-zn:liquid  
_tdb: _tdb:ZnS-17Gua.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): LIQUID, type code %, sha256 `d2ec903c3b000cae…`

~~~~text
44: PHASE LIQUID:L % 1 1 !
45: CONST LIQUID:L : S ZN ZNS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## MONOCLINIC_S (S–Zn)

- Id: `phase:s-zn:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — ZnS-17Gua.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:s-monoclinic)

Names (2): _corpus: _corpus:phase:s-zn:s-monoclinic  
_tdb: _tdb:ZnS-17Gua.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): MONOCLINIC_S, type code %, sha256 `d2ec903c3b000cae…`

~~~~text
69: PHASE MONOCLINIC_S % 1 1 !
70: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## ZNS_B3 (S–Zn)

- Id: `phase:s-zn:zns-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:zns-b3)

Names (2): _corpus: _corpus:phase:s-zn:zns-b3  
_tdb: _tdb:ZnS-17Gua.tdb:ZNS_B3  


### TDB models of ZNS_B3 (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): ZNS_B3, type code %, sha256 `d2ec903c3b000cae…`

~~~~text
74: PHASE ZNS_B3:I % 2 1 1 !
75: CONST ZNS_B3:I : ZNS ZN ZN+2 S-2 ZN2S+2 : VA VA-1 VA+1 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
_assessment that models this phase_

## ZNS_B4 (S–Zn)

- Id: `phase:s-zn:zns-b4`; status `assigned`
- Structure: ZnS (wurtzite) · B4 · hP4 · P6_3mc (186); type `st:b4-zns-wurtzite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: S 0.5000, Zn 0.5000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-zn:zns-b4)

Names (2): _corpus: _corpus:phase:s-zn:zns-b4  
_tdb: _tdb:ZnS-17Gua.tdb:ZNS_B4  


### TDB models of ZNS_B4 (1): PHASE and CONSTITUENT statements as written

[ZnS-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnS-17Gua.tdb): ZNS_B4, type code %, sha256 `d2ec903c3b000cae…`

~~~~text
79: PHASE ZNS_B4 % 2 1 1 !
80: CONST ZNS_B4 : ZN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.10.006](https://doi.org/10.1016/j.calphad.2017.10.006) Calphad, 59, 171-81(2017).  
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
