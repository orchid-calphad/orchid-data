# Cu–Fe phases

> Cu–Fe system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-FE.html · Markdown: https://data.orchid-project.org/phases/pages/CU-FE.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-FE) · [full JSON](https://data.orchid-project.org/phases/systems/CU-FE.json) · [Cu–Fe system page](https://data.orchid-project.org/systems/CU-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Fe system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-fe-bcc-a2); _phase:cu-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2499.7 K, x(Fe) 0.93114–1 | 33 | 6 |
| [FCC_A1](#phase-cu-fe-fcc-a1); _phase:cu-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1781.58 K, x(Fe) 0–1 | 53 | 6 |
| [HCP_A3](#phase-cu-fe-hcp-a3); _phase:cu-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-cu-fe-liquid); _phase:cu-fe:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1357.77–2500 K, x(Fe) 0–1 | 74 | 6 |

## BCC_A2 (Cu–Fe)

- Id: `phase:cu-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2499.7 K, x(Fe) 0.93114–1
- Literature: 33 values (33 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-fe:bcc-a2)

Names (11): _corpus: _corpus:phase:cu-fe:bcc-a2  
_paper: _paper:10.1007/bf02664678:α, paper:10.1007/bf02664678:δ, paper:10.1361/105497103770330280:α, paper:10.1361/105497103770330280:δ  
_tdb: _tdb:CuFe-03Tur.tdb:BCC_A2, tdb:CuFe-15Ste.tdb:BCC_A2, tdb:CuFe-87Jan.tdb:BCC_A2, tdb:CuFe-93Ans-LB.tdb:BCC_A2, tdb:CuFe-93Swa.tdb:BCC_A2, tdb:CuFe-95Che.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[CuFe-03Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-03Tur.tdb): BCC_A2, type code %B, sha256 `cdb9d77a4cc00a0e…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CU FE% : VA : !
~~~~

[CuFe-15Ste.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-15Ste.tdb): BCC_A2, type code %B, sha256 `bfc63223f5caef05…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CU FE% : VA : !
~~~~

[CuFe-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-87Jan.tdb): BCC_A2, type code %B, sha256 `2c05cb21e3fff528…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CU FE% : VA : !
~~~~

[CuFe-93Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Ans-LB.tdb): BCC_A2, type code %B, sha256 `e3232aa138fa336c…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CU FE% : VA : !
~~~~

[CuFe-93Swa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Swa.tdb): BCC_A2, type code %B, sha256 `4c1bc91a8d26ffd4…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU FE% : VA : !
~~~~

[CuFe-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-95Che.tdb): BCC_A2, type code %B, sha256 `2a778f43763571c5…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CU FE% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02664678](https://doi.org/10.1007/BF02664678) Q. Chen, Z.P. Jin, Metall. Mater. Trans. A, 26A, 417-26(1995).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497103770330280](https://doi.org/10.1361/105497103770330280) M. A. Turchanin, P. G. Agraval, I. V. Nikolaenko, Thermodynamics of alloys and phase equilibria in the copper-iron system, JPE 24, 307-319 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2015.08.042](https://doi.org/10.1016/j.actamat.2015.08.042) G. Stechauner, E. Kozeschnik, Thermo-kinetic modeling of Cu precipitation in α-Fe, Acta Materialia 100, 135-146 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(80)90026-7](https://doi.org/10.1016/0364-5916%2880%2990026-7) Mitsuhiro Hasebe, Taiji Nishizawa, Calculation of phase diagrams of the iron-copper and cobalt-copper systems, Calphad 4, 83-100 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(81)90036-5](https://doi.org/10.1016/0364-5916%2881%2990036-5) M. Hasebe and T. Nishizawa: “Further Study on Phase Diagram of the Iron-Copper System,” Calphad, 1981, 5, pp. 105-108.  
_cited as the source of values for this phase_
- [doi:10.1098/rsta.1957.0004](https://doi.org/10.1098/rsta.1957.0004) A. Hellawell, William Hume-Rothery, The constitution of alloys of iron and manganese with transition elements of the first long period, Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249, 417-459 (1957).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Fe)

- Id: `phase:cu-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1781.58 K, x(Fe) 0–1
- Literature: 53 values (53 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-fe:fcc-a1)

Names (12): _corpus: _corpus:phase:cu-fe:fcc-a1, corpus:phase:cu-fe:fcc-a1-2  
_paper: _paper:10.1007/bf02664678:γ, paper:10.1361/105497103770330280:γ, paper:10.1361/105497103770330280:ε  
_system_alias: _system_alias:cu-fe:epsilon  
_tdb: _tdb:CuFe-03Tur.tdb:FCC_A1, tdb:CuFe-15Ste.tdb:FCC_A1, tdb:CuFe-87Jan.tdb:FCC_A1, tdb:CuFe-93Ans-LB.tdb:FCC_A1, tdb:CuFe-93Swa.tdb:FCC_A1, tdb:CuFe-95Che.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[CuFe-03Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-03Tur.tdb): FCC_A1, type code %A, sha256 `cdb9d77a4cc00a0e…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CU% FE% : VA : !
~~~~

[CuFe-15Ste.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-15Ste.tdb): FCC_A1, type code %A, sha256 `bfc63223f5caef05…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CU% FE% : VA : !
~~~~

[CuFe-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-87Jan.tdb): FCC_A1, type code %A, sha256 `2c05cb21e3fff528…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CU% FE% : VA : !
~~~~

[CuFe-93Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Ans-LB.tdb): FCC_A1, type code %A, sha256 `e3232aa138fa336c…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CU% FE% : VA : !
~~~~

[CuFe-93Swa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Swa.tdb): FCC_A1, type code %A, sha256 `4c1bc91a8d26ffd4…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU% FE% : VA : !
~~~~

[CuFe-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-95Che.tdb): FCC_A1, type code %A, sha256 `2a778f43763571c5…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CU% FE% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497103770330280](https://doi.org/10.1361/105497103770330280) M. A. Turchanin, P. G. Agraval, I. V. Nikolaenko, Thermodynamics of alloys and phase equilibria in the copper-iron system, JPE 24, 307-319 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664678](https://doi.org/10.1007/BF02664678) Q. Chen, Z.P. Jin, Metall. Mater. Trans. A, 26A, 417-26(1995).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2015.08.042](https://doi.org/10.1016/j.actamat.2015.08.042) G. Stechauner, E. Kozeschnik, Thermo-kinetic modeling of Cu precipitation in α-Fe, Acta Materialia 100, 135-146 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(80)90026-7](https://doi.org/10.1016/0364-5916%2880%2990026-7) Mitsuhiro Hasebe, Taiji Nishizawa, Calculation of phase diagrams of the iron-copper and cobalt-copper systems, Calphad 4, 83-100 (1980).  
_cited as the source of values for this phase_
- [doi:10.1098/rsta.1957.0004](https://doi.org/10.1098/rsta.1957.0004) A. Hellawell, William Hume-Rothery, The constitution of alloys of iron and manganese with transition elements of the first long period, Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249, 417-459 (1957).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(81)90036-5](https://doi.org/10.1016/0364-5916%2881%2990036-5) M. Hasebe and T. Nishizawa: “Further Study on Phase Diagram of the Iron-Copper System,” Calphad, 1981, 5, pp. 105-108.  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Fe)

- Id: `phase:cu-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-fe:hcp-a3)

Names (7): _corpus: _corpus:phase:cu-fe:hcp-a3  
_tdb: _tdb:CuFe-03Tur.tdb:HCP_A3, tdb:CuFe-15Ste.tdb:HCP_A3, tdb:CuFe-87Jan.tdb:HCP_A3, tdb:CuFe-93Ans-LB.tdb:HCP_A3, tdb:CuFe-93Swa.tdb:HCP_A3, tdb:CuFe-95Che.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[CuFe-03Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-03Tur.tdb): HCP_A3, type code %A, sha256 `cdb9d77a4cc00a0e…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CU FE : VA : !
~~~~

[CuFe-15Ste.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-15Ste.tdb): HCP_A3, type code %A, sha256 `bfc63223f5caef05…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : CU FE : VA : !
~~~~

[CuFe-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-87Jan.tdb): HCP_A3, type code %A, sha256 `2c05cb21e3fff528…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CU FE : VA : !
~~~~

[CuFe-93Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Ans-LB.tdb): HCP_A3, type code %A, sha256 `e3232aa138fa336c…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CU FE : VA : !
~~~~

[CuFe-93Swa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Swa.tdb): HCP_A3, type code %A, sha256 `4c1bc91a8d26ffd4…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU FE : VA : !
~~~~

[CuFe-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-95Che.tdb): HCP_A3, type code %A, sha256 `2a778f43763571c5…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CU FE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02664678](https://doi.org/10.1007/BF02664678) Q. Chen, Z.P. Jin, Metall. Mater. Trans. A, 26A, 417-26(1995).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2015.08.042](https://doi.org/10.1016/j.actamat.2015.08.042) G. Stechauner, E. Kozeschnik, Thermo-kinetic modeling of Cu precipitation in α-Fe, Acta Materialia 100, 135-146 (2015).  
_assessment that models this phase_
- [doi:10.1361/105497103770330280](https://doi.org/10.1361/105497103770330280) M. A. Turchanin, P. G. Agraval, I. V. Nikolaenko, Thermodynamics of alloys and phase equilibria in the copper-iron system, JPE 24, 307-319 (2003).  
_assessment that models this phase_

## LIQUID (Cu–Fe)

- Id: `phase:cu-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1357.77–2500 K, x(Fe) 0–1
- Literature: 74 values (74 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-fe:liquid)

Names (13): _corpus: _corpus:phase:cu-fe:liquid  
_paper: _paper:10.1007/bf02664678:L, paper:10.1007/bf02664678:liq, paper:10.1361/105497103770330280:L, paper:10.1361/105497103770330280:L1, paper:10.1361/105497103770330280:L2, paper:10.1361/105497103770330280:liquid  
_tdb: _tdb:CuFe-03Tur.tdb:LIQUID, tdb:CuFe-15Ste.tdb:LIQUID, tdb:CuFe-87Jan.tdb:LIQUID, tdb:CuFe-93Ans-LB.tdb:LIQUID, tdb:CuFe-93Swa.tdb:LIQUID, tdb:CuFe-95Che.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[CuFe-03Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-03Tur.tdb): LIQUID, type code %, sha256 `cdb9d77a4cc00a0e…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CU FE : !
~~~~

[CuFe-15Ste.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-15Ste.tdb): LIQUID, type code %, sha256 `bfc63223f5caef05…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CU FE : !
~~~~

[CuFe-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-87Jan.tdb): LIQUID, type code %, sha256 `2c05cb21e3fff528…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CU FE : !
~~~~

[CuFe-93Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Ans-LB.tdb): LIQUID, type code %, sha256 `e3232aa138fa336c…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CU FE : !
~~~~

[CuFe-93Swa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-93Swa.tdb): LIQUID, type code %, sha256 `4c1bc91a8d26ffd4…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU FE : !
~~~~

[CuFe-95Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CuFe-95Che.tdb): LIQUID, type code %, sha256 `2a778f43763571c5…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CU FE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497103770330280](https://doi.org/10.1361/105497103770330280) M. A. Turchanin, P. G. Agraval, I. V. Nikolaenko, Thermodynamics of alloys and phase equilibria in the copper-iron system, JPE 24, 307-319 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664678](https://doi.org/10.1007/BF02664678) Q. Chen, Z.P. Jin, Metall. Mater. Trans. A, 26A, 417-26(1995).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2015.08.042](https://doi.org/10.1016/j.actamat.2015.08.042) G. Stechauner, E. Kozeschnik, Thermo-kinetic modeling of Cu precipitation in α-Fe, Acta Materialia 100, 135-146 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(80)90026-7](https://doi.org/10.1016/0364-5916%2880%2990026-7) Mitsuhiro Hasebe, Taiji Nishizawa, Calculation of phase diagrams of the iron-copper and cobalt-copper systems, Calphad 4, 83-100 (1980).  
_cited as the source of values for this phase_
- [doi:10.1098/rsta.1957.0004](https://doi.org/10.1098/rsta.1957.0004) A. Hellawell, William Hume-Rothery, The constitution of alloys of iron and manganese with transition elements of the first long period, Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences 249, 417-459 (1957).  
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
