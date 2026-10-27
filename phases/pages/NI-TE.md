# Ni–Te phases

> Ni–Te system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-TE.html · Markdown: https://data.orchid-project.org/phases/pages/NI-TE.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-TE) · [full JSON](https://data.orchid-project.org/phases/systems/NI-TE.json) · [Ni–Te system page](https://data.orchid-project.org/systems/NI-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Te system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-ni-te-a8-hexagonal); _phase:ni-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 2 | 1 |
| [BCC_A2](#phase-ni-te-bcc-a2); _phase:ni-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ni-te-fcc-a1); _phase:ni-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1762.74 K, x(Te) 0–0.00013 | 4 | 1 |
| [HCP_A3](#phase-ni-te-hcp-a3); _phase:ni-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-ni-te-ion); _phase:ni-te:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 720.93–2500 K, x(Te) 0–1 | 10 | 1 |
| [NI20TE17](#phase-ni-te-ni20te17); _phase:ni-te:ni20te17_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 962.18–1153.34 K, x(Te) 0.45946–0.45946 | 10 | 1 |
| [NI52TE40](#phase-ni-te-ni52te40); _phase:ni-te:ni52te40_ | Ni1.29Te · oP20 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1012.02 K, x(Te) 0.43478–0.43478 | 4 | 1 |
| [NITE_BETA_HT](#phase-ni-te-nite-beta); _phase:ni-te:nite-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1004.57–1295.16 K, x(Te) 0.37103–0.43367 | 12 | 1 |
| [NITE_C38](#phase-ni-te-nite-c38); _phase:ni-te:nite-c38_ | Cu2Sb · C38 · tP6 · P4/nmm (129) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1055.8 K, x(Te) 0.39446–0.41198 | 8 | 1 |
| [NITE_C6](#phase-ni-te-nite-c6); _phase:ni-te:nite-c6_ | CdI2 · C6 · hP3 · P-3m1 (164) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1172.66 K, x(Te) 0.5203–0.66711 | 8 | 1 |

## HEXAGONAL_A8 (Ni–Te)

- Id: `phase:ni-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:a8-hexagonal)

Names (3): _corpus: _corpus:phase:ni-te:a8-hexagonal  
_paper: _paper:10.1007/s10853-019-03689-0:Te – A8  
_tdb: _tdb:NiTe-19Arv.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): HEXAGONAL_A8, type code %, sha256 `be93db315c060716…`

~~~~text
55: PHASE HEXAGONAL_A8 % 1 1 !
56: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Ni–Te)

- Id: `phase:ni-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:bcc-a2)

Names (2): _corpus: _corpus:phase:ni-te:bcc-a2  
_tdb: _tdb:NiTe-19Arv.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): BCC_A2, type code %B, sha256 `be93db315c060716…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : NI TE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase_

## FCC_A1 (Ni–Te)

- Id: `phase:ni-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1762.74 K, x(Te) 0–0.00013
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:fcc-a1)

Names (3): _corpus: _corpus:phase:ni-te:fcc-a1  
_paper: _paper:10.1007/s10853-019-03689-0:FCC  
_tdb: _tdb:NiTe-19Arv.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): FCC_A1, type code %A, sha256 `be93db315c060716…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : NI% TE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ni–Te)

- Id: `phase:ni-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:hcp-a3)

Names (2): _corpus: _corpus:phase:ni-te:hcp-a3  
_tdb: _tdb:NiTe-19Arv.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): HCP_A3, type code %A, sha256 `be93db315c060716…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : NI TE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase_

## ION (Ni–Te)

- Id: `phase:ni-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 720.93–2500 K, x(Te) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:ion)

Names (4): _corpus: _corpus:phase:ni-te:ion, corpus:phase:ni-te:liquid  
_paper: _paper:10.1007/s10853-019-03689-0:L  
_tdb: _tdb:NiTe-19Arv.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): ION, type code %, sha256 `be93db315c060716…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : NI+2 : TE-2 VA TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase; reports values for this phase_

## NI20TE17 (Ni–Te)

- Id: `phase:ni-te:ni20te17`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Ni20Te17) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ni20Te17) — Hallstedt 2025 mmc2 row for NI20TE17: Ni20Te17 (gamma-2, high T)
- Stoichiometry: Ni 0.5405, Te 0.4595
- Stability: stable in 1 of 1 calculated diagram(s): 962.18–1153.34 K, x(Te) 0.45946–0.45946
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:ni20te17)

Names (3): _corpus: _corpus:phase:ni-te:ni20te17  
_paper: _paper:10.1007/s10853-019-03689-0:γ2  
_tdb: _tdb:NiTe-19Arv.tdb:NI20TE17  


### TDB models of NI20TE17 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): NI20TE17, type code %, sha256 `be93db315c060716…`

~~~~text
75: PHASE NI20TE17 % 2 20 17 !
76: CONST NI20TE17 : NI : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase; reports values for this phase_

## NI52TE40 (Ni–Te)

- Id: `phase:ni-te:ni52te40`; status `assigned`
- Structure: Ni1.29Te · oP20 · Pnma (62); type `st:ni1-29te-op20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.5652, Te 0.4348
- Stability: stable in 1 of 1 calculated diagram(s): 300–1012.02 K, x(Te) 0.43478–0.43478
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:ni52te40)

