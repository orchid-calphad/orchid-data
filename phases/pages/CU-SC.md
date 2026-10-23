# Cu–Sc phases

> Cu–Sc system: 7 phases (tier A 6, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-SC.html · Markdown: https://data.orchid-project.org/phases/pages/CU-SC.md

7 phases (tier A 6, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-SC) · [full JSON](https://data.orchid-project.org/phases/systems/CU-SC.json) · [Cu–Sc system page](https://data.orchid-project.org/systems/CU-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Sc system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-sc-bcc-a2); _phase:cu-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300.5–2498.99 K, x(Sc) 0.98615–1 | 2 | 2 |
| [CU2SC_C11B](#phase-cu-sc-cu2sc-c11b); _phase:cu-sc:cu2sc-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1166.01 K, x(Sc) 0.33333–0.33333 | 6 | 2 |
| [CU4SC_D1A](#phase-cu-sc-cu4sc-d1a); _phase:cu-sc:cu4sc-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1198.03 K, x(Sc) 0.2–0.2 | 9 | 2 |
| [CUSC_B2](#phase-cu-sc-cusc-b2); _phase:cu-sc:cusc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1401.42 K, x(Sc) 0.5–0.5 | 9 | 2 |
| [FCC_A1](#phase-cu-sc-fcc-a1); _phase:cu-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1366.7 K, x(Sc) 0–0.005 | 3 | 2 |
| [HCP_A3](#phase-cu-sc-hcp-a3); _phase:cu-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1634.6 K, x(Sc) 0.98507–1 | 5 | 2 |
| [LIQUID](#phase-cu-sc-liquid); _phase:cu-sc:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1124.64–2500 K, x(Sc) 0–1 | 20 | 2 |

## BCC_A2 (Cu–Sc)

- Id: `phase:cu-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.5–2498.99 K, x(Sc) 0.98615–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sc:bcc-a2)

Names (4): _corpus: _corpus:phase:cu-sc:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2009.10.003:βSc  
_tdb: _tdb:CuSc-08GTT.tdb:BCC_A2, tdb:CuSc-10Bo.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-08GTT.tdb): BCC_A2, type code %, sha256 `b0ac063c12480fa6…`

~~~~text
32: PHASE BCC_A2 % 2 1 3 !
33: CONST BCC_A2 : CU SC% : VA : !
~~~~

[CuSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-10Bo.tdb): BCC_A2, type code %, sha256 `6224a1e249a15cfb…`

~~~~text
37: PHASE BCC_A2 % 2 1 3 !
38: CONST BCC_A2 : CU SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0055-4](https://doi.org/10.1007/s11106-006-0055-4) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. I. The copper-scandium system, Powder Metall Met Ceram 45, 143-152 (2006).  
_cited as the source of values for this phase_

## CU2SC_C11B (Cu–Sc)

- Id: `phase:cu-sc:cu2sc-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.6667, Sc 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1166.01 K, x(Sc) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sc:cu2sc-c11b)

Names (4): _corpus: _corpus:phase:cu-sc:cu2sc-c11b  
_paper: _paper:10.1016/j.jallcom.2009.10.003:Cu2Sc  
_tdb: _tdb:CuSc-08GTT.tdb:CU2SC_C11B, tdb:CuSc-10Bo.tdb:CU2SC_C11B  


### TDB models of CU2SC_C11B (2): PHASE and CONSTITUENT statements as written

[CuSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-08GTT.tdb): CU2SC_C11B, type code %, sha256 `b0ac063c12480fa6…`

~~~~text
47: PHASE CU2SC_C11B % 2 2 1 !
48: CONST CU2SC_C11B : CU : SC : !
~~~~

[CuSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-10Bo.tdb): CU2SC_C11B, type code %, sha256 `6224a1e249a15cfb…`

~~~~text
52: PHASE CU2SC_C11B % 2 2 1 !
53: CONST CU2SC_C11B : CU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0055-4](https://doi.org/10.1007/s11106-006-0055-4) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. I. The copper-scandium system, Powder Metall Met Ceram 45, 143-152 (2006).  
_cited as the source of values for this phase_

## CU4SC_D1A (Cu–Sc)

- Id: `phase:cu-sc:cu4sc-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.8000, Sc 0.2000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1198.03 K, x(Sc) 0.2–0.2
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sc:cu4sc-d1a)

Names (4): _corpus: _corpus:phase:cu-sc:cu4sc-d1a  
_paper: _paper:10.1016/j.jallcom.2009.10.003:Cu4Sc  
_tdb: _tdb:CuSc-08GTT.tdb:CU4SC_D1A, tdb:CuSc-10Bo.tdb:CU4SC_D1A  


### TDB models of CU4SC_D1A (2): PHASE and CONSTITUENT statements as written

[CuSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-08GTT.tdb): CU4SC_D1A, type code %, sha256 `b0ac063c12480fa6…`

~~~~text
42: PHASE CU4SC_D1A % 2 4 1 !
43: CONST CU4SC_D1A : CU : SC : !
~~~~

[CuSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-10Bo.tdb): CU4SC_D1A, type code %, sha256 `6224a1e249a15cfb…`

~~~~text
47: PHASE CU4SC_D1A % 2 4 1 !
48: CONST CU4SC_D1A : CU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0055-4](https://doi.org/10.1007/s11106-006-0055-4) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. I. The copper-scandium system, Powder Metall Met Ceram 45, 143-152 (2006).  
_cited as the source of values for this phase_

## CUSC_B2 (Cu–Sc)

- Id: `phase:cu-sc:cusc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabsz and oqmd-88926, space group 221
- Stoichiometry: Cu 0.5000, Sc 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1401.42 K, x(Sc) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sc:cusc-b2)

Names (6): _corpus: _corpus:phase:cu-sc:cusc-b2  
_mp: _mp:mp-aaaaabsz  
_oqmd: _oqmd:oqmd-88926  
_paper: _paper:10.1016/j.jallcom.2009.10.003:CuSc  
_tdb: _tdb:CuSc-08GTT.tdb:CUSC_B2, tdb:CuSc-10Bo.tdb:CUSC_B2  


### TDB models of CUSC_B2 (2): PHASE and CONSTITUENT statements as written

[CuSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-08GTT.tdb): CUSC_B2, type code %, sha256 `b0ac063c12480fa6…`

~~~~text
52: PHASE CUSC_B2 % 2 1 1 !
53: CONST CUSC_B2 : CU : SC : !
~~~~

[CuSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-10Bo.tdb): CUSC_B2, type code %, sha256 `6224a1e249a15cfb…`

~~~~text
57: PHASE CUSC_B2 % 2 1 1 !
58: CONST CUSC_B2 : CU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0055-4](https://doi.org/10.1007/s11106-006-0055-4) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. I. The copper-scandium system, Powder Metall Met Ceram 45, 143-152 (2006).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Sc)

- Id: `phase:cu-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1366.7 K, x(Sc) 0–0.005
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sc:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-sc:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.10.003:Fcc_Cu  
_tdb: _tdb:CuSc-08GTT.tdb:FCC_A1, tdb:CuSc-10Bo.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-08GTT.tdb): FCC_A1, type code %, sha256 `b0ac063c12480fa6…`

~~~~text
27: PHASE FCC_A1 % 2 1 1 !
28: CONST FCC_A1 : CU% SC : VA : !
~~~~

[CuSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-10Bo.tdb): FCC_A1, type code %, sha256 `6224a1e249a15cfb…`

~~~~text
32: PHASE FCC_A1 % 2 1 1 !
33: CONST FCC_A1 : CU% SC : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0055-4](https://doi.org/10.1007/s11106-006-0055-4) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. I. The copper-scandium system, Powder Metall Met Ceram 45, 143-152 (2006).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Sc)

- Id: `phase:cu-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1634.6 K, x(Sc) 0.98507–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sc:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-sc:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.10.003:αSc  
_tdb: _tdb:CuSc-08GTT.tdb:HCP_A3, tdb:CuSc-10Bo.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-08GTT.tdb): HCP_A3, type code %, sha256 `b0ac063c12480fa6…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : CU SC% : VA : !
~~~~

[CuSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-10Bo.tdb): HCP_A3, type code %, sha256 `6224a1e249a15cfb…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : CU SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0055-4](https://doi.org/10.1007/s11106-006-0055-4) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. I. The copper-scandium system, Powder Metall Met Ceram 45, 143-152 (2006).  
_cited as the source of values for this phase_

## LIQUID (Cu–Sc)

- Id: `phase:cu-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1124.64–2500 K, x(Sc) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sc:liquid)

Names (4): _corpus: _corpus:phase:cu-sc:liquid  
_paper: _paper:10.1016/j.jallcom.2009.10.003:L  
_tdb: _tdb:CuSc-08GTT.tdb:LIQUID, tdb:CuSc-10Bo.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-08GTT.tdb): LIQUID, type code %, sha256 `b0ac063c12480fa6…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CU SC : !
~~~~

[CuSc-10Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSc-10Bo.tdb): LIQUID, type code %, sha256 `6224a1e249a15cfb…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CU SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.10.003](https://doi.org/10.1016/j.jallcom.2009.10.003) H. Bo, L.B. Liu, Z.P. Jin, Thermodynamic analysis of Al–Sc, Cu–Sc and Al–Cu–Sc system, Journal of Alloys and Compounds 490, 318-325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0055-4](https://doi.org/10.1007/s11106-006-0055-4) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. I. The copper-scandium system, Powder Metall Met Ceram 45, 143-152 (2006).  
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
