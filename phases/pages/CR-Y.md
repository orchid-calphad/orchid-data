# Cr–Y phases

> Cr–Y system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-Y.html · Markdown: https://data.orchid-project.org/phases/pages/CR-Y.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-Y) · [full JSON](https://data.orchid-project.org/phases/systems/CR-Y.json) · [Cr–Y system page](https://data.orchid-project.org/systems/CR-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Y system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-y-bcc-a2); _phase:cr-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.58 K, x(Y) 0–1 | 11 | 2 |
| [FCC_A1](#phase-cr-y-fcc-a1); _phase:cr-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 1580–1590 K | 0 | 2 |
| [HCP_A3](#phase-cr-y-hcp-a3); _phase:cr-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2172.93 K, x(Y) 0.99326–1 | 7 | 2 |
| [LIQUID](#phase-cr-y-liquid); _phase:cr-y:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1600–4000 K, x(Y) 0–1 | 11 | 2 |

## BCC_A2 (Cr–Y)

- Id: `phase:cr-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.58 K, x(Y) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-y:bcc-a2)

Names (5): _corpus: _corpus:phase:cr-y:bcc-a2  
_paper: _paper:10.1007/s11669-009-9581-3:Cr, paper:10.1007/s11669-009-9581-3:βY  
_tdb: _tdb:CrY-09Cha.tdb:BCC_A2, tdb:CrY-21Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CrY-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-09Cha.tdb): BCC_A2, type code %B, sha256 `eae96d9642ae594d…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR Y : VA : !
~~~~

[CrY-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-21Wan.tdb): BCC_A2, type code %B, sha256 `2261a8ac56309484…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CR Y : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102214](https://doi.org/10.1016/j.calphad.2020.102214) Y. Wang, M. Ostrowska, G. Cacciamani, Calphad, 72, 102214(2021).  
_assessment that models this phase_
- [doi:10.1007/bf02645392](https://doi.org/10.1007/bf02645392) H. Okamoto, Cr-Y (Chromium-Yttrium), J. Phase Equilib., 1992, 13, p 100-101 586 57.71 58 61.1 55.2 98.1 97.1 n/a n/a n/a n/a 0.02 Reference n/a n/a n/a 0.05 n/a 99.6 n/a n/a n/a n/a 99.3 Terekhova et al.\[14\] Venkatraman and Neumann\[15\] Okamoto\[5\] This study Okamoto\[5\] This study Terekhova et al.\[14\] Venkatraman and Neumann\[15\] Terekhova and Korzun\[20\] Okamoto\[5\] This study  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869503](https://doi.org/10.1007/bf02869503) M. Venkatraman and J.P. Neumann, The Cr-Y (ChromiumYttrium) System, Bull. Alloy Phase Diagr., 1985, 6, p 429-431  
_cited as the source of values for this phase_

## FCC_A1 (Cr–Y)

- Id: `phase:cr-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 1580–1590 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-y:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-y:fcc-a1  
_tdb: _tdb:CrY-09Cha.tdb:FCC_A1, tdb:CrY-21Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CrY-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-09Cha.tdb): FCC_A1, type code %A, sha256 `eae96d9642ae594d…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR Y : VA : !
~~~~

[CrY-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-21Wan.tdb): FCC_A1, type code %A, sha256 `2261a8ac56309484…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CR Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102214](https://doi.org/10.1016/j.calphad.2020.102214) Y. Wang, M. Ostrowska, G. Cacciamani, Calphad, 72, 102214(2021).  
_assessment that models this phase_

## HCP_A3 (Cr–Y)

- Id: `phase:cr-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2172.93 K, x(Y) 0.99326–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-y:hcp-a3)

Names (4): _corpus: _corpus:phase:cr-y:hcp-a3  
_paper: _paper:10.1007/s11669-009-9581-3:αY  
_tdb: _tdb:CrY-09Cha.tdb:HCP_A3, tdb:CrY-21Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CrY-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-09Cha.tdb): HCP_A3, type code %A, sha256 `eae96d9642ae594d…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR Y : VA : !
~~~~

[CrY-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-21Wan.tdb): HCP_A3, type code %A, sha256 `2261a8ac56309484…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CR Y : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102214](https://doi.org/10.1016/j.calphad.2020.102214) Y. Wang, M. Ostrowska, G. Cacciamani, Calphad, 72, 102214(2021).  
_assessment that models this phase_
- [doi:10.1007/bf02645392](https://doi.org/10.1007/bf02645392) H. Okamoto, Cr-Y (Chromium-Yttrium), J. Phase Equilib., 1992, 13, p 100-101 586 57.71 58 61.1 55.2 98.1 97.1 n/a n/a n/a n/a 0.02 Reference n/a n/a n/a 0.05 n/a 99.6 n/a n/a n/a n/a 99.3 Terekhova et al.\[14\] Venkatraman and Neumann\[15\] Okamoto\[5\] This study Okamoto\[5\] This study Terekhova et al.\[14\] Venkatraman and Neumann\[15\] Terekhova and Korzun\[20\] Okamoto\[5\] This study  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869503](https://doi.org/10.1007/bf02869503) M. Venkatraman and J.P. Neumann, The Cr-Y (ChromiumYttrium) System, Bull. Alloy Phase Diagr., 1985, 6, p 429-431  
_cited as the source of values for this phase_

## LIQUID (Cr–Y)

- Id: `phase:cr-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1600–4000 K, x(Y) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-y:liquid)

Names (4): _corpus: _corpus:phase:cr-y:liquid  
_paper: _paper:10.1007/s11669-009-9581-3:L2  
_tdb: _tdb:CrY-09Cha.tdb:LIQUID, tdb:CrY-21Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CrY-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-09Cha.tdb): LIQUID, type code %, sha256 `eae96d9642ae594d…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR Y : !
~~~~

[CrY-21Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrY-21Wan.tdb): LIQUID, type code %, sha256 `2261a8ac56309484…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CR Y : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102214](https://doi.org/10.1016/j.calphad.2020.102214) Y. Wang, M. Ostrowska, G. Cacciamani, Calphad, 72, 102214(2021).  
_assessment that models this phase_
- [doi:10.1007/bf02645392](https://doi.org/10.1007/bf02645392) H. Okamoto, Cr-Y (Chromium-Yttrium), J. Phase Equilib., 1992, 13, p 100-101 586 57.71 58 61.1 55.2 98.1 97.1 n/a n/a n/a n/a 0.02 Reference n/a n/a n/a 0.05 n/a 99.6 n/a n/a n/a n/a 99.3 Terekhova et al.\[14\] Venkatraman and Neumann\[15\] Okamoto\[5\] This study Okamoto\[5\] This study Terekhova et al.\[14\] Venkatraman and Neumann\[15\] Terekhova and Korzun\[20\] Okamoto\[5\] This study  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869503](https://doi.org/10.1007/bf02869503) M. Venkatraman and J.P. Neumann, The Cr-Y (ChromiumYttrium) System, Bull. Alloy Phase Diagr., 1985, 6, p 429-431  
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
