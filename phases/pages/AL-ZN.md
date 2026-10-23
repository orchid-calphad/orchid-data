# Al–Zn phases

> Al–Zn system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/AL-ZN.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/AL-ZN.json) · [Al–Zn system page](https://data.orchid-project.org/systems/AL-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Zn system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-al-zn-bcc-a2); _phase:al-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 4 calculated diagram(s): 2473.75–2500 K, x(Zn) 0–0.01517 | 0 | 4 |
| [FCC_A1](#phase-al-zn-fcc-a1); _phase:al-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–933.47 K, x(Zn) 0–0.74215 | 48 | 5 |
| [HCP_A3](#phase-al-zn-hcp-a3); _phase:al-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1467.6 K, x(Zn) 0.94777–1 | 39 | 5 |
| [LIQUID](#phase-al-zn-liquid); _phase:al-zn:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 653.07–2500 K, x(Zn) 0–1 | 17 | 5 |

## BCC_A2 (Al–Zn)

- Id: `phase:al-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 4 calculated diagram(s): 2473.75–2500 K, x(Zn) 0–0.01517
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-zn:bcc-a2)

Names (5): _corpus: _corpus:phase:al-zn:bcc-a2  
_tdb: _tdb:AlZn-00Mat.tdb:BCC_A2, tdb:AlZn-86Mey.tdb:BCC_A2, tdb:AlZn-93Che.tdb:BCC_A2, tdb:AlZn-93Mey-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[AlZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-00Mat.tdb): BCC_A2, type code %B, sha256 `c396f22f72e3f305…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL ZN : VA : !
~~~~

[AlZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-86Mey.tdb): BCC_A2, type code %B, sha256 `e4f6db4a389e402f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AL ZN : VA : !
~~~~

[AlZn-93Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Che.tdb): BCC_A2, type code %B, sha256 `b82ac7635cfdaa7b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL ZN : VA : !
~~~~

[AlZn-93Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Mey-LB.tdb): BCC_A2, type code %B, sha256 `676cd7377477636f…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(93)90011-Y](https://doi.org/10.1016/0364-5916%2893%2990011-Y) S.-L. Chen, Y.A. Chang, Calphad, 17, 113-24(1993).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## FCC_A1 (Al–Zn)

- Id: `phase:al-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–933.47 K, x(Zn) 0–0.74215
- Literature: 48 values (42 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-zn:fcc-a1)

Names (11): _corpus: _corpus:phase:al-zn:fcc-a1  
_paper: _paper:10.1016/0364-5916(93)90011-y:fcc, paper:10.1016/0364-5916(93)90011-y:fcc1, paper:10.1016/s0364-5916(01)00004-9:fcc sol., paper:10.1016/s0364-5916(01)00004-9:fcc', paper:10.1016/s0364-5916(01)00004-9:fcc' sol.  
_tdb: _tdb:AlZn-00Mat.tdb:FCC_A1, tdb:AlZn-20Din-3g.tdb:FCC_A1, tdb:AlZn-86Mey.tdb:FCC_A1, tdb:AlZn-93Che.tdb:FCC_A1, tdb:AlZn-93Mey-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[AlZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-00Mat.tdb): FCC_A1, type code %A, sha256 `c396f22f72e3f305…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL ZN : VA : !
~~~~

[AlZn-20Din-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-20Din-3g.tdb): FCC_A1, type code %A, sha256 `d660148fb562e023…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL ZN : VA : !
~~~~

[AlZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-86Mey.tdb): FCC_A1, type code %A, sha256 `e4f6db4a389e402f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AL ZN : VA : !
~~~~

[AlZn-93Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Che.tdb): FCC_A1, type code %A, sha256 `b82ac7635cfdaa7b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL ZN : VA : !
~~~~

[AlZn-93Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Mey-LB.tdb): FCC_A1, type code %A, sha256 `676cd7377477636f…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL ZN : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90011-Y](https://doi.org/10.1016/0364-5916%2893%2990011-Y) S.-L. Chen, Y.A. Chang, Calphad, 17, 113-24(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101723](https://doi.org/10.1016/j.calphad.2019.101723) Alan Dinsdale, Ondrej Zobac, Ales Kroupa, Alexandra Khvan, Use of third generation data for the elements to model the thermodynamics of binary alloy systems: Part 1 – The critical assessment of data for the Al-Zn system, Calphad 68, 101723 (2020).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(67)90153-8](https://doi.org/10.1016/0001-6160%2867%2990153-8) L.E Larsson, Pre-precipitation and precipitation phenomena in the Al-Zn system, Acta Metallurgica 15, 35-44 (1967).  
_cited as the source of values for this phase_
- [doi:10.1039/ct8977100383](https://doi.org/10.1039/ct8977100383) Charles Thomas Heycock, Francis Henry Neville, XXXIX.—The freezing points of alloys containing zinc and another metal, J. Chem. Soc., Trans. 71, 383-422 (1897).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1936-281-1269](https://doi.org/10.1515/ijmr-1936-281-1269) Hermann Auer, Karl Ernst Mann, Magnetische Untersuchung des Systems Zink-Aluminium, International Journal of Materials Research 28, 323-328 (1936).  
_cited as the source of values for this phase_

## HCP_A3 (Al–Zn)

- Id: `phase:al-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1467.6 K, x(Zn) 0.94777–1
- Literature: 39 values (35 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-zn:hcp-a3)

Names (9): _corpus: _corpus:phase:al-zn:hcp-a3  
_paper: _paper:10.1016/0364-5916(93)90011-y:hcp, paper:10.1016/s0364-5916(01)00004-9:hcp, paper:10.1016/s0364-5916(01)00004-9:hcp sol.  
_tdb: _tdb:AlZn-00Mat.tdb:HCP_A3, tdb:AlZn-20Din-3g.tdb:HCP_A3, tdb:AlZn-86Mey.tdb:HCP_A3, tdb:AlZn-93Che.tdb:HCP_A3, tdb:AlZn-93Mey-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[AlZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-00Mat.tdb): HCP_A3, type code %A, sha256 `c396f22f72e3f305…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL ZN : VA : !
~~~~

[AlZn-20Din-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-20Din-3g.tdb): HCP_A3, type code %A, sha256 `d660148fb562e023…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL ZN : VA : !
~~~~

[AlZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-86Mey.tdb): HCP_A3, type code %A, sha256 `e4f6db4a389e402f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AL ZN : VA : !
~~~~

[AlZn-93Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Che.tdb): HCP_A3, type code %A, sha256 `b82ac7635cfdaa7b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL ZN : VA : !
~~~~

[AlZn-93Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Mey-LB.tdb): HCP_A3, type code %A, sha256 `676cd7377477636f…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL ZN : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90011-Y](https://doi.org/10.1016/0364-5916%2893%2990011-Y) S.-L. Chen, Y.A. Chang, Calphad, 17, 113-24(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101723](https://doi.org/10.1016/j.calphad.2019.101723) Alan Dinsdale, Ondrej Zobac, Ales Kroupa, Alexandra Khvan, Use of third generation data for the elements to model the thermodynamics of binary alloy systems: Part 1 – The critical assessment of data for the Al-Zn system, Calphad 68, 101723 (2020).  
_assessment that models this phase_
- [doi:10.1016/0001-6160(67)90153-8](https://doi.org/10.1016/0001-6160%2867%2990153-8) L.E Larsson, Pre-precipitation and precipitation phenomena in the Al-Zn system, Acta Metallurgica 15, 35-44 (1967).  
_cited as the source of values for this phase_
- [doi:10.1039/ct8977100383](https://doi.org/10.1039/ct8977100383) Charles Thomas Heycock, Francis Henry Neville, XXXIX.—The freezing points of alloys containing zinc and another metal, J. Chem. Soc., Trans. 71, 383-422 (1897).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1936-281-1269](https://doi.org/10.1515/ijmr-1936-281-1269) Hermann Auer, Karl Ernst Mann, Magnetische Untersuchung des Systems Zink-Aluminium, International Journal of Materials Research 28, 323-328 (1936).  
_cited as the source of values for this phase_

## LIQUID (Al–Zn)

- Id: `phase:al-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 653.07–2500 K, x(Zn) 0–1
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-zn:liquid)

Names (8): _corpus: _corpus:phase:al-zn:liquid  
_paper: _paper:10.1016/0364-5916(93)90011-y:L, paper:10.1016/s0364-5916(01)00004-9:liq.  
_tdb: _tdb:AlZn-00Mat.tdb:LIQUID, tdb:AlZn-20Din-3g.tdb:LIQUID, tdb:AlZn-86Mey.tdb:LIQUID, tdb:AlZn-93Che.tdb:LIQUID, tdb:AlZn-93Mey-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[AlZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-00Mat.tdb): LIQUID, type code %, sha256 `c396f22f72e3f305…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL ZN : !
~~~~

[AlZn-20Din-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-20Din-3g.tdb): LIQUID, type code %, sha256 `d660148fb562e023…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL ZN : !
~~~~

[AlZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-86Mey.tdb): LIQUID, type code %, sha256 `e4f6db4a389e402f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AL ZN : !
~~~~

[AlZn-93Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Che.tdb): LIQUID, type code %, sha256 `b82ac7635cfdaa7b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL ZN : !
~~~~

[AlZn-93Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlZn-93Mey-LB.tdb): LIQUID, type code %, sha256 `676cd7377477636f…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL ZN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90011-Y](https://doi.org/10.1016/0364-5916%2893%2990011-Y) S.-L. Chen, Y.A. Chang, Calphad, 17, 113-24(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101723](https://doi.org/10.1016/j.calphad.2019.101723) Alan Dinsdale, Ondrej Zobac, Ales Kroupa, Alexandra Khvan, Use of third generation data for the elements to model the thermodynamics of binary alloy systems: Part 1 – The critical assessment of data for the Al-Zn system, Calphad 68, 101723 (2020).  
_assessment that models this phase_
- [doi:10.1039/ct8977100383](https://doi.org/10.1039/ct8977100383) Charles Thomas Heycock, Francis Henry Neville, XXXIX.—The freezing points of alloys containing zinc and another metal, J. Chem. Soc., Trans. 71, 383-422 (1897).  
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
