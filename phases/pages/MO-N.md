# Mo–N phases

> Mo–N system: 8 phases (tier A 2, tier C 1, liquid 1, gas 1, needs_review 2, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-N.html · Markdown: https://data.orchid-project.org/phases/pages/MO-N.md

8 phases (tier A 2, tier C 1, liquid 1, gas 1, needs_review 2, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-N) · [full JSON](https://data.orchid-project.org/phases/systems/MO-N.json) · [Mo–N system page](https://data.orchid-project.org/systems/MO-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–N system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-n-bcc-a2); _phase:mo-n:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.14 K, x(N) 0–0.0019 | 1 | 2 |
| [FCC_A1](#phase-mo-n-fcc-a1); _phase:mo-n:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 1 of 2 calculated diagram(s): 300–1092.37 K, x(N) 0.30895–0.48355 | 2 | 2 |
| [HCP_A3](#phase-mo-n-hcp-a3); _phase:mo-n:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-mo-n-liquid); _phase:mo-n:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2877.89–4000 K, x(N) 0–0.0096 | 1 | 2 |
| [MC_SHP](#phase-mo-n-mc-shp); _phase:mo-n:mc-shp_ | WC · B_h · hP2 · P-6m2 (187) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–769.48 K, x(N) 0.5–0.5 | 0 | 1 |
| [MO2N_B1](#phase-mo-n-mo2n-b1); _phase:mo-n:mo2n-b1_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [MO2N_BETA](#phase-mo-n-mo2n-beta); _phase:mo-n:mo2n-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–941.97 K, x(N) 0.28199–0.3332 | 0 | 1 |
| [N2GAS](#phase-mo-n-n2gas); _phase:mo-n:n2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(N) 1–1 | 0 | 2 |

## BCC_A2 (Mo–N)

- Id: `phase:mo-n:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.14 K, x(N) 0–0.0019
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:bcc-a2)

Names (4): _corpus: _corpus:phase:mo-n:bcc-a2  
_paper: _paper:10.2298/jmmb210330011d:BCC_A2  
_tdb: _tdb:MoN-23Dac.tdb:BCC_A2, tdb:MoN-91Fri-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): BCC_A2, type code %B, sha256 `d0327d2feb226fde…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : MO : N VA% : !
~~~~

[MoN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-91Fri-LB.tdb): BCC_A2, type code %B, sha256 `1d4dea1aad84fb4b…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO : N VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90073-5](https://doi.org/10.1016/0022-5088%2878%2990073-5) Hermann Jehn, Peter Ettmayer, The molybdenum-nitrogen phase diagram, Journal of the Less Common Metals 58, 85-98 (1978).  
_cited as the source of values for this phase_

## FCC_A1 (Mo–N)

- Id: `phase:mo-n:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–1092.37 K, x(N) 0.30895–0.48355
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:fcc-a1)

Names (4): _corpus: _corpus:phase:mo-n:fcc-a1  
_paper: _paper:10.1016/0364-5916(91)90028-i:MoN  
_tdb: _tdb:MoN-23Dac.tdb:FCC_A1, tdb:MoN-91Fri-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): FCC_A1, type code %A, sha256 `d0327d2feb226fde…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : MO : N VA% : !
~~~~

[MoN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-91Fri-LB.tdb): FCC_A1, type code %A, sha256 `1d4dea1aad84fb4b…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO : N VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
_assessment that models this phase_

## HCP_A3 (Mo–N)

- Id: `phase:mo-n:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:hcp-a3)

Names (3): _corpus: _corpus:phase:mo-n:hcp-a3  
_tdb: _tdb:MoN-23Dac.tdb:HCP_A3, tdb:MoN-91Fri-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): HCP_A3, type code %, sha256 `d0327d2feb226fde…`

~~~~text
53: PHASE HCP_A3 % 2 1 0.5 !
54: CONST HCP_A3 : MO : N VA% : !
~~~~

[MoN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-91Fri-LB.tdb): HCP_A3, type code %, sha256 `1d4dea1aad84fb4b…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : MO : N VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
_assessment that models this phase_

## LIQUID (Mo–N)

- Id: `phase:mo-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2877.89–4000 K, x(N) 0–0.0096
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:liquid)

Names (4): _corpus: _corpus:phase:mo-n:liquid  
_paper: _paper:10.2298/jmmb210330011d:Liquid  
_tdb: _tdb:MoN-23Dac.tdb:LIQUID, tdb:MoN-91Fri-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): LIQUID, type code %, sha256 `d0327d2feb226fde…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : MO N : !
~~~~

[MoN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-91Fri-LB.tdb): LIQUID, type code %, sha256 `1d4dea1aad84fb4b…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO N : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(78)90073-5](https://doi.org/10.1016/0022-5088%2878%2990073-5) Hermann Jehn, Peter Ettmayer, The molybdenum-nitrogen phase diagram, Journal of the Less Common Metals 58, 85-98 (1978).  
_cited as the source of values for this phase_

## MC_SHP (Mo–N)

- Id: `phase:mo-n:mc-shp`; status `assigned`
- Structure: WC · B_h · hP2 · P-6m2 (187); type `st:b-h-wc-hp2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MC,SHP, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mo 0.5000, N 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–769.48 K, x(N) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:mc-shp)

Names (2): _corpus: _corpus:phase:mo-n:mc-shp  
_tdb: _tdb:MoN-23Dac.tdb:MC_SHP  


### TDB models of MC_SHP (1): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): MC_SHP, type code %, sha256 `d0327d2feb226fde…`

~~~~text
69: PHASE MC_SHP % 2 1 1 !
70: CONST MC_SHP : MO : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
_assessment that models this phase_

## MO2N_B1 (Mo–N)

- Id: `phase:mo-n:mo2n-b1`; status `needs_review`
- No structure assigned. Why: site_ratios_contradict_B1:MoN-23Dac.tdb
- Candidate (name_token): NaCl · B1 · cF8 · Fm-3m (225) — Strukturbericht/word 'B1' in the TDB name
- Candidate (sgte_mmc2): NaCl · B1 · cF8 · Fm-3m (225) — Hallstedt 2025 mmc2 row for MO2N_B1: Mo2N-gamma
- Candidate (tdb_comment): NaCl · cF8 · Fm-3m — MoN-23Dac.tdb: 'Prototype NaCl (cF8, Fm-3m), gamma'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:mo2n-b1)

Names (2): _corpus: _corpus:phase:mo-n:mo2n-b1  
_tdb: _tdb:MoN-23Dac.tdb:MO2N_B1  


### TDB models of MO2N_B1 (1): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): MO2N_B1, type code %, sha256 `d0327d2feb226fde…`

~~~~text
63: PHASE MO2N_B1 % 2 2 1 !
64: CONST MO2N_B1 : MO : N% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
_assessment that models this phase_

## MO2N_BETA (Mo–N)

- Id: `phase:mo-n:mo2n-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): Mo2N · tI12 · I4_1/amd (141) — Hallstedt 2025 mmc2 row for MO2N_BETA: Mo2N-beta
- Candidate (tdb_comment): Mo2N · tI12 · I4_1/amd, 141 — MoN-23Dac.tdb: 'Prototype Mo2N (tI12, I4_1/amd, 141)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–941.97 K, x(N) 0.28199–0.3332
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:mo2n-beta)

Names (2): _corpus: _corpus:phase:mo-n:mo2n-beta  
_tdb: _tdb:MoN-23Dac.tdb:MO2N_BETA  


### TDB models of MO2N_BETA (1): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): MO2N_BETA, type code %, sha256 `d0327d2feb226fde…`

~~~~text
58: PHASE MO2N_BETA % 2 2 1 !
59: CONST MO2N_BETA : MO : N% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
_assessment that models this phase_

## N2GAS (Mo–N)

- Id: `phase:mo-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-n:n2gas)

Names (3): _corpus: _corpus:phase:mo-n:n2gas  
_tdb: _tdb:MoN-23Dac.tdb:N2GAS, tdb:MoN-91Fri-LB.tdb:N2GAS  


### TDB models of N2GAS (2): PHASE and CONSTITUENT statements as written

[MoN-23Dac.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb): N2GAS, type code %, sha256 `d0327d2feb226fde…`

~~~~text
72: PHASE N2GAS % 1 1 !
73: CONST N2GAS : N2 : !
~~~~

[MoN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoN-91Fri-LB.tdb): N2GAS, type code %, sha256 `1d4dea1aad84fb4b…`

~~~~text
42: PHASE N2GAS % 1 1 !
43: CONST N2GAS : N2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_
- [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023).  
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
