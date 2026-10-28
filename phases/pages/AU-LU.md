# Au–Lu phases

> Au–Lu system: 9 phases (tier A 8, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-LU.html · Markdown: https://data.orchid-project.org/phases/pages/AU-LU.md

9 phases (tier A 8, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-LU) · [full JSON](https://data.orchid-project.org/phases/systems/AU-LU.json) · [Au–Lu system page](https://data.orchid-project.org/systems/AU-LU.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-LU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Lu system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU2LU_C11B](#phase-au-lu-au2lu-c11b); _phase:au-lu:au2lu-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1400.31 K, x(Lu) 0.33333–0.33333 | 6 | 1 |
| [AU3LU_D0A](#phase-au-lu-au3lu-d0a); _phase:au-lu:au3lu-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 498.36–1350.51 K, x(Lu) 0.25–0.25 | 8 | 1 |
| [AU4LU_D1A](#phase-au-lu-au4lu-d1a); _phase:au-lu:au4lu-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1302.66 K, x(Lu) 0.2–0.2 | 9 | 1 |
| [AULU_B2](#phase-au-lu-aulu-b2); _phase:au-lu:aulu-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2053.18 K, x(Lu) 0.5–0.5 | 7 | 1 |
| [AULU2_C37](#phase-au-lu-aulu2-c37); _phase:au-lu:aulu2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1603.83 K, x(Lu) 0.66667–0.66667 | 4 | 1 |
| [BCC_A2](#phase-au-lu-bcc-a2); _phase:au-lu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-au-lu-fcc-a1); _phase:au-lu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1338.18 K, x(Lu) 0–0.07866 | 3 | 1 |
| [HCP_A3](#phase-au-lu-hcp-a3); _phase:au-lu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.75 K, x(Lu) 1–1 | 2 | 1 |
| [LIQUID](#phase-au-lu-liquid); _phase:au-lu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1162.09–2500 K, x(Lu) 0–1 | 20 | 1 |

## AU2LU_C11B (Au–Lu)

- Id: `phase:au-lu:au2lu-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfyds and oqmd-28185, space group 139
- Stoichiometry: Au 0.6667, Lu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1400.31 K, x(Lu) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:au2lu-c11b)

Names (5): _corpus: _corpus:phase:au-lu:au2lu-c11b  
_mp: _mp:mp-aaacfyds  
_oqmd: _oqmd:oqmd-28185  
_paper: _paper:10.1007/s11669-016-0460-4:Au2Lu  
_tdb: _tdb:AuLu-16Wan.tdb:AU2LU_C11B  


### TDB models of AU2LU_C11B (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): AU2LU_C11B, type code %, sha256 `a48c8c77ccf4a882…`

~~~~text
51: PHASE AU2LU_C11B % 2 2 1 !
52: CONST AU2LU_C11B : AU : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase; reports values for this phase_

## AU3LU_D0A (Au–Lu)

- Id: `phase:au-lu:au3lu-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacgjbi and oqmd-28184, space group 59
- Stoichiometry: Au 0.7500, Lu 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 498.36–1350.51 K, x(Lu) 0.25–0.25
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:au3lu-d0a)

Names (5): _corpus: _corpus:phase:au-lu:au3lu-d0a  
_mp: _mp:mp-aaacgjbi  
_oqmd: _oqmd:oqmd-28184  
_paper: _paper:10.1007/s11669-016-0460-4:Au3Lu  
_tdb: _tdb:AuLu-16Wan.tdb:AU3LU_D0A  


### TDB models of AU3LU_D0A (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): AU3LU_D0A, type code %, sha256 `a48c8c77ccf4a882…`

~~~~text
46: PHASE AU3LU_D0A % 2 3 1 !
47: CONST AU3LU_D0A : AU : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase; reports values for this phase_

## AU4LU_D1A (Au–Lu)

- Id: `phase:au-lu:au4lu-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacivar and oqmd-28186, space group 87
- Stoichiometry: Au 0.8000, Lu 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1302.66 K, x(Lu) 0.2–0.2
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:au4lu-d1a)

Names (5): _corpus: _corpus:phase:au-lu:au4lu-d1a  
_mp: _mp:mp-aaacivar  
_oqmd: _oqmd:oqmd-28186  
_paper: _paper:10.1007/s11669-016-0460-4:Au4Lu  
_tdb: _tdb:AuLu-16Wan.tdb:AU4LU_D1A  


### TDB models of AU4LU_D1A (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): AU4LU_D1A, type code %, sha256 `a48c8c77ccf4a882…`

~~~~text
41: PHASE AU4LU_D1A % 2 4 1 !
42: CONST AU4LU_D1A : AU : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase; reports values for this phase_

## AULU_B2 (Au–Lu)

- Id: `phase:au-lu:aulu-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqqr and oqmd-10775, space group 221
- Stoichiometry: Au 0.5000, Lu 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2053.18 K, x(Lu) 0.5–0.5
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:aulu-b2)

Names (5): _corpus: _corpus:phase:au-lu:aulu-b2  
_mp: _mp:mp-aaaaaqqr  
_oqmd: _oqmd:oqmd-10775  
_paper: _paper:10.1007/s11669-016-0460-4:AuLu  
_tdb: _tdb:AuLu-16Wan.tdb:AULU_B2  


### TDB models of AULU_B2 (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): AULU_B2, type code %, sha256 `a48c8c77ccf4a882…`

~~~~text
56: PHASE AULU_B2 % 2 1 1 !
57: CONST AULU_B2 : AU : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase; reports values for this phase_

## AULU2_C37 (Au–Lu)

- Id: `phase:au-lu:aulu2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackrxo and oqmd-1800554, space group 62
- Stoichiometry: Au 0.3333, Lu 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1603.83 K, x(Lu) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:aulu2-c37)

Names (5): _corpus: _corpus:phase:au-lu:aulu2-c37  
_mp: _mp:mp-aaackrxo  
_oqmd: _oqmd:oqmd-1800554  
_paper: _paper:10.1007/s11669-016-0460-4:AuLu2  
_tdb: _tdb:AuLu-16Wan.tdb:AULU2_C37  


### TDB models of AULU2_C37 (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): AULU2_C37, type code %, sha256 `a48c8c77ccf4a882…`

~~~~text
61: PHASE AULU2_C37 % 2 1 2 !
62: CONST AULU2_C37 : AU : LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Au–Lu)

- Id: `phase:au-lu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:bcc-a2)

Names (2): _corpus: _corpus:phase:au-lu:bcc-a2  
_tdb: _tdb:AuLu-16Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): BCC_A2, type code %B, sha256 `a48c8c77ccf4a882…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase_

## FCC_A1 (Au–Lu)

- Id: `phase:au-lu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1338.18 K, x(Lu) 0–0.07866
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:fcc-a1)

Names (3): _corpus: _corpus:phase:au-lu:fcc-a1  
_paper: _paper:10.1007/s11669-016-0460-4:(Au)  
_tdb: _tdb:AuLu-16Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): FCC_A1, type code %A, sha256 `a48c8c77ccf4a882…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AU% LU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Au–Lu)

- Id: `phase:au-lu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.75 K, x(Lu) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:hcp-a3)

Names (3): _corpus: _corpus:phase:au-lu:hcp-a3  
_paper: _paper:10.1007/s11669-016-0460-4:(Lu)  
_tdb: _tdb:AuLu-16Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): HCP_A3, type code %A, sha256 `a48c8c77ccf4a882…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AU LU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Au–Lu)

- Id: `phase:au-lu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1162.09–2500 K, x(Lu) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-lu:liquid)

Names (3): _corpus: _corpus:phase:au-lu:liquid  
_paper: _paper:10.1007/s11669-016-0460-4:L  
_tdb: _tdb:AuLu-16Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuLu-16Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb): LIQUID, type code %, sha256 `a48c8c77ccf4a882…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AU LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016).  
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
