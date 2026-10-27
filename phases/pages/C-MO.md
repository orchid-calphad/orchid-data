# C–Mo phases

> C–Mo system: 8 phases (tier A 4, tier C 1, liquid 1, needs_review 1, interstitial_fcc_a1_compound 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-MO.html · Markdown: https://data.orchid-project.org/phases/pages/C-MO.md

8 phases (tier A 4, tier C 1, liquid 1, needs_review 1, interstitial_fcc_a1_compound 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-MO) · [full JSON](https://data.orchid-project.org/phases/systems/C-MO.json) · [Markdown](https://data.orchid-project.org/phases/pages/C-MO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Mo system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-mo-a4-diamond); _phase:c-mo:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GRAPHITE_A9](#phase-c-mo-a9-graphite); _phase:c-mo:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 1 |
| [BCC_A2](#phase-c-mo-bcc-a2); _phase:c-mo:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2895.99 K, x(C) 0–0.00877 | 0 | 1 |
| [MC_ETA](#phase-c-mo-eta-mc); _phase:c-mo:eta-mc_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1930–2826.05 K, x(C) 0.35528–0.40968 | 0 | 1 |
| [FCC_A1](#phase-c-mo-fcc-a1); _phase:c-mo:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 1 of 1 calculated diagram(s): 2236.75–2866.05 K, x(C) 0.3974–0.43199 | 0 | 1 |
| [HCP_A3](#phase-c-mo-hcp-a3); _phase:c-mo:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2788.61 K, x(C) 0.27109–0.33333 | 0 | 1 |
| [LIQUID](#phase-c-mo-liquid); _phase:c-mo:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2477.77–4000 K, x(C) 0–0.58357 | 0 | 1 |
| [MC_SHP](#phase-c-mo-mc-shp); _phase:c-mo:mc-shp_ | WC · B_h · hP2 · P-6m2 (187) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1422.95 K, x(C) 0.5–0.5 | 0 | 1 |

## DIAMOND_A4 (C–Mo)

- Id: `phase:c-mo:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:a4-diamond)

Names (2): _corpus: _corpus:phase:c-mo:a4-diamond  
_tdb: _tdb:MoC-88And-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): DIAMOND_A4, type code %, sha256 `8c882437177ec794…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Mo)

- Id: `phase:c-mo:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:a9-graphite)

Names (2): _corpus: _corpus:phase:c-mo:a9-graphite  
_tdb: _tdb:MoC-88And-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): GRAPHITE_A9, type code %, sha256 `8c882437177ec794…`

~~~~text
54: PHASE GRAPHITE_A9 % 1 1 !
55: CONST GRAPHITE_A9 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
_assessment that models this phase_

## BCC_A2 (C–Mo)

- Id: `phase:c-mo:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2895.99 K, x(C) 0–0.00877
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:bcc-a2)

Names (2): _corpus: _corpus:phase:c-mo:bcc-a2  
_tdb: _tdb:MoC-88And-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): BCC_A2, type code %B, sha256 `8c882437177ec794…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : MO : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
_assessment that models this phase_

## MC_ETA (C–Mo)

- Id: `phase:c-mo:eta-mc`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; name_has_descriptive_tokens:MC; no_structure_token
- Candidate (sgte_mmc2): TiAs · B_i · hP8 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for MC_ETA: Mo3C2
- Candidate (tdb_comment): TiAs · hP8 · P6_3/mmc, SB: B_i — MoC-88And-LB.tdb: 'Prototype TiAs (hP8, P6_3/mmc, SB: B_i)'
- Stability: stable in 1 of 1 calculated diagram(s): 1930–2826.05 K, x(C) 0.35528–0.40968
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:eta-mc)

Names (2): _corpus: _corpus:phase:c-mo:eta-mc  
_tdb: _tdb:MoC-88And-LB.tdb:MC_ETA  


### TDB models of MC_ETA (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): MC_ETA, type code %, sha256 `8c882437177ec794…`

~~~~text
59: PHASE MC_ETA % 2 1 1 !
60: CONST MC_ETA : MO : C% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
_assessment that models this phase_

## FCC_A1 (C–Mo)

- Id: `phase:c-mo:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2236.75–2866.05 K, x(C) 0.3974–0.43199
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:fcc-a1)

Names (2): _corpus: _corpus:phase:c-mo:fcc-a1  
_tdb: _tdb:MoC-88And-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): FCC_A1, type code %A, sha256 `8c882437177ec794…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : MO : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
_assessment that models this phase_

## HCP_A3 (C–Mo)

- Id: `phase:c-mo:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2788.61 K, x(C) 0.27109–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:hcp-a3)

Names (2): _corpus: _corpus:phase:c-mo:hcp-a3  
_tdb: _tdb:MoC-88And-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): HCP_A3, type code %A, sha256 `8c882437177ec794…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : MO : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
_assessment that models this phase_

## LIQUID (C–Mo)

- Id: `phase:c-mo:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2477.77–4000 K, x(C) 0–0.58357
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:liquid)

Names (2): _corpus: _corpus:phase:c-mo:liquid  
_tdb: _tdb:MoC-88And-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): LIQUID, type code %, sha256 `8c882437177ec794…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : C MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
_assessment that models this phase_

## MC_SHP (C–Mo)

- Id: `phase:c-mo:mc-shp`; status `assigned`
- Structure: WC · B_h · hP2 · P-6m2 (187); type `st:b-h-wc-hp2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MC,SHP, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.5000, Mo 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1422.95 K, x(C) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-mo:mc-shp)

Names (2): _corpus: _corpus:phase:c-mo:mc-shp  
_tdb: _tdb:MoC-88And-LB.tdb:MC_SHP  


### TDB models of MC_SHP (1): PHASE and CONSTITUENT statements as written

[MoC-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoC-88And-LB.tdb): MC_SHP, type code %, sha256 `8c882437177ec794…`

~~~~text
64: PHASE MC_SHP % 2 1 1 !
65: CONST MC_SHP : MO : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90024-7](https://doi.org/10.1016/0364-5916%2888%2990024-7) J.-O. Andersson, Calphad, 12, 1-8(1988).  
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
