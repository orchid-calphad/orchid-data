# S–Sb phases

> S–Sb system: 8 phases (tier A 6, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/S-SB.html · Markdown: https://data.orchid-project.org/phases/pages/S-SB.md

8 phases (tier A 6, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=S-SB) · [full JSON](https://data.orchid-project.org/phases/systems/S-SB.json) · [Markdown](https://data.orchid-project.org/phases/pages/S-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the S–Sb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-s-sb-a16-orthorhombic); _phase:s-sb:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–368.3 K, x(S) 1–1 | 0 | 2 |
| [RHOMBOHEDRAL_A7](#phase-s-sb-a7-rhombohedral); _phase:s-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(S) 0–0 | 0 | 2 |
| [BCC_A2](#phase-s-sb-bcc-a2); _phase:s-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-s-sb-fcc-a1); _phase:s-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-s-sb-hcp-a3); _phase:s-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-s-sb-liquid); _phase:s-sb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 388.36–2500 K, x(S) 0–1 | 0 | 2 |
| [MONOCLINIC_S](#phase-s-sb-s-monoclinic); _phase:s-sb:s-monoclinic_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 368.3–2499.61 K, x(S) 1–1 | 0 | 2 |
| [SB2S3_D58](#phase-s-sb-sb2s3-d58); _phase:s-sb:sb2s3-d58_ | Sb2S3 · D5_8 · oP20 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–823.01 K, x(S) 0.6–0.6 | 0 | 2 |

## ORTHORHOMBIC_A16 (S–Sb)

- Id: `phase:s-sb:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–368.3 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:a16-orthorhombic)

Names (3): _corpus: _corpus:phase:s-sb:a16-orthorhombic  
_tdb: _tdb:SbS-21Cui.tdb:ORTHORHOMBIC_A16, tdb:SbS-21Shi.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): ORTHORHOMBIC_A16, type code %, sha256 `39dbbc281a135a20…`

~~~~text
52: PHASE ORTHORHOMBIC_A16 % 1 1 !
53: CONST ORTHORHOMBIC_A16 : S : !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): ORTHORHOMBIC_A16, type code %, sha256 `93a43f5f72e34e8e…`

~~~~text
50: PHASE ORTHORHOMBIC_A16 % 1 1 !
51: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (S–Sb)

- Id: `phase:s-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:s-sb:a7-rhombohedral  
_tdb: _tdb:SbS-21Cui.tdb:RHOMBOHEDRAL_A7, tdb:SbS-21Shi.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `39dbbc281a135a20…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `93a43f5f72e34e8e…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## BCC_A2 (S–Sb)

- Id: `phase:s-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:bcc-a2)

Names (3): _corpus: _corpus:phase:s-sb:bcc-a2  
_tdb: _tdb:SbS-21Cui.tdb:BCC_A2, tdb:SbS-21Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): BCC_A2, type code %B, sha256 `39dbbc281a135a20…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : S SB : VA : !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): BCC_A2, type code %B, sha256 `93a43f5f72e34e8e…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : S SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## FCC_A1 (S–Sb)

- Id: `phase:s-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:fcc-a1)

Names (3): _corpus: _corpus:phase:s-sb:fcc-a1  
_tdb: _tdb:SbS-21Cui.tdb:FCC_A1, tdb:SbS-21Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): FCC_A1, type code %A, sha256 `39dbbc281a135a20…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : S SB : VA : !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): FCC_A1, type code %A, sha256 `93a43f5f72e34e8e…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : S SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## HCP_A3 (S–Sb)

- Id: `phase:s-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:s-sb:hcp-a3  
_tdb: _tdb:SbS-21Cui.tdb:HCP_A3, tdb:SbS-21Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): HCP_A3, type code %A, sha256 `39dbbc281a135a20…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : SB : VA: !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): HCP_A3, type code %A, sha256 `93a43f5f72e34e8e…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : SB : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## LIQUID (S–Sb)

- Id: `phase:s-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 388.36–2500 K, x(S) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:liquid)

Names (3): _corpus: _corpus:phase:s-sb:liquid  
_tdb: _tdb:SbS-21Cui.tdb:LIQUID, tdb:SbS-21Shi.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): LIQUID, type code %, sha256 `39dbbc281a135a20…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : S SB2S3 SB : !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): LIQUID, type code %, sha256 `93a43f5f72e34e8e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : S SB2S3 SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## MONOCLINIC_S (S–Sb)

- Id: `phase:s-sb:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — SbS-21Cui.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — SbS-21Shi.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 368.3–2499.61 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:s-monoclinic)

Names (3): _corpus: _corpus:phase:s-sb:s-monoclinic  
_tdb: _tdb:SbS-21Cui.tdb:MONOCLINIC_S, tdb:SbS-21Shi.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): MONOCLINIC_S, type code %, sha256 `39dbbc281a135a20…`

~~~~text
57: PHASE MONOCLINIC_S % 1 1 !
58: CONST MONOCLINIC_S : S : !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): MONOCLINIC_S, type code %, sha256 `93a43f5f72e34e8e…`

~~~~text
55: PHASE MONOCLINIC_S % 1 1 !
56: CONST MONOCLINIC_S : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## SB2S3_D58 (S–Sb)

- Id: `phase:s-sb:sb2s3-d58`; status `assigned`
- Structure: Sb2S3 · D5_8 · oP20 · Pnma (62); type `st:d5-8-sb2s3-op20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaeeb and oqmd-87101, space group 62
- Stoichiometry: S 0.6000, Sb 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–823.01 K, x(S) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sb:sb2s3-d58)

Names (5): _corpus: _corpus:phase:s-sb:sb2s3-d58  
_mp: _mp:mp-aaaaaeeb  
_oqmd: _oqmd:oqmd-87101  
_tdb: _tdb:SbS-21Cui.tdb:SB2S3_D58, tdb:SbS-21Shi.tdb:SB2S3_D58  


### TDB models of SB2S3_D58 (2): PHASE and CONSTITUENT statements as written

[SbS-21Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Cui.tdb): SB2S3_D58, type code %, sha256 `39dbbc281a135a20…`

~~~~text
62: PHASE SB2S3_D58 % 2 2 3 !
63: CONST SB2S3_D58 : SB : S : !
~~~~

[SbS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/SbS-21Shi.tdb): SB2S3_D58, type code %, sha256 `93a43f5f72e34e8e…`

~~~~text
60: PHASE SB2S3_D58 % 2 2 3 !
61: CONST SB2S3_D58 : SB : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2021.102362](https://doi.org/10.1016/j.calphad.2021.102362) J. Cui, Y. Zhang, X. Hao, X. Liu, Y. Shen, Calphad, 75, 102362(2021).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

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
