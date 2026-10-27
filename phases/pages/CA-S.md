# Ca–S phases

> Ca–S system: 8 phases (tier A 4, liquid 2, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-S.html · Markdown: https://data.orchid-project.org/phases/pages/CA-S.md

8 phases (tier A 4, liquid 2, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-S) · [full JSON](https://data.orchid-project.org/phases/systems/CA-S.json) · [Ca–S system page](https://data.orchid-project.org/systems/CA-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–S system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-s-bcc-a2); _phase:ca-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1112–1115 K, x(S) 0–0 | 0 | 1 |
| [CAS_B1](#phase-ca-s-cas-b1); _phase:ca-s:cas-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505 K, x(S) 0.5–0.5 | 0 | 1 |
| [FCC_A1](#phase-ca-s-fcc-a1); _phase:ca-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505 K, x(S) 0–0 | 0 | 1 |
| [HCP_A3](#phase-ca-s-hcp-a3); _phase:ca-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-ca-s-ion); _phase:ca-s:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1112–1115 K, x(S) 0–0.00249 | 0 | 1 |
| [LIQUID](#phase-ca-s-liquid); _phase:ca-s:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |
| [MONOCLINIC_S](#phase-ca-s-s-monoclinic); _phase:ca-s:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ORTHORHOMBIC_S](#phase-ca-s-s-orthorhombic); _phase:ca-s:s-orthorhombic_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–375 K, x(S) 1–1 | 0 | 1 |

## BCC_A2 (Ca–S)

- Id: `phase:ca-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1112–1115 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:bcc-a2)

Names (2): _corpus: _corpus:phase:ca-s:bcc-a2  
_tdb: _tdb:CaS-16Dil.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): BCC_A2, type code %B, sha256 `5f8df58bbc3c6087…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : CA% S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
_assessment that models this phase_

## CAS_B1 (Ca–S)

- Id: `phase:ca-s:cas-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–505 K, x(S) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:cas-b1)

Names (2): _corpus: _corpus:phase:ca-s:cas-b1  
_tdb: _tdb:CaS-16Dil.tdb:CAS_B1  


### TDB models of CAS_B1 (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): CAS_B1, type code %, sha256 `5f8df58bbc3c6087…`

~~~~text
63: PHASE CAS_B1:I % 2 1 1 !
64: CONST CAS_B1:I : CA+2 : S-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
_assessment that models this phase_

## FCC_A1 (Ca–S)

- Id: `phase:ca-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–505 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:fcc-a1)

Names (2): _corpus: _corpus:phase:ca-s:fcc-a1  
_tdb: _tdb:CaS-16Dil.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): FCC_A1, type code %A, sha256 `5f8df58bbc3c6087…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : CA% S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
_assessment that models this phase_

## HCP_A3 (Ca–S)

- Id: `phase:ca-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-s:hcp-a3  
_tdb: _tdb:CaS-16Dil.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): HCP_A3, type code %A, sha256 `5f8df58bbc3c6087…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : CA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
_assessment that models this phase_

## ION (Ca–S)

- Id: `phase:ca-s:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1112–1115 K, x(S) 0–0.00249
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:ion)

Names (2): _corpus: _corpus:phase:ca-s:ion  
_tdb: _tdb:CaS-16Dil.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): ION, type code %, sha256 `5f8df58bbc3c6087…`

~~~~text
30: PHASE ION:Y % 2 1 1 !
31: CONST ION:Y : CA+2 : S-2 VA S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
_assessment that models this phase_

## LIQUID (Ca–S)

- Id: `phase:ca-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Ca 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:liquid)

Names (2): _corpus: _corpus:phase:ca-s:liquid  
_tdb: _tdb:CaS-16Dil.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): LIQUID, type code %, sha256 `5f8df58bbc3c6087…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : CA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
_assessment that models this phase_

## MONOCLINIC_S (Ca–S)

- Id: `phase:ca-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — CaS-16Dil.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:s-monoclinic)

Names (2): _corpus: _corpus:phase:ca-s:s-monoclinic  
_tdb: _tdb:CaS-16Dil.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): MONOCLINIC_S, type code %, sha256 `5f8df58bbc3c6087…`

~~~~text
58: PHASE MONOCLINIC_S % 1 1 !
59: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
_assessment that models this phase_

## ORTHORHOMBIC_S (Ca–S)

- Id: `phase:ca-s:s-orthorhombic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:ORTHORHOMBIC; no_structure_token
- Candidate (sgte_mmc2): alpha-S · A16 · oF128 · Fddd (70) — Hallstedt 2025 mmc2 row for ORTHORHOMBIC_S: alpha-S
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — CaS-16Dil.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–375 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-s:s-orthorhombic)

Names (2): _corpus: _corpus:phase:ca-s:s-orthorhombic  
_tdb: _tdb:CaS-16Dil.tdb:ORTHORHOMBIC_S  


### TDB models of ORTHORHOMBIC_S (1): PHASE and CONSTITUENT statements as written

[CaS-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaS-16Dil.tdb): ORTHORHOMBIC_S, type code %, sha256 `5f8df58bbc3c6087…`

~~~~text
53: PHASE ORTHORHOMBIC_S % 1 1 !
54: CONST ORTHORHOMBIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2) David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016).  
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
