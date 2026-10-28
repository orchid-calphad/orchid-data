# In–Mn phases

> In–Mn system: 8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-MN.html · Markdown: https://data.orchid-project.org/phases/pages/IN-MN.md

8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-MN) · [full JSON](https://data.orchid-project.org/phases/systems/IN-MN.json) · [In–Mn system page](https://data.orchid-project.org/systems/IN-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Mn system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-mn-a6-tetragonal); _phase:in-mn:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.6 K, x(Mn) 0–0 | 3 | 1 |
| [BCC_A2](#phase-in-mn-bcc-a2); _phase:in-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1366.01–2498.99 K, x(Mn) 0.98942–1 | 3 | 1 |
| [CBCC_A12](#phase-in-mn-cbcc-a12); _phase:in-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1355 K, x(Mn) 0.98687–1 | 3 | 1 |
| [CUB_A13](#phase-in-mn-cub-a13); _phase:in-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 908–1359.99 K, x(Mn) 0.91042–1 | 11 | 1 |
| [FCC_A1](#phase-in-mn-fcc-a1); _phase:in-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1293.26–1466.33 K, x(Mn) 0.92218–1 | 5 | 1 |
| [HCP_A3](#phase-in-mn-hcp-a3); _phase:in-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [INMN3_D83](#phase-in-mn-inmn3-d83); _phase:in-mn:inmn3-d83_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1181.8 K, x(Mn) 0.75–0.75 | 10 | 1 |
| [LIQUID](#phase-in-mn-liquid); _phase:in-mn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.6–2500 K, x(Mn) 0–1 | 28 | 1 |

## TETRAGONAL_A6 (In–Mn)

- Id: `phase:in-mn:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.6 K, x(Mn) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:a6-tetragonal)

Names (4): _corpus: _corpus:phase:in-mn:a6-tetragonal, corpus:phase:in-mn:tetragonal-a6  
_paper: _paper:10.1016/j.tca.2015.03.022:(In)  
_tdb: _tdb:InMn-15Wan.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): TETRAGONAL_A6, type code %, sha256 `213bd22e68c918e1…`

~~~~text
43: PHASE TETRAGONAL_A6 % 1 1 !
44: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (In–Mn)

- Id: `phase:in-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1366.01–2498.99 K, x(Mn) 0.98942–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:bcc-a2)

Names (3): _corpus: _corpus:phase:in-mn:bcc-a2  
_paper: _paper:10.1016/j.tca.2015.03.022:δ-Mn  
_tdb: _tdb:InMn-15Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): BCC_A2, type code %B, sha256 `213bd22e68c918e1…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : IN MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase; reports values for this phase_

## CBCC_A12 (In–Mn)

- Id: `phase:in-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1355 K, x(Mn) 0.98687–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:cbcc-a12)

Names (3): _corpus: _corpus:phase:in-mn:cbcc-a12  
_paper: _paper:10.1016/j.tca.2015.03.022:α-Mn  
_tdb: _tdb:InMn-15Wan.tdb:CBCC_A12  


### TDB models of CBCC_A12 (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): CBCC_A12, type code %, sha256 `213bd22e68c918e1…`

~~~~text
48: PHASE CBCC_A12 % 2 1 1 !
49: CONST CBCC_A12 : IN MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase; reports values for this phase_

## CUB_A13 (In–Mn)

- Id: `phase:in-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 908–1359.99 K, x(Mn) 0.91042–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:cub-a13)

Names (3): _corpus: _corpus:phase:in-mn:cub-a13  
_paper: _paper:10.1016/j.tca.2015.03.022:β-Mn  
_tdb: _tdb:InMn-15Wan.tdb:CUB_A13  


### TDB models of CUB_A13 (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): CUB_A13, type code %, sha256 `213bd22e68c918e1…`

~~~~text
53: PHASE CUB_A13 % 2 1 1 !
54: CONST CUB_A13 : IN MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (In–Mn)

- Id: `phase:in-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1293.26–1466.33 K, x(Mn) 0.92218–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:fcc-a1)

Names (3): _corpus: _corpus:phase:in-mn:fcc-a1  
_paper: _paper:10.1016/j.tca.2015.03.022:γ-Mn  
_tdb: _tdb:InMn-15Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): FCC_A1, type code %A, sha256 `213bd22e68c918e1…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : IN MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (In–Mn)

- Id: `phase:in-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:hcp-a3)

Names (2): _corpus: _corpus:phase:in-mn:hcp-a3  
_tdb: _tdb:InMn-15Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): HCP_A3, type code %A, sha256 `213bd22e68c918e1…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : IN MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase_

## INMN3_D83 (In–Mn)

- Id: `phase:in-mn:inmn3-d83`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D8_3; stoichiometry_contradicts_D8_3:InMn-15Wan.tdb
- Candidate (literature_printed): Al4Cu9 · cP52 — printed with a label mapped to this phase
- Candidate (name_token): Al4Cu9 · D8_3 · cP52 · P-43m (215) — Strukturbericht/word 'D83' in the TDB name
- Candidate (sgte_mmc2): Al4Cu9 · D8_3 · cP52 · P-43m (215) — Hallstedt 2025 mmc2 row for INMN3_D83: InMn3
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — InMn-15Wan.tdb: 'Prototype Al4Cu9 (cP52, P-43m)'
- Stoichiometry: In 0.2500, Mn 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1181.8 K, x(Mn) 0.75–0.75
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:inmn3-d83)

Names (3): _corpus: _corpus:phase:in-mn:inmn3-d83  
_paper: _paper:10.1016/j.tca.2015.03.022:InMn3  
_tdb: _tdb:InMn-15Wan.tdb:INMN3_D83  


### TDB models of INMN3_D83 (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): INMN3_D83, type code %, sha256 `213bd22e68c918e1…`

~~~~text
58: PHASE INMN3_D83 % 2 1 3 !
59: CONST INMN3_D83 : IN : MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase; reports values for this phase_

## LIQUID (In–Mn)

- Id: `phase:in-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.6–2500 K, x(Mn) 0–1
- Literature: 28 values (28 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-mn:liquid)

Names (4): _corpus: _corpus:phase:in-mn:liquid  
_paper: _paper:10.1016/j.tca.2015.03.022:L, paper:10.1016/j.tca.2015.03.022:liquid  
_tdb: _tdb:InMn-15Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InMn-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb): LIQUID, type code %, sha256 `213bd22e68c918e1…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : IN MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