Names (3): _corpus: _corpus:phase:ni-te:ni52te40  
_paper: _paper:10.1007/s10853-019-03689-0:γ1  
_tdb: _tdb:NiTe-19Arv.tdb:NI52TE40  


### TDB models of NI52TE40 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): NI52TE40, type code %, sha256 `be93db315c060716…`

~~~~text
70: PHASE NI52TE40 % 2 52 40 !
71: CONST NI52TE40 : NI : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase; reports values for this phase_

## NITE_BETA_HT (Ni–Te)

- Id: `phase:ni-te:nite-beta`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): P2_1/m (11) — on-hull MP Ni3Te2 at x(TE)=0.4000
- Candidate (dft_oqmd): R32 (155) — on-hull OQMD Ni3 Te2 at x(TE)=0.4000
- Candidate (literature_printed): Cu2Se-beta · cF44 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Cu2Se-beta · cF44 · Fm-3m (225) — Hallstedt 2025 mmc2 row for NITE_BETA_HT: Ni3Te2 (beta-1, high T)
- Candidate (tdb_comment): Cu2Se-beta · cF44 · Fm-3m — NiTe-19Arv.tdb: 'Prototype Cu2Se-beta (cF44, Fm-3m), beta-1 (high T), structure uncertain'
- Stability: stable in 1 of 1 calculated diagram(s): 1004.57–1295.16 K, x(Te) 0.37103–0.43367
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:nite-beta)

Names (4): _corpus: _corpus:phase:ni-te:nite-beta, corpus:phase:ni-te:nite-beta-ht  
_paper: _paper:10.1007/s10853-019-03689-0:β1  
_tdb: _tdb:NiTe-19Arv.tdb:NITE_BETA_HT  


### TDB models of NITE_BETA_HT (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): NITE_BETA_HT, type code %, sha256 `be93db315c060716…`

~~~~text
65: PHASE NITE_BETA_HT % 2 2 1 !
66: CONST NITE_BETA_HT : NI TE : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase; reports values for this phase_

## NITE_C38 (Ni–Te)

- Id: `phase:ni-te:nite-c38`; status `assigned`
- Structure: Cu2Sb · C38 · tP6 · P4/nmm (129); type `st:c38-cu2sb-tp6`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1055.8 K, x(Te) 0.39446–0.41198
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:nite-c38)

Names (3): _corpus: _corpus:phase:ni-te:nite-c38  
_paper: _paper:10.1007/s10853-019-03689-0:β2  
_tdb: _tdb:NiTe-19Arv.tdb:NITE_C38  


### TDB models of NITE_C38 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): NITE_C38, type code %, sha256 `be93db315c060716…`

~~~~text
60: PHASE NITE_C38 % 3 1 1 1 !
61: CONST NITE_C38 : NI : TE : NI VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
_assessment that models this phase; reports values for this phase_

## NITE_C6 (Ni–Te)

- Id: `phase:ni-te:nite-c6`; status `assigned`
- Structure: CdI2 · C6 · hP3 · P-3m1 (164); type `st:c6-cdi2-hp3`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1172.66 K, x(Te) 0.5203–0.66711
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-te:nite-c6)

Names (3): _corpus: _corpus:phase:ni-te:nite-c6  
_paper: _paper:10.1007/s10853-019-03689-0:δ  
_tdb: _tdb:NiTe-19Arv.tdb:NITE_C6  


### TDB models of NITE_C6 (1): PHASE and CONSTITUENT statements as written

[NiTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb): NITE_C6, type code %, sha256 `be93db315c060716…`

~~~~text
80: PHASE NITE_C6 % 3 1 1 2 !
81: CONST NITE_C6 : NI VA : NI VA : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019).  
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
