# Mg–Pb phases

> Mg–Pb system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-PB.html · Markdown: https://data.orchid-project.org/phases/pages/MG-PB.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-PB) · [full JSON](https://data.orchid-project.org/phases/systems/MG-PB.json) · [Mg–Pb system page](https://data.orchid-project.org/systems/MG-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Pb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-pb-bcc-a2); _phase:mg-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-mg-pb-fcc-a1); _phase:mg-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–601.06 K, x(Pb) 0.93764–1 | 7 | 3 |
| [HCP_A3](#phase-mg-pb-hcp-a3); _phase:mg-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–927 K, x(Pb) 0–0.0871 | 18 | 3 |
| [LIQUID](#phase-mg-pb-liquid); _phase:mg-pb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 517.29–2500 K, x(Pb) 0–1 | 73 | 3 |
| [MG2PB_C1](#phase-mg-pb-mg2pb-c1); _phase:mg-pb:mg2pb-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–823.81 K, x(Pb) 0.33333–0.33333 | 39 | 3 |

## BCC_A2 (Mg–Pb)

- Id: `phase:mg-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pb:bcc-a2)

Names (4): _corpus: _corpus:phase:mg-pb:bcc-a2  
_tdb: _tdb:MgPb-14Zha-ass.tdb:BCC_A2, tdb:MgPb-14Zha-sub.tdb:BCC_A2, tdb:MgPb-21Deb.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MgPb-14Zha-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-ass.tdb): BCC_A2, type code %B, sha256 `85fd9842fb3b047b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : MG PB : VA : !
~~~~

[MgPb-14Zha-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-sub.tdb): BCC_A2, type code %B, sha256 `715ddff6aaa4430b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MG PB : VA : !
~~~~

[MgPb-21Deb.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-21Deb.tdb): BCC_A2, type code %B, sha256 `c150e3ea46f0693a…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : MG PB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2020.158396](https://doi.org/10.1016/j.jallcom.2020.158396) A. Dębski, W. Gierlotka, S. Terlicka, W. Gąsior, On the Mg-Pb system. Calorimetric studies and thermodynamic calculations, Journal of Alloys and Compounds 861, 158396 (2021).  
_assessment that models this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_

## FCC_A1 (Mg–Pb)

- Id: `phase:mg-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–601.06 K, x(Pb) 0.93764–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pb:fcc-a1)

Names (5): _corpus: _corpus:phase:mg-pb:fcc-a1  
_paper: _paper:10.2298/jmmb130824017z:(Pb)  
_tdb: _tdb:MgPb-14Zha-ass.tdb:FCC_A1, tdb:MgPb-14Zha-sub.tdb:FCC_A1, tdb:MgPb-21Deb.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MgPb-14Zha-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-ass.tdb): FCC_A1, type code %A, sha256 `85fd9842fb3b047b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : MG PB% : VA : !
~~~~

[MgPb-14Zha-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-sub.tdb): FCC_A1, type code %A, sha256 `715ddff6aaa4430b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MG PB% : VA : !
~~~~

[MgPb-21Deb.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-21Deb.tdb): FCC_A1, type code %A, sha256 `c150e3ea46f0693a…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : MG PB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2020.158396](https://doi.org/10.1016/j.jallcom.2020.158396) A. Dębski, W. Gierlotka, S. Terlicka, W. Gąsior, On the Mg-Pb system. Calorimetric studies and thermodynamic calculations, Journal of Alloys and Compounds 861, 158396 (2021).  
_assessment that models this phase_

## HCP_A3 (Mg–Pb)

- Id: `phase:mg-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–927 K, x(Pb) 0–0.0871
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pb:hcp-a3)

Names (7): _corpus: _corpus:phase:mg-pb:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2020.158396:HCP_A3 (Mg), paper:10.1016/j.jallcom.2020.158396:HCP_A3(Mg), paper:10.2298/jmmb130824017z:(Mg)  
_tdb: _tdb:MgPb-14Zha-ass.tdb:HCP_A3, tdb:MgPb-14Zha-sub.tdb:HCP_A3, tdb:MgPb-21Deb.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MgPb-14Zha-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-ass.tdb): HCP_A3, type code %A, sha256 `85fd9842fb3b047b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : MG% PB : VA : !
~~~~

[MgPb-14Zha-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-sub.tdb): HCP_A3, type code %A, sha256 `715ddff6aaa4430b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : MG% PB : VA : !
~~~~

[MgPb-21Deb.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-21Deb.tdb): HCP_A3, type code %A, sha256 `c150e3ea46f0693a…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : MG% PB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2020.158396](https://doi.org/10.1016/j.jallcom.2020.158396) A. Dębski, W. Gierlotka, S. Terlicka, W. Gąsior, On the Mg-Pb system. Calorimetric studies and thermodynamic calculations, Journal of Alloys and Compounds 861, 158396 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19050440107](https://doi.org/10.1002/zaac.19050440107) G. Grube, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. V. Über Magnesium‐Bleilegierungen, Z. Anorg. Chem. 44, 117-130 (1905).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871188](https://doi.org/10.1007/bf02871188) A.A. Nayeb-Hashemi, J.B. Clark, The Mg-Pb (magnesium-lead) system, Bull. Alloy Phase Diag. 6 (1985) 56–66.  
_cited as the source of values for this phase_

## LIQUID (Mg–Pb)

- Id: `phase:mg-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 517.29–2500 K, x(Pb) 0–1
- Literature: 73 values (73 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pb:liquid)

Names (7): _corpus: _corpus:phase:mg-pb:liquid  
_paper: _paper:10.1016/j.jallcom.2020.158396:L, paper:10.1016/j.jallcom.2020.158396:liquid, paper:10.2298/jmmb130824017z:Liquid  
_tdb: _tdb:MgPb-14Zha-ass.tdb:LIQUID, tdb:MgPb-14Zha-sub.tdb:LIQUID, tdb:MgPb-21Deb.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MgPb-14Zha-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-ass.tdb): LIQUID, type code %, sha256 `85fd9842fb3b047b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : MG MG2PB PB : !
~~~~

[MgPb-14Zha-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-sub.tdb): LIQUID, type code %, sha256 `715ddff6aaa4430b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MG PB : !
~~~~

[MgPb-21Deb.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-21Deb.tdb): LIQUID, type code %, sha256 `c150e3ea46f0693a…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : MG MG2PB PB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2020.158396](https://doi.org/10.1016/j.jallcom.2020.158396) A. Dębski, W. Gierlotka, S. Terlicka, W. Gąsior, On the Mg-Pb system. Calorimetric studies and thermodynamic calculations, Journal of Alloys and Compounds 861, 158396 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19050440107](https://doi.org/10.1002/zaac.19050440107) G. Grube, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. V. Über Magnesium‐Bleilegierungen, Z. Anorg. Chem. 44, 117-130 (1905).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871188](https://doi.org/10.1007/bf02871188) A.A. Nayeb-Hashemi, J.B. Clark, The Mg-Pb (magnesium-lead) system, Bull. Alloy Phase Diag. 6 (1985) 56–66.  
_cited as the source of values for this phase_

## MG2PB_C1 (Mg–Pb)

- Id: `phase:mg-pb:mg2pb-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaberc and oqmd-17637, space group 225
- Stoichiometry: Mg 0.6667, Pb 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–823.81 K, x(Pb) 0.33333–0.33333
- Literature: 39 values (39 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-pb:mg2pb-c1)

Names (8): _corpus: _corpus:phase:mg-pb:mg2pb-c1  
_mp: _mp:mp-aaaaberc  
_oqmd: _oqmd:oqmd-17637  
_paper: _paper:10.1016/j.jallcom.2020.158396:Mg2Pb, paper:10.2298/jmmb130824017z:Mg2Pb  
_tdb: _tdb:MgPb-14Zha-ass.tdb:MG2PB_C1, tdb:MgPb-14Zha-sub.tdb:MG2PB_C1, tdb:MgPb-21Deb.tdb:MG2PB_C1  


### TDB models of MG2PB_C1 (3): PHASE and CONSTITUENT statements as written

[MgPb-14Zha-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-ass.tdb): MG2PB_C1, type code %, sha256 `85fd9842fb3b047b…`

~~~~text
50: PHASE MG2PB_C1 % 2 2 1 !
51: CONST MG2PB_C1 : MG : PB : !
~~~~

[MgPb-14Zha-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-14Zha-sub.tdb): MG2PB_C1, type code %, sha256 `715ddff6aaa4430b…`

~~~~text
46: PHASE MG2PB_C1 % 2 2 1 !
47: CONST MG2PB_C1 : MG : PB : !
~~~~

[MgPb-21Deb.tdb](https://orchid-project.org/data/databases/sgte-binary/MgPb-21Deb.tdb): MG2PB_C1, type code %, sha256 `c150e3ea46f0693a…`

~~~~text
52: PHASE MG2PB_C1 % 2 2 1 !
53: CONST MG2PB_C1 : MG : PB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2020.158396](https://doi.org/10.1016/j.jallcom.2020.158396) A. Dębski, W. Gierlotka, S. Terlicka, W. Gąsior, On the Mg-Pb system. Calorimetric studies and thermodynamic calculations, Journal of Alloys and Compounds 861, 158396 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19050440107](https://doi.org/10.1002/zaac.19050440107) G. Grube, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. V. Über Magnesium‐Bleilegierungen, Z. Anorg. Chem. 44, 117-130 (1905).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871188](https://doi.org/10.1007/bf02871188) A.A. Nayeb-Hashemi, J.B. Clark, The Mg-Pb (magnesium-lead) system, Bull. Alloy Phase Diag. 6 (1985) 56–66.  
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
