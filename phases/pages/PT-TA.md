# Pt–Ta phases

> Pt–Ta system: 9 phases (tier A 4, tier C 2, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PT-TA.html · Markdown: https://data.orchid-project.org/phases/pages/PT-TA.md

9 phases (tier A 4, tier C 2, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PT-TA) · [full JSON](https://data.orchid-project.org/phases/systems/PT-TA.json) · [Pt–Ta system page](https://data.orchid-project.org/systems/PT-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/PT-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pt–Ta system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pt-ta-bcc-a2); _phase:pt-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(Ta) 0.92704–1 | 0 | 1 |
| [FCC_A1](#phase-pt-ta-fcc-a1); _phase:pt-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2044.7 K, x(Ta) 0–0.00013 | 0 | 1 |
| [HCP_A3](#phase-pt-ta-hcp-a3); _phase:pt-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pt-ta-liquid); _phase:pt-ta:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1944.7–4000 K, x(Ta) 0–1 | 0 | 1 |
| [PT2TA](#phase-pt-ta-pt2ta); _phase:pt-ta:pt2ta_ | Au2V · oC12 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2504.51 K, x(Ta) 0.33333–0.33333 | 0 | 1 |
| [PT3TA](#phase-pt-ta-pt3ta); _phase:pt-ta:pt3ta_ | NbPt3 · mP16 · P2_1/m (11) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2520.53 K, x(Ta) 0.25–0.25 | 0 | 1 |
| [PTTA](#phase-pt-ta-ptta); _phase:pt-ta:ptta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1909.6–2117.81 K, x(Ta) 0.5–0.5 | 0 | 1 |
| [PTTA3_D8B](#phase-pt-ta-ptta3-d8b); _phase:pt-ta:ptta3-d8b_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 461.76–2632.67 K, x(Ta) 0.64392–0.77362 | 0 | 1 |
| [PTTA6](#phase-pt-ta-ptta6); _phase:pt-ta:ptta6_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2000 K, x(Ta) 0.85714–0.85714 | 0 | 1 |

## BCC_A2 (Pt–Ta)

- Id: `phase:pt-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(Ta) 0.92704–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:bcc-a2)

Names (2): _corpus: _corpus:phase:pt-ta:bcc-a2  
_tdb: _tdb:PtTa-98Spe.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): BCC_A2, type code %B, sha256 `fd7011b9e894274e…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : PT TA% : VA : !
~~~~

## FCC_A1 (Pt–Ta)

- Id: `phase:pt-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2044.7 K, x(Ta) 0–0.00013
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:fcc-a1)

Names (2): _corpus: _corpus:phase:pt-ta:fcc-a1  
_tdb: _tdb:PtTa-98Spe.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): FCC_A1, type code %A, sha256 `fd7011b9e894274e…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : PT% TA : VA : !
~~~~

## HCP_A3 (Pt–Ta)

- Id: `phase:pt-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:hcp-a3)

Names (2): _corpus: _corpus:phase:pt-ta:hcp-a3  
_tdb: _tdb:PtTa-98Spe.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): HCP_A3, type code %A, sha256 `fd7011b9e894274e…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : PT TA : VA : !
~~~~

## LIQUID (Pt–Ta)

- Id: `phase:pt-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1944.7–4000 K, x(Ta) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:liquid)

Names (2): _corpus: _corpus:phase:pt-ta:liquid  
_tdb: _tdb:PtTa-98Spe.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): LIQUID, type code %, sha256 `fd7011b9e894274e…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : PT TA : !
~~~~

## PT2TA (Pt–Ta)

- Id: `phase:pt-ta:pt2ta`; status `assigned`
- Structure: Au2V · oC12 · Cmcm (63); type `st:au2v-oc12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pt 0.6667, Ta 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2504.51 K, x(Ta) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:pt2ta)

Names (2): _corpus: _corpus:phase:pt-ta:pt2ta  
_tdb: _tdb:PtTa-98Spe.tdb:PT2TA  


### TDB models of PT2TA (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): PT2TA, type code %, sha256 `fd7011b9e894274e…`

~~~~text
51: PHASE PT2TA % 2 2 1 !
52: CONST PT2TA : PT : TA : !
~~~~

## PT3TA (Pt–Ta)

- Id: `phase:pt-ta:pt3ta`; status `assigned`
- Structure: NbPt3 · mP16 · P2_1/m (11); type `st:nbpt3-mp16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_11_matches_0_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pt 0.7500, Ta 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–2520.53 K, x(Ta) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:pt3ta)

Names (2): _corpus: _corpus:phase:pt-ta:pt3ta  
_tdb: _tdb:PtTa-98Spe.tdb:PT3TA  


### TDB models of PT3TA (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): PT3TA, type code %, sha256 `fd7011b9e894274e…`

~~~~text
46: PHASE PT3TA % 2 3 1 !
47: CONST PT3TA : PT : TA : !
~~~~

## PTTA (Pt–Ta)

- Id: `phase:pt-ta:ptta`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): Pmma (51) — on-hull OQMD Pt1 Ta1 at x(TA)=0.5000
- Candidate (sgte_mmc2): (PtTa) · tI2 — Hallstedt 2025 mmc2 row for PTTA: PtTa
- Stoichiometry: Pt 0.5000, Ta 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 1909.6–2117.81 K, x(Ta) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:ptta)

Names (2): _corpus: _corpus:phase:pt-ta:ptta  
_tdb: _tdb:PtTa-98Spe.tdb:PTTA  


### TDB models of PTTA (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): PTTA, type code %, sha256 `fd7011b9e894274e…`

~~~~text
56: PHASE PTTA % 2 1 1 !
57: CONST PTTA : PT : TA : !
~~~~

## PTTA3_D8B (Pt–Ta)

- Id: `phase:pt-ta:ptta3-d8b`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 461.76–2632.67 K, x(Ta) 0.64392–0.77362
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:ptta3-d8b)

Names (2): _corpus: _corpus:phase:pt-ta:ptta3-d8b  
_tdb: _tdb:PtTa-98Spe.tdb:PTTA3_D8B  


### TDB models of PTTA3_D8B (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): PTTA3_D8B, type code %, sha256 `fd7011b9e894274e…`

~~~~text
61: PHASE PTTA3_D8B % 1 1 !
62: CONST PTTA3_D8B : PT TA : !
~~~~

## PTTA6 (Pt–Ta)

- Id: `phase:pt-ta:ptta6`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (PtTa6) — Hallstedt 2025 mmc2 row for PTTA6: PtTa6
- Stoichiometry: Pt 0.1429, Ta 0.8571
- Stability: stable in 1 of 1 calculated diagram(s): 300–2000 K, x(Ta) 0.85714–0.85714
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ta:ptta6)

Names (2): _corpus: _corpus:phase:pt-ta:ptta6  
_tdb: _tdb:PtTa-98Spe.tdb:PTTA6  


### TDB models of PTTA6 (1): PHASE and CONSTITUENT statements as written

[PtTa-98Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTa-98Spe.tdb): PTTA6, type code %, sha256 `fd7011b9e894274e…`

~~~~text
66: PHASE PTTA6 % 2 1 6 !
67: CONST PTTA6 : PT : TA : !
~~~~

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
