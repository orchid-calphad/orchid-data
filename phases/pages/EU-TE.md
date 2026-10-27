# Eu–Te phases

> Eu–Te system: 6 phases (tier A 3, liquid 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-TE.html · Markdown: https://data.orchid-project.org/phases/pages/EU-TE.md

6 phases (tier A 3, liquid 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-TE) · [full JSON](https://data.orchid-project.org/phases/systems/EU-TE.json) · [Eu–Te system page](https://data.orchid-project.org/systems/EU-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–Te system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-eu-te-a8-hexagonal); _phase:eu-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.48 K, x(Te) 1–1 | 2 | 2 |
| [BCC_A2](#phase-eu-te-bcc-a2); _phase:eu-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1098.31 K, x(Te) 0–0 | 3 | 2 |
| [EU3TE7](#phase-eu-te-eu3te7); _phase:eu-te:eu3te7_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–703 K, x(Te) 0.7–0.7 | 4 | 2 |
| [EU4TE7](#phase-eu-te-eu4te7); _phase:eu-te:eu4te7_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–793.01 K, x(Te) 0.63636–0.63636 | 4 | 2 |
| [EUTE_B1](#phase-eu-te-eute-b1); _phase:eu-te:eute-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1799.08 K, x(Te) 0.5–0.57439 | 8 | 2 |
| [LIQUID](#phase-eu-te-liquid); _phase:eu-te:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 683.23–2500 K, x(Te) 0–1 | 12 | 2 |

## HEXAGONAL_A8 (Eu–Te)

- Id: `phase:eu-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.48 K, x(Te) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-te:a8-hexagonal)

Names (5): _corpus: _corpus:phase:eu-te:a8-hexagonal, corpus:phase:eu-te:hexagonal-a8  
_paper: _paper:10.1016/j.jallcom.2015.03.224:(Te)  
_tdb: _tdb:EuTe-15Gha.tdb:HEXAGONAL_A8, tdb:EuTe-21Don.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[EuTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-15Gha.tdb): HEXAGONAL_A8, type code %, sha256 `fe1f8b4811f1b60f…`

~~~~text
39: PHASE HEXAGONAL_A8 % 1 1 !
40: CONST HEXAGONAL_A8 : TE : !
~~~~

[EuTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-21Don.tdb): HEXAGONAL_A8, type code %, sha256 `fd5d8bba8db3f01f…`

~~~~text
31: PHASE HEXAGONAL_A8 % 1 1 !
32: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## BCC_A2 (Eu–Te)

- Id: `phase:eu-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1098.31 K, x(Te) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-te:bcc-a2)

Names (4): _corpus: _corpus:phase:eu-te:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2015.03.224:(Eu)  
_tdb: _tdb:EuTe-15Gha.tdb:BCC_A2, tdb:EuTe-21Don.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[EuTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-15Gha.tdb): BCC_A2, type code %B, sha256 `fe1f8b4811f1b60f…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : EU : VA : !
~~~~

[EuTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-21Don.tdb): BCC_A2, type code %B, sha256 `fd5d8bba8db3f01f…`

~~~~text
24: PHASE BCC_A2 %B 2 1 3 !
25: CONST BCC_A2 : EU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## EU3TE7 (Eu–Te)

- Id: `phase:eu-te:eu3te7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Eu3Te7) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Eu3Te7) — Hallstedt 2025 mmc2 row for EU3TE7: Eu3Te7
- Stoichiometry: Eu 0.3000, Te 0.7000
- Stability: stable in 2 of 2 calculated diagram(s): 300–703 K, x(Te) 0.7–0.7
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-te:eu3te7)

Names (4): _corpus: _corpus:phase:eu-te:eu3te7  
_paper: _paper:10.1016/j.jallcom.2015.03.224:Eu3Te7  
_tdb: _tdb:EuTe-15Gha.tdb:EU3TE7, tdb:EuTe-21Don.tdb:EU3TE7  


### TDB models of EU3TE7 (2): PHASE and CONSTITUENT statements as written

[EuTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-15Gha.tdb): EU3TE7, type code %, sha256 `fe1f8b4811f1b60f…`

~~~~text
54: PHASE EU3TE7 % 2 3 7 !
55: CONST EU3TE7 : EU : TE : !
~~~~

[EuTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-21Don.tdb): EU3TE7, type code %, sha256 `fd5d8bba8db3f01f…`

~~~~text
46: PHASE EU3TE7 % 2 3 7 !
47: CONST EU3TE7 : EU : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## EU4TE7 (Eu–Te)

- Id: `phase:eu-te:eu4te7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Eu4Te7) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Eu4Te7) — Hallstedt 2025 mmc2 row for EU4TE7: Eu4Te7
- Stoichiometry: Eu 0.3636, Te 0.6364
- Stability: stable in 2 of 2 calculated diagram(s): 300–793.01 K, x(Te) 0.63636–0.63636
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-te:eu4te7)

Names (4): _corpus: _corpus:phase:eu-te:eu4te7  
_paper: _paper:10.1016/j.jallcom.2015.03.224:Eu4Te7  
_tdb: _tdb:EuTe-15Gha.tdb:EU4TE7, tdb:EuTe-21Don.tdb:EU4TE7  


### TDB models of EU4TE7 (2): PHASE and CONSTITUENT statements as written

[EuTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-15Gha.tdb): EU4TE7, type code %, sha256 `fe1f8b4811f1b60f…`

~~~~text
49: PHASE EU4TE7 % 2 4 7 !
50: CONST EU4TE7 : EU : TE : !
~~~~

[EuTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-21Don.tdb): EU4TE7, type code %, sha256 `fd5d8bba8db3f01f…`

~~~~text
41: PHASE EU4TE7 % 2 4 7 !
42: CONST EU4TE7 : EU : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## EUTE_B1 (Eu–Te)

- Id: `phase:eu-te:eute-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1799.08 K, x(Te) 0.5–0.57439
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-te:eute-b1)

Names (4): _corpus: _corpus:phase:eu-te:eute-b1  
_paper: _paper:10.1016/j.jallcom.2015.03.224:(EuTe)  
_tdb: _tdb:EuTe-15Gha.tdb:EUTE_B1, tdb:EuTe-21Don.tdb:EUTE_B1  


### TDB models of EUTE_B1 (2): PHASE and CONSTITUENT statements as written

[EuTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-15Gha.tdb): EUTE_B1, type code %, sha256 `fe1f8b4811f1b60f…`

~~~~text
44: PHASE EUTE_B1 % 2 1 1 !
45: CONST EUTE_B1 : EU% TE : TE : !
~~~~

[EuTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-21Don.tdb): EUTE_B1, type code %, sha256 `fd5d8bba8db3f01f…`

~~~~text
36: PHASE EUTE_B1 % 2 1 1 !
37: CONST EUTE_B1 : EU VA : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## LIQUID (Eu–Te)

- Id: `phase:eu-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 683.23–2500 K, x(Te) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-te:liquid)

Names (4): _corpus: _corpus:phase:eu-te:liquid  
_paper: _paper:10.1016/j.jallcom.2015.03.224:Liq  
_tdb: _tdb:EuTe-15Gha.tdb:LIQUID, tdb:EuTe-21Don.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[EuTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-15Gha.tdb): LIQUID, type code %, sha256 `fe1f8b4811f1b60f…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : EU TE : !
~~~~

[EuTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/EuTe-21Don.tdb): LIQUID, type code %, sha256 `fd5d8bba8db3f01f…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : EU TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
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
