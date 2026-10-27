# Fe–In phases

> Fe–In system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-IN.html · Markdown: https://data.orchid-project.org/phases/pages/FE-IN.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-IN) · [full JSON](https://data.orchid-project.org/phases/systems/FE-IN.json) · [Fe–In system page](https://data.orchid-project.org/systems/FE-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–In system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-fe-in-a6-tetragonal); _phase:fe-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(In) 1–1 | 1 | 1 |
| [BCC_A2](#phase-fe-in-bcc-a2); _phase:fe-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1810.95 K, x(In) 0–0.00919 | 4 | 1 |
| [FCC_A1](#phase-fe-in-fcc-a1); _phase:fe-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1184.82–1692.46 K, x(In) 0–0.00645 | 2 | 1 |
| [HCP_A3](#phase-fe-in-hcp-a3); _phase:fe-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-fe-in-liquid); _phase:fe-in:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(In) 0–1 | 5 | 1 |

## TETRAGONAL_A6 (Fe–In)

- Id: `phase:fe-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(In) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-in:a6-tetragonal)

Names (4): _corpus: _corpus:phase:fe-in:a6-tetragonal, corpus:phase:fe-in:tetragonal-a6  
_paper: _paper:10.2320/matertrans.mer2008437:In  
_tdb: _tdb:FeIn-09Ohn.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[FeIn-09Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeIn-09Ohn.tdb): TETRAGONAL_A6, type code %, sha256 `199a9d26cb33c1fc…`

~~~~text
43: PHASE TETRAGONAL_A6 % 1 1 !
44: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MER2008437](https://doi.org/10.2320/matertrans.MER2008437) M. Ohno, K. Yoh, Mater. Trans. (JIM), 50, 1202-7(2009).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Fe–In)

- Id: `phase:fe-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1810.95 K, x(In) 0–0.00919
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-in:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-in:bcc-a2  
_paper: _paper:10.2320/matertrans.mer2008437:(αFe), paper:10.2320/matertrans.mer2008437:(δFe)  
_tdb: _tdb:FeIn-09Ohn.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[FeIn-09Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeIn-09Ohn.tdb): BCC_A2, type code %B, sha256 `199a9d26cb33c1fc…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MER2008437](https://doi.org/10.2320/matertrans.MER2008437) M. Ohno, K. Yoh, Mater. Trans. (JIM), 50, 1202-7(2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Fe–In)

- Id: `phase:fe-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1184.82–1692.46 K, x(In) 0–0.00645
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-in:fcc-a1)

Names (3): _corpus: _corpus:phase:fe-in:fcc-a1  
_paper: _paper:10.2320/matertrans.mer2008437:(γFe)  
_tdb: _tdb:FeIn-09Ohn.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[FeIn-09Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeIn-09Ohn.tdb): FCC_A1, type code %A, sha256 `199a9d26cb33c1fc…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MER2008437](https://doi.org/10.2320/matertrans.MER2008437) M. Ohno, K. Yoh, Mater. Trans. (JIM), 50, 1202-7(2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Fe–In)

- Id: `phase:fe-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-in:hcp-a3)

Names (2): _corpus: _corpus:phase:fe-in:hcp-a3  
_tdb: _tdb:FeIn-09Ohn.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[FeIn-09Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeIn-09Ohn.tdb): HCP_A3, type code %A, sha256 `199a9d26cb33c1fc…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MER2008437](https://doi.org/10.2320/matertrans.MER2008437) M. Ohno, K. Yoh, Mater. Trans. (JIM), 50, 1202-7(2009).  
_assessment that models this phase_

## LIQUID (Fe–In)

- Id: `phase:fe-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(In) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-in:liquid)

Names (4): _corpus: _corpus:phase:fe-in:liquid  
_paper: _paper:10.2320/matertrans.mer2008437:L, paper:10.2320/matertrans.mer2008437:L2  
_tdb: _tdb:FeIn-09Ohn.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[FeIn-09Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeIn-09Ohn.tdb): LIQUID, type code %, sha256 `199a9d26cb33c1fc…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.MER2008437](https://doi.org/10.2320/matertrans.MER2008437) M. Ohno, K. Yoh, Mater. Trans. (JIM), 50, 1202-7(2009).  
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
