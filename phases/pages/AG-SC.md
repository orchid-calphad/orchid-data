# Ag–Sc phases

> Ag–Sc system: 7 phases (tier A 6, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-SC.html · Markdown: https://data.orchid-project.org/phases/pages/AG-SC.md

7 phases (tier A 6, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-SC) · [full JSON](https://data.orchid-project.org/phases/systems/AG-SC.json) · [Ag–Sc system page](https://data.orchid-project.org/systems/AG-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Sc system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2SC_C11B](#phase-ag-sc-ag2sc-c11b); _phase:ag-sc:ag2sc-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1427.79 K, x(Sc) 0.33333–0.33333 | 7 | 2 |
| [AG4SC_D1A](#phase-ag-sc-ag4sc-d1a); _phase:ag-sc:ag4sc-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1217.88 K, x(Sc) 0.2–0.2 | 6 | 2 |
| [AGSC_B2](#phase-ag-sc-agsc-b2); _phase:ag-sc:agsc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1502.89 K, x(Sc) 0.5–0.5 | 6 | 2 |
| [BCC_A2](#phase-ag-sc-bcc-a2); _phase:ag-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1607.9–2499.64 K, x(Sc) 0.99988–1 | 5 | 2 |
| [FCC_A1](#phase-ag-sc-fcc-a1); _phase:ag-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1234.93 K, x(Sc) 0–0.11506 | 6 | 2 |
| [HCP_A3](#phase-ag-sc-hcp-a3); _phase:ag-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1812.9 K, x(Sc) 0.99985–1 | 4 | 2 |
| [LIQUID](#phase-ag-sc-liquid); _phase:ag-sc:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1167.38–2500 K, x(Sc) 0–1 | 20 | 2 |

## AG2SC_C11B (Ag–Sc)

- Id: `phase:ag-sc:ag2sc-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.6667, Sc 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1427.79 K, x(Sc) 0.33333–0.33333
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sc:ag2sc-c11b)

Names (4): _corpus: _corpus:phase:ag-sc:ag2sc-c11b  
_paper: _paper:10.1016/j.jallcom.2008.02.018:Ag2Sc  
_tdb: _tdb:AgSc-08GTT.tdb:AG2SC_C11B, tdb:AgSc-09Liu.tdb:AG2SC_C11B  


### TDB models of AG2SC_C11B (2): PHASE and CONSTITUENT statements as written

[AgSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-08GTT.tdb): AG2SC_C11B, type code %, sha256 `db418ccc9bec81b8…`

~~~~text
45: PHASE AG2SC_C11B % 2 2 1 !
46: CONST AG2SC_C11B : AG : SC : !
~~~~

[AgSc-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-09Liu.tdb): AG2SC_C11B, type code %, sha256 `e16ba0ef60c77667…`

~~~~text
50: PHASE AG2SC_C11B % 2 2 1 !
51: CONST AG2SC_C11B : AG : SC : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(75)90196-4](https://doi.org/10.1016/0022-5088%2875%2990196-4) Isolde Stapf, Gonde Kiessler, Erich Gebhardt, Das system Silber-Scandium, Journal of the Less Common Metals 39, 219-225 (1975).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868084](https://doi.org/10.1007/bf02868084) K. A. Gschneidner, F. W. Calderwood, The Ag−Sc (Silver-Scandium) system, Bulletin of Alloy Phase Diagrams 4, 375-377 (1983).  
_cited as the source of values for this phase_

## AG4SC_D1A (Ag–Sc)

- Id: `phase:ag-sc:ag4sc-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabsxm and oqmd-10666, space group 87
- Stoichiometry: Ag 0.8000, Sc 0.2000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1217.88 K, x(Sc) 0.2–0.2
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sc:ag4sc-d1a)

Names (6): _corpus: _corpus:phase:ag-sc:ag4sc-d1a  
_mp: _mp:mp-aaaabsxm  
_oqmd: _oqmd:oqmd-10666  
_paper: _paper:10.1016/j.jallcom.2008.02.018:Ag4Sc  
_tdb: _tdb:AgSc-08GTT.tdb:AG4SC_D1A, tdb:AgSc-09Liu.tdb:AG4SC_D1A  


### TDB models of AG4SC_D1A (2): PHASE and CONSTITUENT statements as written

[AgSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-08GTT.tdb): AG4SC_D1A, type code %, sha256 `db418ccc9bec81b8…`

~~~~text
40: PHASE AG4SC_D1A % 2 4 1 !
41: CONST AG4SC_D1A : AG : SC : !
~~~~

[AgSc-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-09Liu.tdb): AG4SC_D1A, type code %, sha256 `e16ba0ef60c77667…`

~~~~text
45: PHASE AG4SC_D1A % 2 4 1 !
46: CONST AG4SC_D1A : AG : SC : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868084](https://doi.org/10.1007/bf02868084) K. A. Gschneidner, F. W. Calderwood, The Ag−Sc (Silver-Scandium) system, Bulletin of Alloy Phase Diagrams 4, 375-377 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90196-4](https://doi.org/10.1016/0022-5088%2875%2990196-4) Isolde Stapf, Gonde Kiessler, Erich Gebhardt, Das system Silber-Scandium, Journal of the Less Common Metals 39, 219-225 (1975).  
_cited as the source of values for this phase_

## AGSC_B2 (Ag–Sc)

- Id: `phase:ag-sc:agsc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqqf and oqmd-10665, space group 221
- Stoichiometry: Ag 0.5000, Sc 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1502.89 K, x(Sc) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sc:agsc-b2)

Names (6): _corpus: _corpus:phase:ag-sc:agsc-b2  
_mp: _mp:mp-aaaaaqqf  
_oqmd: _oqmd:oqmd-10665  
_paper: _paper:10.1016/j.jallcom.2008.02.018:AgSc  
_tdb: _tdb:AgSc-08GTT.tdb:AGSC_B2, tdb:AgSc-09Liu.tdb:AGSC_B2  


### TDB models of AGSC_B2 (2): PHASE and CONSTITUENT statements as written

[AgSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-08GTT.tdb): AGSC_B2, type code %, sha256 `db418ccc9bec81b8…`

~~~~text
50: PHASE AGSC_B2 % 2 1 1 !
51: CONST AGSC_B2 : AG : SC : !
~~~~

[AgSc-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-09Liu.tdb): AGSC_B2, type code %, sha256 `e16ba0ef60c77667…`

~~~~text
55: PHASE AGSC_B2 % 2 1 1 !
56: CONST AGSC_B2 : AG : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(75)90196-4](https://doi.org/10.1016/0022-5088%2875%2990196-4) Isolde Stapf, Gonde Kiessler, Erich Gebhardt, Das system Silber-Scandium, Journal of the Less Common Metals 39, 219-225 (1975).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Sc)

- Id: `phase:ag-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1607.9–2499.64 K, x(Sc) 0.99988–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sc:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-sc:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.02.018:βSc  
_tdb: _tdb:AgSc-08GTT.tdb:BCC_A2, tdb:AgSc-09Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-08GTT.tdb): BCC_A2, type code %, sha256 `db418ccc9bec81b8…`

~~~~text
30: PHASE BCC_A2 % 2 1 3 !
31: CONST BCC_A2 : AG SC% : VA : !
~~~~

[AgSc-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-09Liu.tdb): BCC_A2, type code %B, sha256 `e16ba0ef60c77667…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG SC% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868084](https://doi.org/10.1007/bf02868084) K. A. Gschneidner, F. W. Calderwood, The Ag−Sc (Silver-Scandium) system, Bulletin of Alloy Phase Diagrams 4, 375-377 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90196-4](https://doi.org/10.1016/0022-5088%2875%2990196-4) Isolde Stapf, Gonde Kiessler, Erich Gebhardt, Das system Silber-Scandium, Journal of the Less Common Metals 39, 219-225 (1975).  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Sc)

- Id: `phase:ag-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1234.93 K, x(Sc) 0–0.11506
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sc:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-sc:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2008.02.018:(Ag)  
_tdb: _tdb:AgSc-08GTT.tdb:FCC_A1, tdb:AgSc-09Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-08GTT.tdb): FCC_A1, type code %, sha256 `db418ccc9bec81b8…`

~~~~text
25: PHASE FCC_A1 % 2 1 1 !
26: CONST FCC_A1 : AG% SC : VA : !
~~~~

[AgSc-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-09Liu.tdb): FCC_A1, type code %A, sha256 `e16ba0ef60c77667…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% SC : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868084](https://doi.org/10.1007/bf02868084) K. A. Gschneidner, F. W. Calderwood, The Ag−Sc (Silver-Scandium) system, Bulletin of Alloy Phase Diagrams 4, 375-377 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90196-4](https://doi.org/10.1016/0022-5088%2875%2990196-4) Isolde Stapf, Gonde Kiessler, Erich Gebhardt, Das system Silber-Scandium, Journal of the Less Common Metals 39, 219-225 (1975).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Sc)

- Id: `phase:ag-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1812.9 K, x(Sc) 0.99985–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sc:hcp-a3)

Names (4): _corpus: _corpus:phase:ag-sc:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.02.018:αSc  
_tdb: _tdb:AgSc-08GTT.tdb:HCP_A3, tdb:AgSc-09Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-08GTT.tdb): HCP_A3, type code %, sha256 `db418ccc9bec81b8…`

~~~~text
35: PHASE HCP_A3 % 2 1 0.5 !
36: CONST HCP_A3 : AG SC% : VA : !
~~~~

[AgSc-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-09Liu.tdb): HCP_A3, type code %A, sha256 `e16ba0ef60c77667…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG SC% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868084](https://doi.org/10.1007/bf02868084) K. A. Gschneidner, F. W. Calderwood, The Ag−Sc (Silver-Scandium) system, Bulletin of Alloy Phase Diagrams 4, 375-377 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90196-4](https://doi.org/10.1016/0022-5088%2875%2990196-4) Isolde Stapf, Gonde Kiessler, Erich Gebhardt, Das system Silber-Scandium, Journal of the Less Common Metals 39, 219-225 (1975).  
_cited as the source of values for this phase_

## LIQUID (Ag–Sc)

- Id: `phase:ag-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1167.38–2500 K, x(Sc) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sc:liquid)

Names (4): _corpus: _corpus:phase:ag-sc:liquid  
_paper: _paper:10.1016/j.jallcom.2008.02.018:L  
_tdb: _tdb:AgSc-08GTT.tdb:LIQUID, tdb:AgSc-09Liu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-08GTT.tdb): LIQUID, type code %, sha256 `db418ccc9bec81b8…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG SC : !
~~~~

[AgSc-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSc-09Liu.tdb): LIQUID, type code %, sha256 `e16ba0ef60c77667…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG SC : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(75)90196-4](https://doi.org/10.1016/0022-5088%2875%2990196-4) Isolde Stapf, Gonde Kiessler, Erich Gebhardt, Das system Silber-Scandium, Journal of the Less Common Metals 39, 219-225 (1975).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868084](https://doi.org/10.1007/bf02868084) K. A. Gschneidner, F. W. Calderwood, The Ag−Sc (Silver-Scandium) system, Bulletin of Alloy Phase Diagrams 4, 375-377 (1983).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
