# As–Ni phases

> As–Ni system: 9 phases (tier A 5, tier B 2, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-NI.html · Markdown: https://data.orchid-project.org/phases/pages/AS-NI.md

9 phases (tier A 5, tier B 2, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-NI) · [full JSON](https://data.orchid-project.org/phases/systems/AS-NI.json) · [Markdown](https://data.orchid-project.org/phases/pages/AS-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–Ni system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-as-ni-a7-rhombohedral); _phase:as-ni:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1090 K, x(As) 1–1 | 0 | 1 |
| [BCC_A2](#phase-as-ni-bcc-a2); _phase:as-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-as-ni-fcc-a1); _phase:as-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2213.24 K, x(As) 0–0.07094 | 0 | 1 |
| [HCP_A3](#phase-as-ni-hcp-a3); _phase:as-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-as-ni-liquid); _phase:as-ni:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 973.57–2500 K, x(As) 0–1 | 0 | 1 |
| [NI11AS8](#phase-as-ni-ni11as8); _phase:as-ni:ni11as8_ | Ni11As8 · tP76 · P4_12_12 (92) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1158.29 K, x(As) 0.42105–0.42105 | 0 | 1 |
| [NI5AS2](#phase-as-ni-ni5as2); _phase:as-ni:ni5as2_ | Pd5Sb2 · hP42 · P6_3cm (185) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1286.11 K, x(As) 0.28571–0.28571 | 0 | 1 |
| [NIAS_B81](#phase-as-ni-nias-b81); _phase:as-ni:nias-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1266.54 K, x(As) 0.5–0.5 | 0 | 1 |
| [NIAS2](#phase-as-ni-nias2); _phase:as-ni:nias2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1127.54 K, x(As) 0.66667–0.66667 | 0 | 1 |

## RHOMBOHEDRAL_A7 (As–Ni)

- Id: `phase:as-ni:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1090 K, x(As) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:as-ni:a7-rhombohedral  
_tdb: _tdb:NiAs-01Uhl.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `968fca0a518bfee0…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## BCC_A2 (As–Ni)

- Id: `phase:as-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:bcc-a2)

Names (2): _corpus: _corpus:phase:as-ni:bcc-a2  
_tdb: _tdb:NiAs-01Uhl.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): BCC_A2, type code %B, sha256 `968fca0a518bfee0…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AS NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## FCC_A1 (As–Ni)

- Id: `phase:as-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2213.24 K, x(As) 0–0.07094
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:fcc-a1)

Names (2): _corpus: _corpus:phase:as-ni:fcc-a1  
_tdb: _tdb:NiAs-01Uhl.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): FCC_A1, type code %A, sha256 `968fca0a518bfee0…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AS NI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## HCP_A3 (As–Ni)

- Id: `phase:as-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:hcp-a3)

Names (2): _corpus: _corpus:phase:as-ni:hcp-a3  
_tdb: _tdb:NiAs-01Uhl.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): HCP_A3, type code %A, sha256 `968fca0a518bfee0…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AS NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## LIQUID (As–Ni)

- Id: `phase:as-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 973.57–2500 K, x(As) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:liquid)

Names (2): _corpus: _corpus:phase:as-ni:liquid  
_tdb: _tdb:NiAs-01Uhl.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): LIQUID, type code %, sha256 `968fca0a518bfee0…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AS NI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## NI11AS8 (As–Ni)

- Id: `phase:as-ni:ni11as8`; status `assigned`
- Structure: Ni11As8 · tP76 · P4_12_12 (92); type `st:ni11as8-tp76`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: As 0.4211, Ni 0.5789
- Stability: stable in 1 of 1 calculated diagram(s): 300–1158.29 K, x(As) 0.42105–0.42105
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:ni11as8)

Names (4): _corpus: _corpus:phase:as-ni:ni11as8  
_mp: _mp:mp-aaaabptr  
_oqmd: _oqmd:oqmd-43653  
_tdb: _tdb:NiAs-01Uhl.tdb:NI11AS8  


### TDB models of NI11AS8 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): NI11AS8, type code %, sha256 `968fca0a518bfee0…`

~~~~text
50: PHASE NI11AS8 % 2 11 8 !
51: CONST NI11AS8 : NI : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## NI5AS2 (As–Ni)

- Id: `phase:as-ni:ni5as2`; status `assigned`
- Structure: Pd5Sb2 · hP42 · P6_3cm (185); type `st:pd5sb2-hp42`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: As 0.2857, Ni 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–1286.11 K, x(As) 0.28571–0.28571
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:ni5as2)

Names (4): _corpus: _corpus:phase:as-ni:ni5as2  
_mp: _mp:mp-aaaaabkf  
_oqmd: _oqmd:oqmd-2965  
_tdb: _tdb:NiAs-01Uhl.tdb:NI5AS2  


### TDB models of NI5AS2 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): NI5AS2, type code %, sha256 `968fca0a518bfee0…`

~~~~text
45: PHASE NI5AS2 % 2 5 2 !
46: CONST NI5AS2 : NI : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## NIAS_B81 (As–Ni)

- Id: `phase:as-ni:nias-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: As 0.5000, Ni 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1266.54 K, x(As) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:nias-b81)

Names (2): _corpus: _corpus:phase:as-ni:nias-b81  
_tdb: _tdb:NiAs-01Uhl.tdb:NIAS_B81  


### TDB models of NIAS_B81 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): NIAS_B81, type code %, sha256 `968fca0a518bfee0…`

~~~~text
55: PHASE NIAS_B81 % 2 1 1 !
56: CONST NIAS_B81 : NI : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
_assessment that models this phase_

## NIAS2 (As–Ni)

- Id: `phase:as-ni:nias2`; status `needs_review`
- No structure assigned. Why: dft_space_group_61_matches_3_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Pbca (61) — on-hull MP NiAs2 at x(NI)=0.3333
- Candidate (dft_oqmd): Pbca (61) — on-hull OQMD As2 Ni1 at x(NI)=0.3333
- Candidate (dft_space_group_and_stoichiometry): AuSn2 · oP24 · Pbca (61) — space group 61 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): TiO2 · C21 · oP24 · Pbca (61) — space group 61 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): NiAs2 · oP24 · Pbca (61) — space group 61 and stoichiometry match
- Candidate (sgte_mmc2): alpha-FeS2 · C18 · oP6 · Pnnm (58) — Hallstedt 2025 mmc2 row for NIAS2: NiAs2 (rammelsbergite, see also NiAs2)
- Candidate (sgte_mmc2): NiAs2 · oP24 · Pbca (61) — Hallstedt 2025 mmc2 row for NIAS2: NiAs2 (pararammelsbergite, see also FeAs2)
- Candidate (tdb_comment): FeS2 · oP6 · Pnnm, C18 — NiAs-01Uhl.tdb: 'Prototype FeS2 (oP6, Pnnm, C18), rammelsbergite, high T ?'
- Stoichiometry: As 0.6667, Ni 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1127.54 K, x(As) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ni:nias2)

Names (2): _corpus: _corpus:phase:as-ni:nias2  
_tdb: _tdb:NiAs-01Uhl.tdb:NIAS2  


### TDB models of NIAS2 (1): PHASE and CONSTITUENT statements as written

[NiAs-01Uhl.tdb](https://orchid-project.org/data/databases/sgte-binary/NiAs-01Uhl.tdb): NIAS2, type code %, sha256 `968fca0a518bfee0…`

~~~~text
61: PHASE NIAS2 % 2 1 2 !
62: CONST NIAS2 : NI : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00034-7](https://doi.org/10.1016/S0364-5916%2801%2900034-7) S. Uhland, H. Lechtman, L. Kaufman, Calphad, 25, 109-24(2001).  
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
