# Ba–Cu phases

> Ba–Cu system: 6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-CU.html · Markdown: https://data.orchid-project.org/phases/pages/BA-CU.md

6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-CU) · [full JSON](https://data.orchid-project.org/phases/systems/BA-CU.json) · [Ba–Cu system page](https://data.orchid-project.org/systems/BA-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–Cu system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BACU](#phase-ba-cu-bacu); _phase:ba-cu:bacu_ | BaCu · hP8 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–823.1 K, x(Cu) 0.5–0.5 | 0 | 2 |
| [BACU13_D23](#phase-ba-cu-bacu13-d23); _phase:ba-cu:bacu13-d23_ | NaZn13 · D2_3 · cF112 · Fm-3c (226) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1031.68 K, x(Cu) 0.92857–0.92857 | 0 | 2 |
| [BCC_A2](#phase-ba-cu-bcc-a2); _phase:ba-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1011.23 K, x(Cu) 0–2e-05 | 0 | 2 |
| [FCC_A1](#phase-ba-cu-fcc-a1); _phase:ba-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.94 K, x(Cu) 0.99999–1 | 0 | 2 |
| [HCP_A3](#phase-ba-cu-hcp-a3); _phase:ba-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ba-cu-liquid); _phase:ba-cu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 733.11–2500 K, x(Cu) 0–1 | 0 | 2 |

## BACU (Ba–Cu)

- Id: `phase:ba-cu:bacu`; status `assigned`
- Structure: BaCu · hP8 · P6_3/mmc (194); type `st:bacu-hp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ba 0.5000, Cu 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–823.1 K, x(Cu) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-cu:bacu)

Names (3): _corpus: _corpus:phase:ba-cu:bacu  
_tdb: _tdb:BaCu-93Kon-LB.tdb:BACU, tdb:BaCu-98Lys.tdb:BACU  


### TDB models of BACU (2): PHASE and CONSTITUENT statements as written

[BaCu-93Kon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-93Kon-LB.tdb): BACU, type code %, sha256 `1d51146aafb7ffe0…`

~~~~text
44: PHASE BACU % 2 1 1 !
45: CONST BACU : BA : CU : !
~~~~

[BaCu-98Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-98Lys.tdb): BACU, type code %, sha256 `23cbb93ece40a4f8…`

~~~~text
43: PHASE BACU % 2 1 1 !
44: CONST BACU : BA : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1993-840810](https://doi.org/10.1515/ijmr-1993-840810) R. Konetzki, R. Schmid-Fetzer, A. Watson, B. Argent, S.G. Fries, H.L. Lukas, Z. Metallkd., 84, 569-73(1993).  
_assessment that models this phase_

## BACU13_D23 (Ba–Cu)

- Id: `phase:ba-cu:bacu13-d23`; status `assigned`
- Structure: NaZn13 · D2_3 · cF112 · Fm-3c (226); type `st:d2-3-nazn13-cf112`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaays and oqmd-18752, space group 226
- Stoichiometry: Ba 0.0714, Cu 0.9286
- Stability: stable in 2 of 2 calculated diagram(s): 300–1031.68 K, x(Cu) 0.92857–0.92857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-cu:bacu13-d23)

Names (5): _corpus: _corpus:phase:ba-cu:bacu13-d23  
_mp: _mp:mp-aaaaaays  
_oqmd: _oqmd:oqmd-18752  
_tdb: _tdb:BaCu-93Kon-LB.tdb:BACU13_D23, tdb:BaCu-98Lys.tdb:BACU13_D23  


### TDB models of BACU13_D23 (2): PHASE and CONSTITUENT statements as written

[BaCu-93Kon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-93Kon-LB.tdb): BACU13_D23, type code %, sha256 `1d51146aafb7ffe0…`

~~~~text
49: PHASE BACU13_D23 % 2 1 13 !
50: CONST BACU13_D23 : BA : CU : !
~~~~

[BaCu-98Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-98Lys.tdb): BACU13_D23, type code %, sha256 `23cbb93ece40a4f8…`

~~~~text
48: PHASE BACU13_D23 % 2 1 13 !
49: CONST BACU13_D23 : BA : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1993-840810](https://doi.org/10.1515/ijmr-1993-840810) R. Konetzki, R. Schmid-Fetzer, A. Watson, B. Argent, S.G. Fries, H.L. Lukas, Z. Metallkd., 84, 569-73(1993).  
_assessment that models this phase_

## BCC_A2 (Ba–Cu)

- Id: `phase:ba-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1011.23 K, x(Cu) 0–2e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-cu:bcc-a2)

Names (3): _corpus: _corpus:phase:ba-cu:bcc-a2  
_tdb: _tdb:BaCu-93Kon-LB.tdb:BCC_A2, tdb:BaCu-98Lys.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BaCu-93Kon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-93Kon-LB.tdb): BCC_A2, type code %B, sha256 `1d51146aafb7ffe0…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : BA% CU : VA : !
~~~~

[BaCu-98Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-98Lys.tdb): BCC_A2, type code %B, sha256 `23cbb93ece40a4f8…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BA% CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1993-840810](https://doi.org/10.1515/ijmr-1993-840810) R. Konetzki, R. Schmid-Fetzer, A. Watson, B. Argent, S.G. Fries, H.L. Lukas, Z. Metallkd., 84, 569-73(1993).  
_assessment that models this phase_

## FCC_A1 (Ba–Cu)

- Id: `phase:ba-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.94 K, x(Cu) 0.99999–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-cu:fcc-a1)

Names (3): _corpus: _corpus:phase:ba-cu:fcc-a1  
_tdb: _tdb:BaCu-93Kon-LB.tdb:FCC_A1, tdb:BaCu-98Lys.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BaCu-93Kon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-93Kon-LB.tdb): FCC_A1, type code %A, sha256 `1d51146aafb7ffe0…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : BA CU% : VA : !
~~~~

[BaCu-98Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-98Lys.tdb): FCC_A1, type code %A, sha256 `23cbb93ece40a4f8…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BA CU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1993-840810](https://doi.org/10.1515/ijmr-1993-840810) R. Konetzki, R. Schmid-Fetzer, A. Watson, B. Argent, S.G. Fries, H.L. Lukas, Z. Metallkd., 84, 569-73(1993).  
_assessment that models this phase_

## HCP_A3 (Ba–Cu)

- Id: `phase:ba-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:ba-cu:hcp-a3  
_tdb: _tdb:BaCu-93Kon-LB.tdb:HCP_A3, tdb:BaCu-98Lys.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BaCu-93Kon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-93Kon-LB.tdb): HCP_A3, type code %A, sha256 `1d51146aafb7ffe0…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : BA CU : VA : !
~~~~

[BaCu-98Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-98Lys.tdb): HCP_A3, type code %A, sha256 `23cbb93ece40a4f8…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BA CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1993-840810](https://doi.org/10.1515/ijmr-1993-840810) R. Konetzki, R. Schmid-Fetzer, A. Watson, B. Argent, S.G. Fries, H.L. Lukas, Z. Metallkd., 84, 569-73(1993).  
_assessment that models this phase_

## LIQUID (Ba–Cu)

- Id: `phase:ba-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 733.11–2500 K, x(Cu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-cu:liquid)

Names (3): _corpus: _corpus:phase:ba-cu:liquid  
_tdb: _tdb:BaCu-93Kon-LB.tdb:LIQUID, tdb:BaCu-98Lys.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BaCu-93Kon-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-93Kon-LB.tdb): LIQUID, type code %, sha256 `1d51146aafb7ffe0…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : BA CU : !
~~~~

[BaCu-98Lys.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCu-98Lys.tdb): LIQUID, type code %, sha256 `23cbb93ece40a4f8…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BA CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1993-840810](https://doi.org/10.1515/ijmr-1993-840810) R. Konetzki, R. Schmid-Fetzer, A. Watson, B. Argent, S.G. Fries, H.L. Lukas, Z. Metallkd., 84, 569-73(1993).  
_assessment that models this phase_

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
