# Nb–Re phases

> Nb–Re system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-RE.html · Markdown: https://data.orchid-project.org/phases/pages/NB-RE.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-RE) · [full JSON](https://data.orchid-project.org/phases/systems/NB-RE.json) · [Nb–Re system page](https://data.orchid-project.org/systems/NB-RE.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-RE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Re system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [CHI_A12](#phase-nb-re-a12-chi); _phase:nb-re:a12-chi_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3018.52 K, x(Re) 0.60144–0.90044 | 24 | 2 |
| [BCC_A2](#phase-nb-re-bcc-a2); _phase:nb-re:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2779.46 K, x(Re) 0–0.46955 | 10 | 2 |
| [SIGMA_D8B](#phase-nb-re-d8b-sigma); _phase:nb-re:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2435.76–2831.78 K, x(Re) 0.52522–0.59992 | 21 | 2 |
| [FCC_A1](#phase-nb-re-fcc-a1); _phase:nb-re:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-nb-re-hcp-a3); _phase:nb-re:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.23 K, x(Re) 0.97513–1 | 5 | 2 |
| [LIQUID](#phase-nb-re-liquid); _phase:nb-re:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2703.45–4000 K, x(Re) 0–1 | 15 | 2 |

## CHI_A12 (Nb–Re)

- Id: `phase:nb-re:a12-chi`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3018.52 K, x(Re) 0.60144–0.90044
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-re:a12-chi)

Names (7): _corpus: _corpus:phase:nb-re:a12-chi, corpus:phase:nb-re:chi-a12  
_paper: _paper:10.1016/j.calphad.2013.02.006:(χ), paper:10.1016/j.calphad.2013.02.006:χ, paper:10.1016/j.calphad.2020.101797:χ  
_tdb: _tdb:NbRe-13Liu.tdb:CHI_A12, tdb:NbRe-20Yen.tdb:CHI_A12  


### TDB models of CHI_A12 (2): PHASE and CONSTITUENT statements as written

[NbRe-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-13Liu.tdb): CHI_A12, type code %, sha256 `9127581a18abfbf7…`

~~~~text
40: PHASE CHI_A12 % 3 24 10 24 !
41: CONST CHI_A12 : RE : NB RE : NB RE : !
~~~~

[NbRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-20Yen.tdb): CHI_A12, type code %, sha256 `a3f16c73704aef3b…`

~~~~text
40: PHASE CHI_A12 % 3 24 10 24 !
41: CONST CHI_A12 : RE : NB RE : NB RE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006) Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Nb–Re)

- Id: `phase:nb-re:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2779.46 K, x(Re) 0–0.46955
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-re:bcc-a2)

Names (5): _corpus: _corpus:phase:nb-re:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.02.006:bcc, paper:10.1016/j.calphad.2020.101797:bcc  
_tdb: _tdb:NbRe-13Liu.tdb:BCC_A2, tdb:NbRe-20Yen.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NbRe-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-13Liu.tdb): BCC_A2, type code %B, sha256 `9127581a18abfbf7…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NB% RE : VA : !
~~~~

[NbRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-20Yen.tdb): BCC_A2, type code %B, sha256 `a3f16c73704aef3b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NB% RE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006) Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013).  
_assessment that models this phase; reports values for this phase_

## SIGMA_D8B (Nb–Re)

- Id: `phase:nb-re:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbRe-20Yen.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 2435.76–2831.78 K, x(Re) 0.52522–0.59992
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-re:d8b-sigma)

Names (7): _corpus: _corpus:phase:nb-re:d8b-sigma, corpus:phase:nb-re:sigma-d8b  
_paper: _paper:10.1016/j.calphad.2013.02.006:(σ), paper:10.1016/j.calphad.2013.02.006:σ, paper:10.1016/j.calphad.2020.101797:σ  
_tdb: _tdb:NbRe-13Liu.tdb:SIGMA_D8B, tdb:NbRe-20Yen.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (2): PHASE and CONSTITUENT statements as written

[NbRe-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-13Liu.tdb): SIGMA_D8B, type code %, sha256 `9127581a18abfbf7…`

~~~~text
45: PHASE SIGMA_D8B % 3 10 4 16 !
46: CONST SIGMA_D8B : RE : NB : NB RE : !
~~~~

[NbRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-20Yen.tdb): SIGMA_D8B, type code %, sha256 `a3f16c73704aef3b…`

~~~~text
45: PHASE SIGMA_D8B % 3 10 4 16 !
46: CONST SIGMA_D8B : RE : NB RE : NB RE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006) Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Nb–Re)

- Id: `phase:nb-re:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-re:fcc-a1)

Names (3): _corpus: _corpus:phase:nb-re:fcc-a1  
_tdb: _tdb:NbRe-13Liu.tdb:FCC_A1, tdb:NbRe-20Yen.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NbRe-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-13Liu.tdb): FCC_A1, type code %A, sha256 `9127581a18abfbf7…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NB RE : VA : !
~~~~

[NbRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-20Yen.tdb): FCC_A1, type code %A, sha256 `a3f16c73704aef3b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NB RE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006) Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_

## HCP_A3 (Nb–Re)

- Id: `phase:nb-re:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.23 K, x(Re) 0.97513–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-re:hcp-a3)

Names (5): _corpus: _corpus:phase:nb-re:hcp-a3  
_paper: _paper:10.1016/j.calphad.2013.02.006:hcp, paper:10.1016/j.calphad.2020.101797:hcp  
_tdb: _tdb:NbRe-13Liu.tdb:HCP_A3, tdb:NbRe-20Yen.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NbRe-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-13Liu.tdb): HCP_A3, type code %A, sha256 `9127581a18abfbf7…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NB RE% : VA : !
~~~~

[NbRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-20Yen.tdb): HCP_A3, type code %A, sha256 `a3f16c73704aef3b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NB RE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006) Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Nb–Re)

- Id: `phase:nb-re:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2703.45–4000 K, x(Re) 0–1
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-re:liquid)

Names (5): _corpus: _corpus:phase:nb-re:liquid  
_paper: _paper:10.1016/j.calphad.2013.02.006:L, paper:10.1016/j.calphad.2020.101797:L  
_tdb: _tdb:NbRe-13Liu.tdb:LIQUID, tdb:NbRe-20Yen.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NbRe-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-13Liu.tdb): LIQUID, type code %, sha256 `9127581a18abfbf7…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NB RE : !
~~~~

[NbRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbRe-20Yen.tdb): LIQUID, type code %, sha256 `a3f16c73704aef3b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NB RE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.02.006](https://doi.org/10.1016/j.calphad.2013.02.006) Xuan L. Liu, Chelsey Z. Hargather, Zi-Kui Liu, First-principles aided thermodynamic modeling of the Nb–Re system, Calphad 41, 119-127 (2013).  
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
