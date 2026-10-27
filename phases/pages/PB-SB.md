# Pb–Sb phases

> Pb–Sb system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-SB.html · Markdown: https://data.orchid-project.org/phases/pages/PB-SB.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-SB) · [full JSON](https://data.orchid-project.org/phases/systems/PB-SB.json) · [Pb–Sb system page](https://data.orchid-project.org/systems/PB-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Sb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-pb-sb-a7-rhombohedral); _phase:pb-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–903.78 K, x(Sb) 0.97572–1 | 5 | 4 |
| [BCC_A2](#phase-pb-sb-bcc-a2); _phase:pb-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-pb-sb-fcc-a1); _phase:pb-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(Sb) 0–0.58047 | 5 | 4 |
| [HCP_A3](#phase-pb-sb-hcp-a3); _phase:pb-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-pb-sb-liquid); _phase:pb-sb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 522.19–2500 K, x(Sb) 0–1 | 19 | 4 |

## RHOMBOHEDRAL_A7 (Pb–Sb)

- Id: `phase:pb-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–903.78 K, x(Sb) 0.97572–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sb:a7-rhombohedral)

Names (7): _corpus: _corpus:phase:pb-sb:a7-rhombohedral, corpus:phase:pb-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.jallcom.2008.09.002:rhombo(Sb)  
_tdb: _tdb:PbSb-09Has.tdb:RHOMBOHEDRAL_A7, tdb:PbSb-13Gie.tdb:RHOMBOHEDRAL_A7, tdb:PbSb-94Lee.tdb:RHOMBOHEDRAL_A7, tdb:PbSb-95Oht-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (4): PHASE and CONSTITUENT statements as written

[PbSb-09Has.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-09Has.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `2166e8958db172ec…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : PB SB% : !
~~~~

[PbSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-13Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `dfa5cb119cb28aaa…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : PB SB% : !
~~~~

[PbSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-94Lee.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `880084b4a6eaac54…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : PB SB% : !
~~~~

[PbSb-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-95Oht-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `138f59b0ca163055…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : PB SB% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.002](https://doi.org/10.1016/j.jallcom.2008.09.002) S. Hassam, D. Boa, Y. Fouque, K.P. Kotchi, J. Rogez, Thermodynamic investigation of the Pb – Sb system, Journal of Alloys and Compounds 476, 74-78 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0252-z](https://doi.org/10.1007/s11669-013-0252-z) W. Gierlotka, C. Lee, P. Chumpanaya, M.A. Rahman, T.-N. Ko, J. Phase Equilib. Diffus., 34, 421-24(2013).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02873711](https://doi.org/10.1007/bf02873711) S. Ashtakala, A. D. Pelton, C. W. Bale, The Pb−Sb (Lead-Antimony) system, Bulletin of Alloy Phase Diagrams 2, 86-89 (1981).  
_cited as the source of values for this phase_

## BCC_A2 (Pb–Sb)

- Id: `phase:pb-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sb:bcc-a2)

Names (5): _corpus: _corpus:phase:pb-sb:bcc-a2  
_tdb: _tdb:PbSb-09Has.tdb:BCC_A2, tdb:PbSb-13Gie.tdb:BCC_A2, tdb:PbSb-94Lee.tdb:BCC_A2, tdb:PbSb-95Oht-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[PbSb-09Has.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-09Has.tdb): BCC_A2, type code %B, sha256 `2166e8958db172ec…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PB SB : VA : !
~~~~

[PbSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-13Gie.tdb): BCC_A2, type code %B, sha256 `dfa5cb119cb28aaa…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : PB SB : VA : !
~~~~

[PbSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-94Lee.tdb): BCC_A2, type code %B, sha256 `880084b4a6eaac54…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : PB SB : VA : !
~~~~

[PbSb-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-95Oht-LB.tdb): BCC_A2, type code %B, sha256 `138f59b0ca163055…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : PB SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0252-z](https://doi.org/10.1007/s11669-013-0252-z) W. Gierlotka, C. Lee, P. Chumpanaya, M.A. Rahman, T.-N. Ko, J. Phase Equilib. Diffus., 34, 421-24(2013).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.09.002](https://doi.org/10.1016/j.jallcom.2008.09.002) S. Hassam, D. Boa, Y. Fouque, K.P. Kotchi, J. Rogez, Thermodynamic investigation of the Pb – Sb system, Journal of Alloys and Compounds 476, 74-78 (2009).  
_assessment that models this phase_

## FCC_A1 (Pb–Sb)

- Id: `phase:pb-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(Sb) 0–0.58047
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sb:fcc-a1)

Names (6): _corpus: _corpus:phase:pb-sb:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2008.09.002:fcc(Pb)  
_tdb: _tdb:PbSb-09Has.tdb:FCC_A1, tdb:PbSb-13Gie.tdb:FCC_A1, tdb:PbSb-94Lee.tdb:FCC_A1, tdb:PbSb-95Oht-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[PbSb-09Has.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-09Has.tdb): FCC_A1, type code %A, sha256 `2166e8958db172ec…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PB% SB : VA : !
~~~~

[PbSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-13Gie.tdb): FCC_A1, type code %A, sha256 `dfa5cb119cb28aaa…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : PB% SB : VA : !
~~~~

[PbSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-94Lee.tdb): FCC_A1, type code %A, sha256 `880084b4a6eaac54…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : PB% SB : VA : !
~~~~

[PbSb-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-95Oht-LB.tdb): FCC_A1, type code %A, sha256 `138f59b0ca163055…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : PB% SB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.002](https://doi.org/10.1016/j.jallcom.2008.09.002) S. Hassam, D. Boa, Y. Fouque, K.P. Kotchi, J. Rogez, Thermodynamic investigation of the Pb – Sb system, Journal of Alloys and Compounds 476, 74-78 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0252-z](https://doi.org/10.1007/s11669-013-0252-z) W. Gierlotka, C. Lee, P. Chumpanaya, M.A. Rahman, T.-N. Ko, J. Phase Equilib. Diffus., 34, 421-24(2013).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02873711](https://doi.org/10.1007/bf02873711) S. Ashtakala, A. D. Pelton, C. W. Bale, The Pb−Sb (Lead-Antimony) system, Bulletin of Alloy Phase Diagrams 2, 86-89 (1981).  
_cited as the source of values for this phase_

## HCP_A3 (Pb–Sb)

- Id: `phase:pb-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sb:hcp-a3)

Names (5): _corpus: _corpus:phase:pb-sb:hcp-a3  
_tdb: _tdb:PbSb-09Has.tdb:HCP_A3, tdb:PbSb-13Gie.tdb:HCP_A3, tdb:PbSb-94Lee.tdb:HCP_A3, tdb:PbSb-95Oht-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[PbSb-09Has.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-09Has.tdb): HCP_A3, type code %A, sha256 `2166e8958db172ec…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PB SB : VA : !
~~~~

[PbSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-13Gie.tdb): HCP_A3, type code %A, sha256 `dfa5cb119cb28aaa…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : PB SB : VA : !
~~~~

[PbSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-94Lee.tdb): HCP_A3, type code %A, sha256 `880084b4a6eaac54…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : PB SB : VA : !
~~~~

[PbSb-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-95Oht-LB.tdb): HCP_A3, type code %A, sha256 `138f59b0ca163055…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : PB SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0252-z](https://doi.org/10.1007/s11669-013-0252-z) W. Gierlotka, C. Lee, P. Chumpanaya, M.A. Rahman, T.-N. Ko, J. Phase Equilib. Diffus., 34, 421-24(2013).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.09.002](https://doi.org/10.1016/j.jallcom.2008.09.002) S. Hassam, D. Boa, Y. Fouque, K.P. Kotchi, J. Rogez, Thermodynamic investigation of the Pb – Sb system, Journal of Alloys and Compounds 476, 74-78 (2009).  
_assessment that models this phase_

## LIQUID (Pb–Sb)

- Id: `phase:pb-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 522.19–2500 K, x(Sb) 0–1
- Literature: 19 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sb:liquid)

Names (8): _corpus: _corpus:phase:pb-sb:liquid  
_paper: _paper:10.1007/bf02645349:liquid, paper:10.1016/j.jallcom.2008.09.002:L, paper:10.1016/j.jallcom.2008.09.002:liquid  
_tdb: _tdb:PbSb-09Has.tdb:LIQUID, tdb:PbSb-13Gie.tdb:LIQUID, tdb:PbSb-94Lee.tdb:LIQUID, tdb:PbSb-95Oht-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[PbSb-09Has.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-09Has.tdb): LIQUID, type code %, sha256 `2166e8958db172ec…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PB SB : !
~~~~

[PbSb-13Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-13Gie.tdb): LIQUID, type code %, sha256 `dfa5cb119cb28aaa…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : PB SB : !
~~~~

[PbSb-94Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-94Lee.tdb): LIQUID, type code %, sha256 `880084b4a6eaac54…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : PB SB : !
~~~~

[PbSb-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSb-95Oht-LB.tdb): LIQUID, type code %, sha256 `138f59b0ca163055…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : PB SB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.002](https://doi.org/10.1016/j.jallcom.2008.09.002) S. Hassam, D. Boa, Y. Fouque, K.P. Kotchi, J. Rogez, Thermodynamic investigation of the Pb – Sb system, Journal of Alloys and Compounds 476, 74-78 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-013-0252-z](https://doi.org/10.1007/s11669-013-0252-z) W. Gierlotka, C. Lee, P. Chumpanaya, M.A. Rahman, T.-N. Ko, J. Phase Equilib. Diffus., 34, 421-24(2013).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90857-5](https://doi.org/10.1016/0925-8388%2894%2990857-5) Byung-Zu Lee, Chang-Seok Oh, Dong Nyung Lee, A thermodynamic evaluation of the AgPbSb system, Journal of Alloys and Compounds 215, 293-301 (1994).  
_assessment that models this phase_
- [doi:10.1007/bf02873711](https://doi.org/10.1007/bf02873711) S. Ashtakala, A. D. Pelton, C. W. Bale, The Pb−Sb (Lead-Antimony) system, Bulletin of Alloy Phase Diagrams 2, 86-89 (1981).  
_cited as the source of values for this phase_

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
