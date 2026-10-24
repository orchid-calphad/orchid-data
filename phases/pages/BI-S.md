# Bi–S phases

> Bi–S system: 8 phases (tier A 6, liquid 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-S.html · Markdown: https://data.orchid-project.org/phases/pages/BI-S.md

8 phases (tier A 6, liquid 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-S) · [full JSON](https://data.orchid-project.org/phases/systems/BI-S.json) · [Bi–S system page](https://data.orchid-project.org/systems/BI-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–S system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-bi-s-a16-orthorhombic); _phase:bi-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.34 K, x(S) 1–1 | 0 | 1 |
| [RHOMBOHEDRAL_A7](#phase-bi-s-a7-rhombohedral); _phase:bi-s:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.52 K, x(S) 0–0 | 1 | 1 |
| [BCC_A2](#phase-bi-s-bcc-a2); _phase:bi-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BI2S3_D58](#phase-bi-s-bi2s3-d58); _phase:bi-s:bi2s3-d58_ | Sb2S3 · D5_8 · oP20 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1042.41 K, x(S) 0.6–0.6 | 3 | 1 |
| [FCC_A1](#phase-bi-s-fcc-a1); _phase:bi-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-s-hcp-a3); _phase:bi-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-bi-s-liquid); _phase:bi-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1 | 3 | 1 |
| [MONOCLINIC_S](#phase-bi-s-s-monoclinic); _phase:bi-s:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## ORTHORHOMBIC_A16 (Bi–S)

- Id: `phase:bi-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.34 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:a16-orthorhombic)

Names (3): _corpus: _corpus:phase:bi-s:a16-orthorhombic, corpus:phase:bi-s:orthorhombic-a16  
_tdb: _tdb:BiS-14Hua.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): ORTHORHOMBIC_A16, type code %, sha256 `5bb6b53163e5d599…`

~~~~text
53: PHASE ORTHORHOMBIC_A16 % 1 1 !
54: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (Bi–S)

- Id: `phase:bi-s:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.52 K, x(S) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-s:a7-rhombohedral, corpus:phase:bi-s:rhombohedral-a7  
_paper: _paper:10.1007/s11664-014-3004-x:Rho_Bi  
_tdb: _tdb:BiS-14Hua.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `5bb6b53163e5d599…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Bi–S)

- Id: `phase:bi-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-s:bcc-a2  
_tdb: _tdb:BiS-14Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): BCC_A2, type code %B, sha256 `5bb6b53163e5d599…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : BI S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

## BI2S3_D58 (Bi–S)

- Id: `phase:bi-s:bi2s3-d58`; status `assigned`
- Structure: Sb2S3 · D5_8 · oP20 · Pnma (62); type `st:d5-8-sb2s3-op20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabhvc and oqmd-5929, space group 62
- Stoichiometry: Bi 0.4000, S 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1042.41 K, x(S) 0.6–0.6
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:bi2s3-d58)

Names (5): _corpus: _corpus:phase:bi-s:bi2s3-d58  
_mp: _mp:mp-aaaabhvc  
_oqmd: _oqmd:oqmd-5929  
_paper: _paper:10.1007/s11664-014-3004-x:Bi2S3  
_tdb: _tdb:BiS-14Hua.tdb:BI2S3_D58  


### TDB models of BI2S3_D58 (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): BI2S3_D58, type code %, sha256 `5bb6b53163e5d599…`

~~~~text
63: PHASE BI2S3_D58 % 2 2 3 !
64: CONST BI2S3_D58 : BI : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Bi–S)

- Id: `phase:bi-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-s:fcc-a1  
_tdb: _tdb:BiS-14Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): FCC_A1, type code %A, sha256 `5bb6b53163e5d599…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : BI S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

## HCP_A3 (Bi–S)

- Id: `phase:bi-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-s:hcp-a3  
_tdb: _tdb:BiS-14Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): HCP_A3, type code %A, sha256 `5bb6b53163e5d599…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : BI : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

## LIQUID (Bi–S)

- Id: `phase:bi-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:liquid)

Names (4): _corpus: _corpus:phase:bi-s:liquid  
_paper: _paper:10.1007/s11664-014-3004-x:L, paper:10.1007/s11664-014-3004-x:L2  
_tdb: _tdb:BiS-14Hua.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): LIQUID, type code %, sha256 `5bb6b53163e5d599…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : BI BI2S3 S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase; reports values for this phase_

## MONOCLINIC_S (Bi–S)

- Id: `phase:bi-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — BiS-14Hua.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-s:s-monoclinic)

Names (2): _corpus: _corpus:phase:bi-s:s-monoclinic  
_tdb: _tdb:BiS-14Hua.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[BiS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb): MONOCLINIC_S, type code %, sha256 `5bb6b53163e5d599…`

~~~~text
58: PHASE MONOCLINIC_S % 1 1 !
59: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
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
