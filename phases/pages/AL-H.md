# Al–H phases

> Al–H system: 6 phases (tier A 3, liquid 1, gas 1, needs_review 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-H.html · Markdown: https://data.orchid-project.org/phases/pages/AL-H.md

6 phases (tier A 3, liquid 1, gas 1, needs_review 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-H) · [full JSON](https://data.orchid-project.org/phases/systems/AL-H.json) · [Al–H system page](https://data.orchid-project.org/systems/AL-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–H system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALH3](#phase-al-h-alh3); _phase:al-h:alh3_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-al-h-bcc-a2); _phase:al-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-al-h-fcc-a1); _phase:al-h:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–934.46 K, x(H) 0–0 | 0 | 1 |
| [GAS](#phase-al-h-gas); _phase:al-h:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 0.85511–1 | 0 | 1 |
| [HCP_A3](#phase-al-h-hcp-a3); _phase:al-h:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-al-h-liquid); _phase:al-h:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 933.46–2500 K, x(H) 0–0.00148 | 8 | 1 |

## ALH3 (Al–H)

- Id: `phase:al-h:alh3`; status `needs_review`
- No structure assigned. Why: dft_space_group_227_matches_0_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Fd-3m (227) — on-hull MP AlH3 at x(H)=0.7500
- Candidate (dft_oqmd): Fd-3m (227) — on-hull OQMD Al1 H3 at x(H)=0.7500
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for ALH3: AlH3 (see also AlH3 and FeF3)
- Candidate (sgte_mmc2): AlH3 · oP24 · Pnnm (58) — Hallstedt 2025 mmc2 row for ALH3: AlH3 (see also Cr3Si and FeF3)
- Candidate (sgte_mmc2): FeF3 · hR8 · R-3c (167) — Hallstedt 2025 mmc2 row for ALH3: AlH3 (see also AlH3 and Cr3Si)
- Candidate (tdb_comment): AlH3 · oP24 · Pnnm — AlH-04Qiu.tdb: 'Prototype AlH3 (oP24, Pnnm), gamma'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n, SB A15 — AlH-04Qiu.tdb: 'Prototype Cr3Si (cP8, Pm-3n, SB A15), beta?'
- Candidate (tdb_comment): FeF3 · hR8 · R-3c — AlH-04Qiu.tdb: 'Prototype FeF3 (hR8, R-3c), alpha'
- Stoichiometry: Al 0.2500, H 0.7500
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-h:alh3)

Names (2): _corpus: _corpus:phase:al-h:alh3  
_tdb: _tdb:AlH-04Qiu.tdb:ALH3  


### TDB models of ALH3 (1): PHASE and CONSTITUENT statements as written

[AlH-04Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlH-04Qiu.tdb): ALH3, type code %, sha256 `cafc133e72167e9d…`

~~~~text
51: PHASE ALH3 % 2 1 3 !
52: CONST ALH3 : AL : H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/15477020421043](https://doi.org/10.1361/15477020421043) Caian Qiu, Gregory B. Olson, Susanne M. Opalka, Donald L. Anton, Thermodynamic Evaluation of the Al-H System, Journal of Phase Equilibria &amp; Diffusion 25, 520-527 (2004).  
_assessment that models this phase_

## BCC_A2 (Al–H)

- Id: `phase:al-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-h:bcc-a2)

Names (2): _corpus: _corpus:phase:al-h:bcc-a2  
_tdb: _tdb:AlH-04Qiu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AlH-04Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlH-04Qiu.tdb): BCC_A2, type code %B, sha256 `cafc133e72167e9d…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AL : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/15477020421043](https://doi.org/10.1361/15477020421043) Caian Qiu, Gregory B. Olson, Susanne M. Opalka, Donald L. Anton, Thermodynamic Evaluation of the Al-H System, Journal of Phase Equilibria &amp; Diffusion 25, 520-527 (2004).  
_assessment that models this phase_

## FCC_A1 (Al–H)

- Id: `phase:al-h:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–934.46 K, x(H) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-h:fcc-a1)

Names (2): _corpus: _corpus:phase:al-h:fcc-a1  
_tdb: _tdb:AlH-04Qiu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AlH-04Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlH-04Qiu.tdb): FCC_A1, type code %A, sha256 `cafc133e72167e9d…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AL : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/15477020421043](https://doi.org/10.1361/15477020421043) Caian Qiu, Gregory B. Olson, Susanne M. Opalka, Donald L. Anton, Thermodynamic Evaluation of the Al-H System, Journal of Phase Equilibria &amp; Diffusion 25, 520-527 (2004).  
_assessment that models this phase_

## GAS (Al–H)

- Id: `phase:al-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 0.85511–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-h:gas)

Names (2): _corpus: _corpus:phase:al-h:gas  
_tdb: _tdb:AlH-04Qiu.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[AlH-04Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlH-04Qiu.tdb): GAS, type code %, sha256 `cafc133e72167e9d…`

~~~~text
54: PHASE GAS:G % 1 1 !
55: CONST GAS:G : AL AL2 ALH ALH2 ALH3 H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/15477020421043](https://doi.org/10.1361/15477020421043) Caian Qiu, Gregory B. Olson, Susanne M. Opalka, Donald L. Anton, Thermodynamic Evaluation of the Al-H System, Journal of Phase Equilibria &amp; Diffusion 25, 520-527 (2004).  
_assessment that models this phase_

## HCP_A3 (Al–H)

- Id: `phase:al-h:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-h:hcp-a3)

Names (2): _corpus: _corpus:phase:al-h:hcp-a3  
_tdb: _tdb:AlH-04Qiu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AlH-04Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlH-04Qiu.tdb): HCP_A3, type code %A, sha256 `cafc133e72167e9d…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : AL : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/15477020421043](https://doi.org/10.1361/15477020421043) Caian Qiu, Gregory B. Olson, Susanne M. Opalka, Donald L. Anton, Thermodynamic Evaluation of the Al-H System, Journal of Phase Equilibria &amp; Diffusion 25, 520-527 (2004).  
_assessment that models this phase_

## LIQUID (Al–H)

- Id: `phase:al-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 933.46–2500 K, x(H) 0–0.00148
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-h:liquid)

Names (3): _corpus: _corpus:phase:al-h:liquid  
_paper: _paper:10.1361/15477020421043:liquid  
_tdb: _tdb:AlH-04Qiu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AlH-04Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlH-04Qiu.tdb): LIQUID, type code %, sha256 `cafc133e72167e9d…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AL H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/15477020421043](https://doi.org/10.1361/15477020421043) Caian Qiu, Gregory B. Olson, Susanne M. Opalka, Donald L. Anton, Thermodynamic Evaluation of the Al-H System, Journal of Phase Equilibria &amp; Diffusion 25, 520-527 (2004).  
_assessment that models this phase; reports values for this phase_

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
