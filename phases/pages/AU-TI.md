# Au–Ti phases

> Au–Ti system: 8 phases (tier A 6, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-TI.html · Markdown: https://data.orchid-project.org/phases/pages/AU-TI.md

8 phases (tier A 6, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-TI) · [full JSON](https://data.orchid-project.org/phases/systems/AU-TI.json) · [Au–Ti system page](https://data.orchid-project.org/systems/AU-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Ti system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU2TI_C11B](#phase-au-ti-au2ti-c11b); _phase:au-ti:au2ti-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1717.77 K, x(Ti) 0.33333–0.33333 | 9 | 1 |
| [AU4TI_D1A](#phase-au-ti-au4ti-d1a); _phase:au-ti:au4ti-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1443.75 K, x(Ti) 0.18235–0.2 | 6 | 1 |
| [AUTI](#phase-au-ti-auti); _phase:au-ti:auti_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1754.28 K, x(Ti) 0.49038–0.61943 | 11 | 1 |
| [AUTI3_A15](#phase-au-ti-auti3-a15); _phase:au-ti:auti3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1654.27 K, x(Ti) 0.75–0.75 | 12 | 1 |
| [BCC_A2](#phase-au-ti-bcc-a2); _phase:au-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1104.89–2205.98 K, x(Ti) 0.84497–1 | 6 | 1 |
| [FCC_A1](#phase-au-ti-fcc-a1); _phase:au-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1394.1 K, x(Ti) 0–0.12621 | 3 | 1 |
| [HCP_A3](#phase-au-ti-hcp-a3); _phase:au-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 0.98233–1 | 1 | 1 |
| [LIQUID](#phase-au-ti-liquid); _phase:au-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1337.33–2500 K, x(Ti) 0–1 | 24 | 1 |

## AU2TI_C11B (Au–Ti)

- Id: `phase:au-ti:au2ti-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfycp and oqmd-10816, space group 139
- Stoichiometry: Au 0.6667, Ti 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1717.77 K, x(Ti) 0.33333–0.33333
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:au2ti-c11b)

Names (5): _corpus: _corpus:phase:au-ti:au2ti-c11b  
_mp: _mp:mp-aaacfycp  
_oqmd: _oqmd:oqmd-10816  
_paper: _paper:10.1016/s0364-5916(01)00026-8:TiAu2  
_tdb: _tdb:AuTi-01Luo-LB.tdb:AU2TI_C11B  


### TDB models of AU2TI_C11B (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): AU2TI_C11B, type code %, sha256 `3cb2928079fa6325…`

~~~~text
48: PHASE AU2TI_C11B % 2 2 1 !
49: CONST AU2TI_C11B : AU : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

## AU4TI_D1A (Au–Ti)

- Id: `phase:au-ti:au4ti-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1443.75 K, x(Ti) 0.18235–0.2
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:au4ti-d1a)

Names (3): _corpus: _corpus:phase:au-ti:au4ti-d1a  
_paper: _paper:10.1016/s0364-5916(01)00026-8:TiAu4  
_tdb: _tdb:AuTi-01Luo-LB.tdb:AU4TI_D1A  


### TDB models of AU4TI_D1A (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): AU4TI_D1A, type code %, sha256 `3cb2928079fa6325…`

~~~~text
43: PHASE AU4TI_D1A % 2 4 1 !
44: CONST AU4TI_D1A : AU : AU TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

## AUTI (Au–Ti)

- Id: `phase:au-ti:auti`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P4/nmm (129) — on-hull MP TiAu at x(TI)=0.5000
- Candidate (dft_oqmd): P4/nmm (129) — on-hull OQMD Au1 Ti1 at x(TI)=0.5000
- Candidate (literature_printed): AuCd · oP4 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): CuTi-gamma · B11 · tP4 · P4/nmm (129) — Hallstedt 2025 mmc2 row for AUTI: AuTi (alpha, low T)
- Candidate (sgte_mmc2): AuCd · B19 · oP4 · Pmma (51) — Hallstedt 2025 mmc2 row for AUTI: AuTi (beta, low T)
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for AUTI: AuTi (gamma, dominating)
- Candidate (tdb_comment): AuCd · oP4 · Pmma, B19 — AuTi-01Luo-LB.tdb: 'Prototype AuCd (oP4, Pmma, B19) beta, low T'
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m, B2 — AuTi-01Luo-LB.tdb: 'Prototype CsCl (cP2, Pm-3m, B2) gamma, dominating'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1754.28 K, x(Ti) 0.49038–0.61943
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:auti)

Names (4): _corpus: _corpus:phase:au-ti:auti  
_paper: _paper:10.1016/s0364-5916(01)00026-8:(αTi), paper:10.1016/s0364-5916(01)00026-8:TiAu  
_tdb: _tdb:AuTi-01Luo-LB.tdb:AUTI  


### TDB models of AUTI (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): AUTI, type code %, sha256 `3cb2928079fa6325…`

~~~~text
55: PHASE AUTI % 2 1 1 !
56: CONST AUTI : AU TI : TI VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

## AUTI3_A15 (Au–Ti)

- Id: `phase:au-ti:auti3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacqs and oqmd-10815, space group 223
- Stoichiometry: Au 0.2500, Ti 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1654.27 K, x(Ti) 0.75–0.75
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:auti3-a15)

Names (5): _corpus: _corpus:phase:au-ti:auti3-a15  
_mp: _mp:mp-aaaaacqs  
_oqmd: _oqmd:oqmd-10815  
_paper: _paper:10.1016/s0364-5916(01)00026-8:Ti3Au  
_tdb: _tdb:AuTi-01Luo-LB.tdb:AUTI3_A15  


### TDB models of AUTI3_A15 (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): AUTI3_A15, type code %, sha256 `3cb2928079fa6325…`

~~~~text
60: PHASE AUTI3_A15 % 2 1 3 !
61: CONST AUTI3_A15 : AU : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Au–Ti)

- Id: `phase:au-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1104.89–2205.98 K, x(Ti) 0.84497–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:bcc-a2)

Names (3): _corpus: _corpus:phase:au-ti:bcc-a2  
_paper: _paper:10.1016/s0364-5916(01)00026-8:(βTi)  
_tdb: _tdb:AuTi-01Luo-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): BCC_A2, type code %B, sha256 `3cb2928079fa6325…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AU TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Au–Ti)

- Id: `phase:au-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1394.1 K, x(Ti) 0–0.12621
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:au-ti:fcc-a1  
_paper: _paper:10.1016/s0364-5916(01)00026-8:(Au)  
_tdb: _tdb:AuTi-01Luo-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): FCC_A1, type code %A, sha256 `3cb2928079fa6325…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AU% TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Au–Ti)

- Id: `phase:au-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 0.98233–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:hcp-a3)

Names (3): _corpus: _corpus:phase:au-ti:hcp-a3  
_paper: _paper:10.1016/s0364-5916(01)00026-8:(αTi)  
_tdb: _tdb:AuTi-01Luo-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): HCP_A3, type code %A, sha256 `3cb2928079fa6325…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AU TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Au–Ti)

- Id: `phase:au-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1337.33–2500 K, x(Ti) 0–1
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ti:liquid)

Names (3): _corpus: _corpus:phase:au-ti:liquid  
_paper: _paper:10.1016/s0364-5916(01)00026-8:L  
_tdb: _tdb:AuTi-01Luo-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuTi-01Luo-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb): LIQUID, type code %, sha256 `3cb2928079fa6325…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AU TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001).  
_assessment that models this phase; reports values for this phase_

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
