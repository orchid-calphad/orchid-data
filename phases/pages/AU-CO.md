# Au–Co phases

> Au–Co system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-CO.html · Markdown: https://data.orchid-project.org/phases/pages/AU-CO.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-CO) · [full JSON](https://data.orchid-project.org/phases/systems/AU-CO.json) · [Au–Co system page](https://data.orchid-project.org/systems/AU-CO.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-CO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Co system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-au-co-bcc-a2); _phase:au-co:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-au-co-fcc-a1); _phase:au-co:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.24 K, x(Co) 0–1 | 4 | 2 |
| [HCP_A3](#phase-au-co-hcp-a3); _phase:au-co:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–697.61 K, x(Co) 0.99865–1 | 2 | 2 |
| [LIQUID](#phase-au-co-liquid); _phase:au-co:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1270.51–2500 K, x(Co) 0–1 | 2 | 2 |

## BCC_A2 (Au–Co)

- Id: `phase:au-co:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-co:bcc-a2)

Names (3): _corpus: _corpus:phase:au-co:bcc-a2  
_tdb: _tdb:AuCo-04Kor-LB.tdb:BCC_A2, tdb:AuCo-09Don.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AuCo-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-04Kor-LB.tdb): BCC_A2, type code %B, sha256 `fe460222ed545fd8…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU CO : VA : !
~~~~

[AuCo-09Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-09Don.tdb): BCC_A2, type code %B, sha256 `bf5afe9f855266c5…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AU CO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-009-0874-4](https://doi.org/10.1007/s11664-009-0874-4) H. Q. Dong, S. Jin, L. G. Zhang, J. S. Wang, X. M. Tao, H. S. Liu et al., Thermodynamic Assessment of the Au-Co-Sn Ternary System, Journal of Elec Materi 38, 2158-2169 (2009).  
_assessment that models this phase_

## FCC_A1 (Au–Co)

- Id: `phase:au-co:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.24 K, x(Co) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-co:fcc-a1)

Names (5): _corpus: _corpus:phase:au-co:fcc-a1  
_paper: _paper:10.1007/s11664-009-0874-4:Au, paper:10.1007/s11664-009-0874-4:αCo  
_tdb: _tdb:AuCo-04Kor-LB.tdb:FCC_A1, tdb:AuCo-09Don.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AuCo-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-04Kor-LB.tdb): FCC_A1, type code %A, sha256 `fe460222ed545fd8…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU CO : VA : !
~~~~

[AuCo-09Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-09Don.tdb): FCC_A1, type code %A, sha256 `bf5afe9f855266c5…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AU CO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-009-0874-4](https://doi.org/10.1007/s11664-009-0874-4) H. Q. Dong, S. Jin, L. G. Zhang, J. S. Wang, X. M. Tao, H. S. Liu et al., Thermodynamic Assessment of the Au-Co-Sn Ternary System, Journal of Elec Materi 38, 2158-2169 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869509](https://doi.org/10.1007/bf02869509) H. Okamoto, T.B. Massalski, M. Hasebe, and T. Nishizawa, Bull. Alloy Phase Diagrams 6, 449 (1985).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Co)

- Id: `phase:au-co:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–697.61 K, x(Co) 0.99865–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-co:hcp-a3)

Names (4): _corpus: _corpus:phase:au-co:hcp-a3  
_paper: _paper:10.1007/s11664-009-0874-4:εCo  
_tdb: _tdb:AuCo-04Kor-LB.tdb:HCP_A3, tdb:AuCo-09Don.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AuCo-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-04Kor-LB.tdb): HCP_A3, type code %A, sha256 `fe460222ed545fd8…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU CO% : VA : !
~~~~

[AuCo-09Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-09Don.tdb): HCP_A3, type code %A, sha256 `bf5afe9f855266c5…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AU CO% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-009-0874-4](https://doi.org/10.1007/s11664-009-0874-4) H. Q. Dong, S. Jin, L. G. Zhang, J. S. Wang, X. M. Tao, H. S. Liu et al., Thermodynamic Assessment of the Au-Co-Sn Ternary System, Journal of Elec Materi 38, 2158-2169 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869509](https://doi.org/10.1007/bf02869509) H. Okamoto, T.B. Massalski, M. Hasebe, and T. Nishizawa, Bull. Alloy Phase Diagrams 6, 449 (1985).  
_cited as the source of values for this phase_

## LIQUID (Au–Co)

- Id: `phase:au-co:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1270.51–2500 K, x(Co) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-co:liquid)

Names (4): _corpus: _corpus:phase:au-co:liquid  
_paper: _paper:10.1007/s11664-009-0874-4:L  
_tdb: _tdb:AuCo-04Kor-LB.tdb:LIQUID, tdb:AuCo-09Don.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AuCo-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-04Kor-LB.tdb): LIQUID, type code %, sha256 `fe460222ed545fd8…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU CO : !
~~~~

[AuCo-09Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuCo-09Don.tdb): LIQUID, type code %, sha256 `bf5afe9f855266c5…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AU CO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-009-0874-4](https://doi.org/10.1007/s11664-009-0874-4) H. Q. Dong, S. Jin, L. G. Zhang, J. S. Wang, X. M. Tao, H. S. Liu et al., Thermodynamic Assessment of the Au-Co-Sn Ternary System, Journal of Elec Materi 38, 2158-2169 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869509](https://doi.org/10.1007/bf02869509) H. Okamoto, T.B. Massalski, M. Hasebe, and T. Nishizawa, Bull. Alloy Phase Diagrams 6, 449 (1985).  
_cited as the source of values for this phase_

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
