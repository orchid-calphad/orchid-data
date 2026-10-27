# Te–Yb phases

> Te–Yb system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TE-YB.html · Markdown: https://data.orchid-project.org/phases/pages/TE-YB.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TE-YB) · [full JSON](https://data.orchid-project.org/phases/systems/TE-YB.json) · [Te–Yb system page](https://data.orchid-project.org/systems/TE-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/TE-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Te–Yb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-te-yb-a8-hexagonal); _phase:te-yb:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 2 | 2 |
| [BCC_A2](#phase-te-yb-bcc-a2); _phase:te-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1033–2500 K, x(Te) 0–0 | 2 | 2 |
| [FCC_A1](#phase-te-yb-fcc-a1); _phase:te-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1033 K, x(Te) 0–0 | 0 | 2 |
| [HCP_A3](#phase-te-yb-hcp-a3); _phase:te-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-te-yb-liquid); _phase:te-yb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 721.7–2500 K, x(Te) 0–1 | 6 | 2 |
| [YBTE_B1](#phase-te-yb-ybte-b1); _phase:te-yb:ybte-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2003.55 K, x(Te) 0.5–0.5 | 6 | 2 |

## HEXAGONAL_A8 (Te–Yb)

- Id: `phase:te-yb:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-yb:a8-hexagonal)

Names (5): _corpus: _corpus:phase:te-yb:a8-hexagonal, corpus:phase:te-yb:hexagonal-a8  
_paper: _paper:10.1016/j.jallcom.2015.03.224:(Te)  
_tdb: _tdb:YbTe-15Gha.tdb:HEXAGONAL_A8, tdb:YbTe-15Wan.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[YbTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Gha.tdb): HEXAGONAL_A8, type code %, sha256 `3ca7dcdce3986005…`

~~~~text
43: PHASE HEXAGONAL_A8 % 1 1 !
44: CONST HEXAGONAL_A8 : TE : !
~~~~

[YbTe-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Wan.tdb): HEXAGONAL_A8, type code %, sha256 `ffc72cd66dbb4e24…`

~~~~text
49: PHASE HEXAGONAL_A8 % 1 1 !
50: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## BCC_A2 (Te–Yb)

- Id: `phase:te-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Yb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 1033–2500 K, x(Te) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-yb:bcc-a2)

Names (4): _corpus: _corpus:phase:te-yb:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2015.03.224:(γYb)  
_tdb: _tdb:YbTe-15Gha.tdb:BCC_A2, tdb:YbTe-15Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[YbTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Gha.tdb): BCC_A2, type code %B, sha256 `3ca7dcdce3986005…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : YB : VA : !
~~~~

[YbTe-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Wan.tdb): BCC_A2, type code %B, sha256 `ffc72cd66dbb4e24…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : YB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## FCC_A1 (Te–Yb)

- Id: `phase:te-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Yb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1033 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:te-yb:fcc-a1  
_tdb: _tdb:YbTe-15Gha.tdb:FCC_A1, tdb:YbTe-15Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[YbTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Gha.tdb): FCC_A1, type code %A, sha256 `3ca7dcdce3986005…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : YB : VA : !
~~~~

[YbTe-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Wan.tdb): FCC_A1, type code %A, sha256 `ffc72cd66dbb4e24…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : YB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase_

## HCP_A3 (Te–Yb)

- Id: `phase:te-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Yb 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-yb:hcp-a3)

Names (3): _corpus: _corpus:phase:te-yb:hcp-a3  
_tdb: _tdb:YbTe-15Gha.tdb:HCP_A3, tdb:YbTe-15Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[YbTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Gha.tdb): HCP_A3, type code %A, sha256 `3ca7dcdce3986005…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : YB : VA: !
~~~~

[YbTe-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Wan.tdb): HCP_A3, type code %A, sha256 `ffc72cd66dbb4e24…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : YB : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase_

## LIQUID (Te–Yb)

- Id: `phase:te-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 721.7–2500 K, x(Te) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-yb:liquid)

Names (4): _corpus: _corpus:phase:te-yb:liquid  
_paper: _paper:10.1016/j.jallcom.2015.03.224:L  
_tdb: _tdb:YbTe-15Gha.tdb:LIQUID, tdb:YbTe-15Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[YbTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Gha.tdb): LIQUID, type code %, sha256 `3ca7dcdce3986005…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : TE YB : !
~~~~

[YbTe-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Wan.tdb): LIQUID, type code %, sha256 `ffc72cd66dbb4e24…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : TE YB YBTE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

## YBTE_B1 (Te–Yb)

- Id: `phase:te-yb:ybte-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Te 0.5000, Yb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2003.55 K, x(Te) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-yb:ybte-b1)

Names (4): _corpus: _corpus:phase:te-yb:ybte-b1  
_paper: _paper:10.1016/j.jallcom.2015.03.224:TeYb  
_tdb: _tdb:YbTe-15Gha.tdb:YBTE_B1, tdb:YbTe-15Wan.tdb:YBTE_B1  


### TDB models of YBTE_B1 (2): PHASE and CONSTITUENT statements as written

[YbTe-15Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Gha.tdb): YBTE_B1, type code %, sha256 `3ca7dcdce3986005…`

~~~~text
48: PHASE YBTE_B1 % 2 1 1 !
49: CONST YBTE_B1 : YB : TE : !
~~~~

[YbTe-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Wan.tdb): YBTE_B1, type code %, sha256 `ffc72cd66dbb4e24…`

~~~~text
54: PHASE YBTE_B1 % 2 1 1 !
55: CONST YBTE_B1 : YB : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, Thermodynamic modeling of the Eu–Te and Te–Yb systems, Journal of Alloys and Compounds 643, 121-128 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015).  
_assessment that models this phase_

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
