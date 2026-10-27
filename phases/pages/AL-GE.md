# Al–Ge phases

> Al–Ge system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-GE.html · Markdown: https://data.orchid-project.org/phases/pages/AL-GE.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-GE) · [full JSON](https://data.orchid-project.org/phases/systems/AL-GE.json) · [Al–Ge system page](https://data.orchid-project.org/systems/AL-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Ge system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-al-ge-a4-diamond); _phase:al-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(Ge) 0.97865–1 | 0 | 3 |
| [BCC_A2](#phase-al-ge-bcc-a2); _phase:al-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-al-ge-fcc-a1); _phase:al-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–933.47 K, x(Ge) 0–0.02671 | 0 | 3 |
| [HCP_A3](#phase-al-ge-hcp-a3); _phase:al-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-al-ge-liquid); _phase:al-ge:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 695.88–2500 K, x(Ge) 0–1 | 0 | 3 |

## DIAMOND_A4 (Al–Ge)

- Id: `phase:al-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(Ge) 0.97865–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ge:a4-diamond)

Names (4): _corpus: _corpus:phase:al-ge:a4-diamond  
_tdb: _tdb:AlGe-06Isl.tdb:DIAMOND_A4, tdb:AlGe-79Ans-LB.tdb:DIAMOND_A4, tdb:AlGe-96Sri.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[AlGe-06Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-06Isl.tdb): DIAMOND_A4, type code %, sha256 `269b3ee97d694107…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : AL GE% : !
~~~~

[AlGe-79Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-79Ans-LB.tdb): DIAMOND_A4, type code %, sha256 `325d0fdf39329c3f…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : AL GE% : !
~~~~

[AlGe-96Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-96Sri.tdb): DIAMOND_A4, type code %, sha256 `f9456a87a28ab5ed…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : AL GE% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050) F. Islam, A.K. Thykadavil, M. Medraj, A computational thermodynamic model of the Mg–Al–Ge system, Journal of Alloys and Compounds 425, 129-139 (2006).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00034-X](https://doi.org/10.1016/S0364-5916%2896%2900034-X) S. Srikanth, D. Sanyal, P. Ramachandrarao, Calphad, 20, 321-32(1996).  
_assessment that models this phase_

## BCC_A2 (Al–Ge)

- Id: `phase:al-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ge:bcc-a2)

Names (4): _corpus: _corpus:phase:al-ge:bcc-a2  
_tdb: _tdb:AlGe-06Isl.tdb:BCC_A2, tdb:AlGe-79Ans-LB.tdb:BCC_A2, tdb:AlGe-96Sri.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlGe-06Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-06Isl.tdb): BCC_A2, type code %B, sha256 `269b3ee97d694107…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL GE : VA : !
~~~~

[AlGe-79Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-79Ans-LB.tdb): BCC_A2, type code %B, sha256 `325d0fdf39329c3f…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : AL GE : VA : !
~~~~

[AlGe-96Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-96Sri.tdb): BCC_A2, type code %B, sha256 `f9456a87a28ab5ed…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AL GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050) F. Islam, A.K. Thykadavil, M. Medraj, A computational thermodynamic model of the Mg–Al–Ge system, Journal of Alloys and Compounds 425, 129-139 (2006).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00034-X](https://doi.org/10.1016/S0364-5916%2896%2900034-X) S. Srikanth, D. Sanyal, P. Ramachandrarao, Calphad, 20, 321-32(1996).  
_assessment that models this phase_

## FCC_A1 (Al–Ge)

- Id: `phase:al-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–933.47 K, x(Ge) 0–0.02671
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ge:fcc-a1)

Names (4): _corpus: _corpus:phase:al-ge:fcc-a1  
_tdb: _tdb:AlGe-06Isl.tdb:FCC_A1, tdb:AlGe-79Ans-LB.tdb:FCC_A1, tdb:AlGe-96Sri.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlGe-06Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-06Isl.tdb): FCC_A1, type code %A, sha256 `269b3ee97d694107…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL GE : VA : !
~~~~

[AlGe-79Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-79Ans-LB.tdb): FCC_A1, type code %A, sha256 `325d0fdf39329c3f…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AL GE : VA : !
~~~~

[AlGe-96Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-96Sri.tdb): FCC_A1, type code %A, sha256 `f9456a87a28ab5ed…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AL GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050) F. Islam, A.K. Thykadavil, M. Medraj, A computational thermodynamic model of the Mg–Al–Ge system, Journal of Alloys and Compounds 425, 129-139 (2006).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00034-X](https://doi.org/10.1016/S0364-5916%2896%2900034-X) S. Srikanth, D. Sanyal, P. Ramachandrarao, Calphad, 20, 321-32(1996).  
_assessment that models this phase_

## HCP_A3 (Al–Ge)

- Id: `phase:al-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ge:hcp-a3)

Names (4): _corpus: _corpus:phase:al-ge:hcp-a3  
_tdb: _tdb:AlGe-06Isl.tdb:HCP_A3, tdb:AlGe-79Ans-LB.tdb:HCP_A3, tdb:AlGe-96Sri.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlGe-06Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-06Isl.tdb): HCP_A3, type code %A, sha256 `269b3ee97d694107…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL GE : VA : !
~~~~

[AlGe-79Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-79Ans-LB.tdb): HCP_A3, type code %A, sha256 `325d0fdf39329c3f…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : AL GE : VA : !
~~~~

[AlGe-96Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-96Sri.tdb): HCP_A3, type code %A, sha256 `f9456a87a28ab5ed…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AL GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050) F. Islam, A.K. Thykadavil, M. Medraj, A computational thermodynamic model of the Mg–Al–Ge system, Journal of Alloys and Compounds 425, 129-139 (2006).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00034-X](https://doi.org/10.1016/S0364-5916%2896%2900034-X) S. Srikanth, D. Sanyal, P. Ramachandrarao, Calphad, 20, 321-32(1996).  
_assessment that models this phase_

## LIQUID (Al–Ge)

- Id: `phase:al-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 695.88–2500 K, x(Ge) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ge:liquid)

Names (4): _corpus: _corpus:phase:al-ge:liquid  
_tdb: _tdb:AlGe-06Isl.tdb:LIQUID, tdb:AlGe-79Ans-LB.tdb:LIQUID, tdb:AlGe-96Sri.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlGe-06Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-06Isl.tdb): LIQUID, type code %, sha256 `269b3ee97d694107…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL GE : !
~~~~

[AlGe-79Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-79Ans-LB.tdb): LIQUID, type code %, sha256 `325d0fdf39329c3f…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : AL GE : !
~~~~

[AlGe-96Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGe-96Sri.tdb): LIQUID, type code %, sha256 `f9456a87a28ab5ed…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AL GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050) F. Islam, A.K. Thykadavil, M. Medraj, A computational thermodynamic model of the Mg–Al–Ge system, Journal of Alloys and Compounds 425, 129-139 (2006).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00034-X](https://doi.org/10.1016/S0364-5916%2896%2900034-X) S. Srikanth, D. Sanyal, P. Ramachandrarao, Calphad, 20, 321-32(1996).  
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
